from django.contrib import admin
from .models import User, Team, Task

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name', 'last_name', 'email', 'phone', 'is_user', 'is_teamleader', 'is_teammember']
admin.site.register(User, UserAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'team_leader', 'team_member']
admin.site.register(Team, TeamAdmin)

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'team', 'status', 'started_at', 'completed_at']
admin.site.register(Task, TaskAdmin)
