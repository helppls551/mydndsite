from django.shortcuts import render,redirect,get_object_or_404
from .models import MyHero
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostFrom

def info(request):
    posts = MyHero.objects.filter(created_time__lte=timezone.now()).order_by('created_time')
    return render(request, 'blog/info.html', {'posts': posts})


def post_info(request, pk):
    post = get_object_or_404(MyHero, pk=pk)
    return render(request, 'blog/post_info.html', {'post': post})


@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostFrom(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_time = timezone.now()
            print(post.created_time)
            post.save()
            return redirect('info')
    else:
        form = PostFrom()
    return render(request, 'blog/post_new.html', {'form': form})
