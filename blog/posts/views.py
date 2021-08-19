from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post

# Create your views here.
class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 3
    context_object_name = 'posts'

class PostSearch(PostIndex):
    pass

class PostCategory(PostIndex):
    pass

class PostDetails(UpdateView):
    pass