from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sitemaps import Sitemap
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import ListView, DetailView, DeleteView
from django.views.generic.base import View

from blog.forms import PostCreateForm
from blog.models import Post
from blog.utils import get_read_time
from comment.forms import CommentForm
from comment.models import Comment
from users.models import User


class ArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.timestamp

    def location(self, obj):
        return obj.get_absolute_url()


class UserArticleSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8
    protocol = 'http'

    def items(self):
        return User.objects.all()

    def location(self, obj):
        return f'/blog/%23/%23/{obj.username}/'


class BlogListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'HomePage/blog/blog.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        username = self.request.GET.get('username')
        post = Post.objects.all()
        if query:
            object_list = post.filter(
                Q(category__icontains=query) |
                Q(description__icontains=query) |
                Q(user__username__icontains=query) |
                Q(title__icontains=query)
            ).distinct()
        elif username:
            object_list = post.filter(user__username__icontains=username)
        else:
            object_list = Post.objects.all()
        return object_list


def blog_user_list_view(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
        if user:
            page = request.GET.get('page', 1)

            post = Post.objects.filter(user=user)
            paginator = Paginator(post, 10)
            try:
                post = paginator.page(page)
            except PageNotAnInteger:
                post = paginator.page(1)
            except EmptyPage:
                post = paginator.page(paginator.num_pages)
            return render(request, 'HomePage/blog/blog_user.html', {'post': post, 'user': user})
    else:
        return redirect('blog:blog_list')


class BlogDetailView(DetailView):
    template_name = 'HomePage/blog/blog-single.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = context['object']
        """ note this instance.get_content_type is from our models where we 
        linked the comment models and the blog models with content_type and object_id """
        context['comment'] = instance.get_content_type

        print('read time :', get_read_time(instance.description))
        print('read time :', get_read_time(instance.get_markdown()))

        context['form'] = CommentForm()
        return context


class DeletePostView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'HomePage/blog/post_delete.html'
    success_url = '/blog/'


@login_required
def create_comment(request, slug=None):
    try:
        instance = Post.objects.get(slug=slug)
    except ObjectDoesNotExist:
        instance = None
    form = CommentForm(request.POST or None)
    print('The form data :', form)
    if form.is_valid():
        print(form.cleaned_data)
        form_data = form.save(commit=False)
        form_data.user = request.user
        form_data.content_type = instance.get_content_type
        form_data.object_id = instance.id
        form_data.parent = None
        try:
            parent_id = int(request.POST.get('parent_id'))
        except:
            parent_id = None

        if parent_id:
            parent_qs = Comment.objects.filter(id=parent_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_obj = parent_qs.first()
                print('parent_obj :', parent_obj)
                form_data.parent = parent_obj
        form.save()
        messages.success(request, 'form has being submitted')
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, f'{form.errors}')
    return redirect('blog:blog_detail', instance.slug)
