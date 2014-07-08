from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from bestblog.models import Post, PostForm


def index(request):
    return HttpResponse('Hello, World!')

def show_404(request):
    return render_to_response('404.html')

def show_n_posts(request):
    posts = Post.objects.all().order_by('-date')
    paginator = Paginator(posts, 5)
    n = request.GET.get('page')
    page = n
    try:
	posts = paginator.page(page)
    except PageNotAnInteger:
	posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'posts': posts})

def show_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render_to_response('post.html', {'post': post})

def submit_post(request):
    newPostForm = PostForm(request.POST)
    return render_to_response('newPost.html', {'newPostForm': newPostForm},
                              context_instance=RequestContext(request))

def create_new_post(request):
    print '*' * 75
    if request.method == 'POST':
        newPostForm = PostForm(request.POST)
        if newPostForm.is_valid():
            newPostForm.save()
    else:
        newPostForm = PostForm()

    # variables = RequestContext(request, {'newPostForm': newPostForm})
    posts = Post.objects.all().order_by('-date')

    # return render_to_response('index.html', {'posts': posts})
    return HttpResponseRedirect(reverse('bestblog.views.show_n_posts'))

