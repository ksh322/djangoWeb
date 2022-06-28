from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from board.forms import PostForm
from board.models import Post, PostImage
from reply.forms import ReplyForm
from reply.models import Reply


def mainPage(request):
    return render(request, 'base.html')


@login_required(login_url='/user/login') #decorator
def create(request):

    if request.method == "GET":
        postForm = PostForm()
        context = {'postForm': postForm}
        return render(request, 'board/create.html', context)
    elif request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():

            post = postForm.save(commit=False)
            post.writer = request.user
            post.save()
            for image in request.FILES.getlist('image', None):
                postImage = PostImage()
                postImage.image = image
                postImage.post = post
                postImage.save()
            # post.image = request.FILES.get('image', None) #1개만 업로드

        return redirect('/board/read/'+str(post.id))


def list(request):
    posts = Post.objects.all().order_by('-id')

    context = {'posts': posts}

    return render(request, 'board/list.html', context)

#두가지 조회방식
#selected _ related 정방향 reply-> post // reply쪽 코드에 post가있음
#prefetch _ related 역방향 post -> reply


def read(request, bid):

    post = Post.objects.prefetch_related('reply_set').get(Q(id=bid))
    reply = Reply.objects.all()
    context = {'post': post, 'reply': reply}


    return render(request, 'board/read.html', context)


    #reply = Reply.Objects.get(Q(id=rid))


@login_required(login_url='/user/login')
def delete(request, bid):
    post = Post.objects.get(id=bid)
    if request.user != post.writer:
        return redirect('/board/list')

    post.delete()
    return redirect('/board/list')


@login_required(login_url='/user/login')
def update(request, bid):

    post = Post.objects.get(Q(id=bid))
    if request.method == "GET":

        context = {'post': post}
        return render(request,"board/update.html",context)
    elif request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            post.title = postForm.cleaned_data['title']
            post.contents = postForm.cleaned_data['contents']
            post.writer = request.user
            post.save()
        return redirect('/board/read/' + str(post.id))


@login_required(login_url='/user/login')
def like(request,bid):
    post = Post.objects.get(Q(id=bid))
    user = request.user

    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        return JsonResponse({'message': 'deleted', 'like_cnt': post.like.count()})
    else:
        post.like.add(request.user)
        return JsonResponse({'message': 'added' , 'like_cnt': post.like.count()})


