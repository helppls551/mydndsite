from django.shortcuts import render, redirect, get_object_or_404
from .models import MyHero
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .forms import PostFrom, CommentForm
from django.forms.models import model_to_dict
from .func import dex


def info(request):
    posts = MyHero.objects.filter(created_time__lte=timezone.now()).order_by('created_time')
    return render(request, 'blog/info.html', {'posts': posts})


def post_info(request, pk):
    post = get_object_or_404(MyHero, pk=pk)
    field = model_to_dict(post)
    acrobatics = dex(field['dexterity'], field['acrobatics'])
    analysis = dex(field['dexterity'], field['analysis'])
    athletics = dex(field['strength'], field['athletics'])
    perception = dex(field['wisdom'], field['perception'])
    survival = dex(field['wisdom'], field['survival'])
    performance = dex(field['charizma'], field['performance'])
    intimidation = dex(field['charizma'], field['intimidation'])
    history = dex(field['wisdom'], field['history'])
    sleight_hand = dex(field['dexterity'], field['sleight_hand'])
    magic = dex(field['intellegence'], field['magic'])
    medicine = dex(field['wisdom'], field['medicine'])
    deception = dex(field['charizma'], field['deception'])
    nature = dex(field['wisdom'], field['nature'])
    insight = dex(field['wisdom'], field['insight'])
    religic = dex(field['intellegence'], field['religic'])
    stealth = dex(field['dexterity'], field['stealth'])
    conviction = dex(field['charizma'], field['conviction'])
    caring = dex(field['wisdom'], field['caring'])
    return render(request, 'blog/post_info.html',
                  {'post': post, 'acrobatics': acrobatics, 'analysis': analysis, 'athletics': athletics,
                   'perception': perception, 'survival': survival, 'performance': performance,
                   'intimidation': intimidation, 'history': history, 'sleight_hand': sleight_hand,
                   'magic': magic, 'medicine': medicine, 'deception': deception,
                   'nature': nature, 'insight': insight, 'religic': religic,
                   'stealth': stealth, 'conviction': conviction, 'caring': caring})


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


@login_required
def post_edit(request, pk):
    post = get_object_or_404(MyHero, pk=pk)
    if request.method == "POST":
        form = PostFrom(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_time = timezone.now()
            post.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = PostFrom(instance=post)
    return render(request, 'blog/post_new.html', {"form": form})


@login_required
def post_del(request, pk):
    post = get_object_or_404(MyHero, pk=pk)
    post.delete()
    return redirect('index')


def add_comment(request, pk):
    post = get_object_or_404(MyHero, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_info', pk=post.pk)
    else:
        form = CommentForm()
        return render(request, "blog/add_comment.html", {'form': form})
