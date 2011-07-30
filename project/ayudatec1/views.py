from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from ayudatec1.models import UserProfile

def expert_list(request):

    return render_to_response('experts_list.html', {})

def profile(request, username):
    u = get_object_or_404(UserProfile, user__username=username)    
    return render_to_response('profile.html', {'user': ' - '.join([u.user.username, u.bio, u.user.email])})
