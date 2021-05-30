from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from backend.models import User, Post, Follower, Profile, ConnectedUsers
import datetime

@login_required
def profile(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    users_posts = Post.objects.filter(user = user)
    return render(request, 'social/user.html', {
        'user_info': user, 
        'request_user': request.user, 
        'latest_posts_list': users_posts, 
        'latest_post': users_posts, 
    })

@login_required
def changeinfo(request):
    return render(request, 'social/change_info.html', {})

@login_required
def currentUser(request):
    current_user = request.user

    return JsonResponse({
        'current_authenticated_user_id': current_user.id
    })

def users_online(request):
    connected_users = [user for user in ConnectedUsers.objects.all()]
    return JsonResponse({
        'connected_users': len(connected_users)
    })

