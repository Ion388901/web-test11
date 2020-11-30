from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
import boto3
from pprint import pprint
from botocore.config import Config
from boto3.dynamodb.conditions import Key

def post_list(request):
    dynamodb = boto3.resource('dynamodb')
    table_mensajes = dynamodb.Table('Mensajes')
    response=table_mensajes.query(KeyConditionExpression=Key('ID').eq('5'))
    mensaje= response
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print (response)
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

