from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail
from taggit.models import Tag

# Create your views here.
def post_list(request,  tag_slug=None):
    post_list = Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])
    """How to use panigator
        from django.core.paginator import Paginator

        objects = ["item1", "item2", "item3", "item4", "item5", "item6", "item7", "item8", "item9", "item10"]
        p = Paginator(objects, 4)       # Each page will have 4 items
        p.count -> number of posts: 10
        p.pages -> number of pages: 3
        page1 = p.page(1) 
        print(page1.object_list) -> access page1 result = : ['item1', 'item2', 'item3', 'item4']
    """
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    # Get 'page' parameter from request.GET and assigns a default value of 1 if no 'page' parameter is passed.
    # If a user visits the URL: http://example.com/?page=3, the page_number will be 3.
    # If the user visits the URL: http://example.com/, the page_number will be 1 (default value).
    page_number = request.GET.get('page', 1)
    # Visit the corresponding page to get the list of articles
    try:
        posts = paginator.get_page(page_number)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)

    # Call file templates/post/list.html
    return render(request, '_blog/post/home.html', {'posts': posts, 'tag': tag})

def post_detail(request, slug):
    post = get_object_or_404(Post,
                             slug=slug,
                             status=Post.Status.PUBLISHED)

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(request,
                  '_blog/post/post_detail.html',
                  {'post': post, 'similar_posts': similar_posts})

class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = '_blog/post/home.html'

class PostListViewBlog(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = '_blog/post/blog.html'

class CategoryView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context