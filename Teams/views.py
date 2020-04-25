from django.shortcuts import render, redirect
from django.views.generic.base import View
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import TeamModelSerializer, PlayerModelSerializer, UserModelSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.http import Http404
from .forms import *

#CBV Views

class TeamList(APIView):
    def get(self, request):
        teams = Team.objects.all()
        serializer = TeamModelSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeamModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class TeamDetailView(APIView):
    def get_object(self,pk):
        try:
            return Team.objects.get(id=pk)
        except Team.DoesNotExist:
            return Http404

    def get(self, request, pk):
        team = Team.objects.get(id=pk)
        serializer = TeamModelSerializer(team)
        return Response(serializer.data)

    def put(self, request, pk):
        team = Team.objects.get(id=pk)
        serializer = TeamModelSerializer(instance=team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        team = Team.objects.get(id=pk)
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PlayerList(APIView):
    def get(self, request):
        player = Player.objects.all()
        serializer = PlayerModelSerializer(player, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlayerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class PlayerDetailView(APIView):
    def get_object(self,pk):
        try:
            return Player.objects.get(id=pk)
        except Player.DoesNotExist:
            return Http404

    def get(self, request, pk):
        player = Player.objects.get(id=pk)
        serializer = PlayerModelSerializer(player)
        return Response(serializer.data)

    def put(self, request, pk):
        player = Player.objects.get(id=pk)
        serializer = PlayerModelSerializer(instance=player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        player = Player.objects.get(id=pk)
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#FBV Views

@api_view(['GET', 'POST'])
def team_list(request):
    if request.method == 'GET':
        teams = Team.objects.all()
        serializer = TeamModelSerializer(teams, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeamModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Team.objects.get(id=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamModelSerializer(team)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TeamModelSerializer(instance=team, data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def player_list(request):
    if request.method == 'GET':
        players = Player.objects.all()
        serializer = PlayerModelSerializer(players, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PlayerModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    @api_view(['GET', 'PUT', 'DELETE'])
    def player_detail(request, pk):
        try:
            player = Player.objects.get(id=pk)
        except Team.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = PlayerModelSerializer(player)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = PlayerModelSerializer(instance=player, data=request.data)
            if serializer.is_valid():
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        elif request.method == 'DELETE':
            player.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)




#class TeamsView(View):
#    def get(self, request):
#        teams = Team.objects.all()
#        form = TeamForm()
#
#        if request.method == 'POST':
#            form = TeamForm(request.POST)
#            if form.is_valid():
#                form.save()
#            return redirect('/')
#
#        return render(request, "teams/team_list.html", {"team_list": teams, 'form': form})



# Auth View
@api_view(['POST'])
def register(request):
    serializer = UserModelSerializer(data=request.data)
    if serializer.is_valid():
        username = request.data.get("username")
        email = request.data.get("email")
        password = request.data.get("password")
        User.objects.create(username=username, email=email)
        user = User.objects.get(username=username)
        User.set_password(user, raw_password=password)
        user.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    return Response({"errors": "Invalid data"})

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'nepravilno'})

    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)





