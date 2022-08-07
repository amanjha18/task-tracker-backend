from lib2to3.pgen2 import token
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .models import Task, Team, User
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.core.mail import send_mail



class create_team(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            name = request.data['name']
            team_leader = request.data['team_leader']
            team_member = request.data['team_member']
            user_id = User.objects.get(id=request.user.id)
            if user_id.is_user==True:
                team_data = Team.objects.create(user=user_id, name=name, team_leader=team_leader, team_member=team_member) 
                team_data.save()
                return Response({"status": True, "message": "team created successfully"})
            return Response({"status": False, "message": "You are not User"})
        except:
            return Response({"status": False, "message": "something went wrong"})

class create_task(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user_id = User.objects.get(id=request.user.id)
            if user_id.is_user==True:
                name = request.data['name']
                team = request.data['team']
                tl_mail = request.data['tl_mail']
                find_team = Team.objects.filter(name=team)
                team_id = list(find_team)[0]
                task_data = Task.objects.create(user=user_id, name=name, team=team_id, status='Assigned')
                task_data.save()
                task_data_value = Task.objects.get(id=task_data.id)
                subject = 'task created succesfully'
                message = '''Hi here is task info - ,\n{}\n{}\n{}\n{}\n{}'''.format(task_data_value.name, task_data_value.team, task_data_value.status, task_data_value.started_at, task_data_value.completed_at)
                email_from = settings.EMAIL_HOST_USER
                send_mail( subject, message, email_from, tl_mail)
                return Response({"status": True, "message": "task created successfully"})
            return Response({"status": False, "message": "You are not User"})
        except:
            return Response({"status": False, "message": "something went wrong"})

class UpdateTask(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user_id = User.objects.get(id=request.user.id)
            if user_id.is_teamleader==True:
                task_id = request.data['task_id']
                check_task_id = Task.objects.get(id=task_id)
                name = request.data['name']
                team = request.data['team']
                status = request.data['status']
                started_at = request.data['started_at']
                completed_at = request.data['completed_at']
                check_task_id.name = name
                check_task_id.team = team
                check_task_id.status = status
                check_task_id.started_at = started_at
                check_task_id.completed_at = completed_at
                check_task_id.save()
                return Response({"status": True, "message": "Task Updated successfully"})
            return Response({"status": False, "message": "You are not User"})

        except:
            return Response({"status": False, "message": "something went wrong"})


# update task status by team member

class UpdateTaskStatus(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            user_id = User.objects.get(id=request.user.id)
            if user_id.is_teammember==True:
                task_id = request.data['task_id']
                check_task_id = Task.objects.get(id=task_id)
                status = request.data['status']
                check_task_id.status = status
                check_task_id.save()
                return Response({"status": True, "message": "Task Updated successfully"})
            return Response({"status": False, "message": "You are not User"})

        except:
            return Response({"status": False, "message": "something went wrong"})


class ListTask(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        tasks = Task.objects.all()
        all_task = []
        for task in tasks:
            dic = {
                "task_name": task.name,
                "task_id": task.id,
                # "team": task(Team=task.id),
                "status": task.status,
                "started_at": task.started_at,
                "completed_at": task.completed_at
            }
            all_task.append(dic)
        return Response({"status": True, "data": all_task})