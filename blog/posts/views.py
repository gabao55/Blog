from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from posts.models import Post
from django.db.models import Q, Count, Case, When
from comments.forms import FormComment
from comments.models import Comments
from django.contrib import messages

# Create your views here.
class PostIndex(ListView):
    model = Post
    template_name = 'posts/index.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.select_related('post_category')
        qs = qs.order_by('-post_date').filter(post_published=True)
        qs = qs.annotate(
            comments_number=Count(
                Case(
                    When(comments__comment_published=True, then=1)
                )
            )
        )
        return qs

class PostSearch(PostIndex):
    template_name = 'posts/post_search.html'

    def get_queryset(self):
        qs = super().get_queryset()
        term = self.request.GET.get('term')

        if not term:
            return qs

        qs = qs.filter(
            Q(post_tittle__icontains=term) | 
            Q(post_author__first_name__iexact=term) | 
            Q(post_content__icontains=term) | 
            Q(post_excerpt__icontains=term) | 
            Q(post_category__cat_name__iexact=term)
        )

        return qs

class PostCategory(PostIndex):
    template_name = 'posts/post_category.html'

    def get_queryset(self):
        qs = super().get_queryset()

        category = self.kwargs.get('category', None)

        if not category:
            return qs

        qs = qs.filter(post_category__cat_name__iexact=category)
        
        return qs

class PostDetails(UpdateView):
    template_name = 'posts/post_details.html'
    model = Post
    form_class = FormComment
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = Comments.objects.filter(comment_published=True, post_comment=post.id)
        context['comments'] = comments

        return context

    def form_valid(self, form):
        post = self.get_object()
        comment = Comments(**form.cleaned_data)
        comment.post_comment = post

        if self.request.user.is_authenticated:
            comment.comment_user = self.request.user

        comment.comment_published = True
        comment.save()
        messages.success(self.request, 'Comment saved successfuly.')
        return redirect('post_details', pk=post.id)