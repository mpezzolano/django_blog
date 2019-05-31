from django.shortcuts import render, render_to_response, HttpResponseRedirect, get_object_or_404
from blog.models import Post
from blog.forms import PostForm
from django.contrib import messages

def posts(request):
    return render_to_response('posts.html', {"posts": Post.objects.all(), "messages" : messages.get_messages(request)} )

def add_post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save();
            messages.add_message(request, messages.SUCCESS, 'POST GUARDADO CORRECTAMENTE')
            return HttpResponseRedirect('/posts/')
    return render (request, 'form_posts.html', {'form':form})

def update_post(request, postId):
    instance = get_object_or_404(Post, id=postId)
    form = PostForm (request.POST or NONE, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save();
            messages.add_message(request, messages.SUCCESS, 'POST actualizado CORRECTAMENTE')
            return HttpResponseRedirect('/posts/list/')
    return render (request, 'form_post.html', {'form':form})

def delete_post(request, postId):
    instance = get_object_or_404(Post, id=postid)
    instance.delete()
    messages.add_message(request, messages.SUCCESS, 'E eliminado CORRECTAMENTE')
    return HttpResponseRedirect('/posts/list/')
