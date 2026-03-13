from django.shortcuts import render
from django.views.generic import DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Blog

# Create your views here.


# @cache_page(60 * 5)
def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', context={'blogs': get_recent_blogposts()})


@method_decorator(cache_page(60 * 2), name='dispatch')
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blogdetail.html'


# Low level cache API
# Caching a queryset response that can be used in view and template
def get_recent_blogposts():
    posts = cache.get('recent-posts')
    if not posts:
        posts = Blog.objects.all()
        cache.set('recent-posts', posts, 60 * 5)  # cache for 10 minutes
    return posts


def paginated_blogposts(request):
    posts_list = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'posts': posts})
