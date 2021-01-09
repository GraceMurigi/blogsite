from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Post, Comment

def index(request): 
    latest_posts_list = Post.objects.order_by('-pub_date')[:3]
    template = loader.get_template('blog/home.html')
    context = {
        'latest_posts_list' : latest_posts_list,
    }
    return HttpResponse(template.render(context, request))

def post(request, post_id):
    response = "You're viewing post %s."
    return HttpResponse(response % post_id)
    
def comments(request, post_id):
    return HttpResponse("You're looking at the comments for post %s." % post_id)
