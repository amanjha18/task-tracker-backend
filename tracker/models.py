
from xml.parsers.expat import model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,Group
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):
    '''
    create user-Manager class
    '''
    def create_superuser(self, email, password):
        user=self.model(email=email)
        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
class User(AbstractBaseUser,PermissionsMixin):
    '''
    create custom user modal
    '''
    first_name=models.CharField("User First Name",max_length=50,null=False,blank=False)
    last_name=models.CharField("User Last Name", max_length=50, null=False, blank=False)
    email = models.EmailField("User Email", null=False, blank=False,unique=True, error_messages={"unique":"OOPS,This Email is Already Registered"})
    phone = models.IntegerField("User Phone", null=True, blank=True, unique=True, error_messages={"unique":"this mobile number is already exist"})
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    is_active = models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    is_user = models.BooleanField('user status', default=False)
    is_teamleader = models.BooleanField('team-leader status', default=False)
    is_teammember = models.BooleanField('team-member status', default=False)
    objects=UserManager()
    # notice the absence of a "Password field", that is built in.
    USERNAME_FIELD = 'email'

class Team(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    team_leader = models.CharField(max_length=255, null=False, blank=False)
    team_member = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.name

class Task(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    STATUS_CHOICES = (
        ("ASSIGNED", "Assigned"),
        ("INPROGRESS", "Inprogress"),
        ("UNDER REVIEW", "Under Review"),
        ("DONE", "Done"),
    )

    status = models.CharField(max_length=15,
                  choices=STATUS_CHOICES,
                  default="Assigned")
    started_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
