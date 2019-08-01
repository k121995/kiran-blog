from django.shortcuts import render,get_object_or_404
from blogapp.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.core.mail import send_mail
from blogapp.forms import EmailForm,CommentForm
from taggit.models import Tag

# Create your views here.
def post_list_view(request,tag_slug=None):
    post_list=Post.objects.all()
    tag=None
    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        post_list=post_list.filter(tags__in=[tag])

    paginator=Paginator(post_list,3)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        post_list=paginator.page(1)
    except EmptyPage:
        post_list=paginator.page(paginator.num_pages)
    return render(request,'post_list.html',{'post_list':post_list,'tag':tag})

def post_detail_view(request,year,month,day,post):
    cpost=get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day,
        )
    comments=cpost.comments.filter(active=True)
    csubmit=False
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            new_comment=form.save(commit=False)
            new_comment.post=cpost
            new_comment.save()
            csubmit=True
    else:
        form=CommentForm()
    return render(request,'post_detail.html',{'post':post,'csubmit':csubmit,'form':form,'comments':comments})

def mail_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method== 'POST':
        form=EmailForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recommand to you read"{}"'.format(cd['name'],cd['email'],post.title)
            post_url=request.build_absolute_url(post.get_absolute_url())
            message='Read post At:\n {}\n\n{}'
            Comments:'\n{}'.format('post_url',cd['name'],cd['comments'])
            send_mail(
                subject,
                message,
                'kiran.sonawne135@gmail.com',
                [cd['to']])
            sent=True
    else:
        form=EmailForm()
    return render(request,'email.html',{'form':form,'post':post,'sent':sent})
