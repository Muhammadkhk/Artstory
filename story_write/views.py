
from story_account.models import Profile
from django.http import Http404
from django.views.generic import ListView
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from story_write.models import Writestory,Comment
from django.contrib.auth.models import User
# Create your views here.


class storyListview(ListView):
    template_name = 'story/blog.html'
    paginate_by = 21

    def get_queryset(self):
        return Writestory.objects.get_show_story()

class storyListviewprivate(LoginRequiredMixin,ListView):
    login_url = '/singin'
    redirect_field_name = '/singin'
    template_name = 'story/blog_private.html'
    paginate_by = 21
    
    
    def get_queryset(self):
        story_user1 = self.request.user.id
        story_user = self.request.user
        user1 = User.objects.get(id=story_user1)
        if user1:
            page = Writestory.objects.get_show_story_private(story_user)
            #print(page)
            if page :
                return page
            else:
                redirect('/write')
        else:
            redirect('/singin')


@login_required(login_url = '/singin')   
def story_detail(request, **kwargs):
    user_id = request.user.id
    user1 = User.objects.get(id=user_id)
    
    if user1:
        selected_story_id = kwargs['storyId']
        story: Writestory = Writestory.objects.get_by_id(selected_story_id)
        comments = Comment.objects.filter(postID = selected_story_id)

        for comment in comments:
            img = get_object_or_404(Profile, author = comment.author)
            comment.image = img.image
        
        if story is None or not story.public:
            raise Http404('404 NOT FUND')
        context = {
            'story': story,
            'comments':comments,
            }
        return render(request, 'story/story_detail.html', context)


@login_required(login_url = '/singin')
def write_story(request):
    if request.method == 'GET':
        return render(request, 'home/write.html', {})
    else:
        writestory = Writestory.objects.create (
            title = request.POST['title'],
            text = request.POST['text'],
            image = request.FILES['image'],
            public = request.POST['private'],
            author = request.user,
        )
        writestory.save()
        context={
        'title':request.POST['title']
            }
        return render(request, 'home/index.html', context)

    
@login_required(login_url = '/singin')
def write_comment(request):

    if request.method == 'GET':
        return render(request, 'story/story_detail.html', {})
    else:
        comment = Comment.objects.create (
            text = request.POST['comment'],
            author = request.user,
            postID = request.POST['post_pk']
        )
        comment.save()
        return redirect('public')


@login_required(login_url = '/singin')   
def story_detail_privat(request, **kwargs):
    
    user_id = request.user.id
    user1 = User.objects.get(id=user_id)
    
    if user1:
        selected_story_id = kwargs['storyId']
        story_private = get_object_or_404(Writestory,author=request.user,public=False,pk=selected_story_id)
        if story_private is None:
            raise Http404('404 NOT FUND')

        else:
            context = {
                'story_private': story_private,
            }

        return render(request, 'story/story_detail_private.html', context)


@login_required(login_url='/singin')
def edit_story_privat(request, **kwargs):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    selected_story_id = kwargs['storyId']
    story1 = get_object_or_404(Writestory,author=request.user,public=False,pk=selected_story_id)
    if user is None:
        raise Http404('user dosnot exsist')


    if request.method == 'GET':
        context = {
            'story':story1,
        } 
        return render(request, 'home/edit_page.html', context)

    if request.method == 'POST':
        story1.title = request.POST['title']
        story1.text = request.POST['text']
        story1.image = request.FILES['image']
        story1.public = request.POST['private']
        story1.author = request.user
        story1.save()
        if story1.public==False :
            return story_detail(request, **kwargs)
        else:
            return story_detail_privat(request, **kwargs)


@login_required(login_url='/singin')
def edit_story_public(request, **kwargs):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    selected_story_id = kwargs['storyId']
    story1 = get_object_or_404(Writestory,author=request.user,public=True,pk=selected_story_id)
    if user is None:
        raise Http404('user dosnot exsist')


    if request.method == 'GET':
        context = {
            'story':story1,
        } 
        return render(request, 'home/edit_page_public.html', context)

    if request.method == 'POST':
        story1.title = request.POST['title']
        story1.text = request.POST['text']
        story1.image = request.FILES['image']
        story1.public = request.POST['private']
        story1.author = request.user
        story1.save()
        if story1.public==False :
            return story_detail(request, **kwargs)
        else:
            return story_detail_privat(request, **kwargs)