
from django.http import Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, get_user_model, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from story_account.models import Profile
from story_write.models import Writestory,Comment   

# Create your views here
def singin_user(request):  
    if request.method == 'GET':
        return render(request, 'account/singin_story.html', {})
        
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            context = {'error':'username and password does not match'}
            return render(request, 'account/singin_story.html',context)
        else:
            login(request, user)
            return redirect('/')

def singup_user(request):
    print(request)
    if request.user.is_authenticated:
        return redirect ('/')
    
    else:
        if request.method == 'GET':
            
            return render(request, 'account/singup_story.html', {})
        else:
            is_exists_user_by_email = User.objects.filter(email=request.POST['email']).exists()
            is_exists_user_by_username = User.objects.filter(username=request.POST['username']).exists()
            if is_exists_user_by_email:
                return render(request, 'account/singup_story.html',{'error':'this email exsist'})

            else:
                if is_exists_user_by_username:
                    return render(request, 'account/singup_story.html',{'error1':'this username exsist'})

                else:
                    if (request.POST['password'] == request.POST['repassword']):
                        user =User.objects.create_user(request.POST['username'],
                                                        email=request.POST['email'],
                                                        password=request.POST['password'])
                        user.save()
                        user1 = authenticate(request,username=request.POST['username'],password=request.POST['password'])
                        login(request, user1)
                        print(request.user)
                        profile =Profile.objects.create(firstname='empty',
                                                      lastname='empty',
                                                      email='empty',
                                                      slogan = 'empty',
                                                      text = 'empty',
                                                      image = f"logo-image/artstory.png",
                                                      author = request.user,
                                                     )
                        profile.save()
                        context={
                        'username':request.POST['username'],
                        'email':request.POST['email'], 
                        'password':request.POST['password'], 
                        'repassword':request.POST['repassword']
                        }
                        return render(request, 'home/index.html',context) 
                    else:
                        return render(request, 'account/login_story.html',{'error2':'password and re-password does not match'})

@login_required(login_url='/singin')
def my_profile_page(request):
    #site_profile = Profile.objects.filter(author=request.user)
    #print(site_profile)
    site_profile = get_object_or_404(Profile,author=request.user)
    print(site_profile)
    user_name = request.user
    
    context = {
        
        'site_profile': site_profile,
        'user_name':user_name
        
    }
    return render(request, 'account/profile.html', context)

@login_required(login_url='/singin')
def edit_user_profile(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    profiles1 = get_object_or_404(Profile,author=request.user)
    if user is None:
        raise Http404('user dosnot exsist')

    if request.method == 'GET':
        context = {
            'profile':profiles1,
            'user_name':request.user
        }
        return render(request, 'account/editprofile.html', context)
    else:
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.save()
        
        profiles1.firstname = request.POST['firstname']
        profiles1.lastname = request.POST['lastname']
        profiles1.email = request.POST['email']
        profiles1.slogan = request.POST['slogan']
        profiles1.text = request.POST['text']
        profiles1.image = request.FILES['image']
        profiles1.author = request.user
        profiles1.save()
        context={
        'firstname':request.POST['firstname']
            }
        return my_profile_page(request)

            
def singout(request):
    logout(request)
    return redirect('/')

@login_required(login_url='/singin')
def your_profile_page(request):
    user_name = get_object_or_404(Writestory,pk=request.POST['post_pk'])
    site_profile = get_object_or_404(Profile,author=user_name.author)
    context = {
        
        'site_profile': site_profile,
        
    }
    return render(request, 'account/your_profile.html', context)

@login_required(login_url='/singin')
def your_profile_page1(request):
    print(request.POST['comment_author'])
    user = get_object_or_404(User, pk = request.POST['comment_author'])
    site_profile = get_object_or_404(Profile,author= user)
    context = {
        
        'site_profile': site_profile,
        
    }
    return render(request, 'account/your_profile.html', context)