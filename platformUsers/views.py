from ast import keyword
import logging
from pickle import NONE
from django.shortcuts import redirect, render
#from .models import *
from multiprocessing import pool,context
from github import Github


# Create your views here.
from django.http import HttpResponse
from platformUsers.models import*

MAX_RESULT = 100
KEYWORDS = []
pool = []

def search_keyword():
    ACCESS_TOKEN = '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'
    global KEYWORDS
    global pool

    def search_github(keywords):
        g = Github(ACCESS_TOKEN)
        keywords = [keyword.strip() for keyword in keywords.split(',')]
        query = '+'.join(keywords) + '+in:readme+in:description'
        print("keywords: " , keywords  , "\nquery: "  , query)
        result = g.search_repositories(query, 'stars', 'desc')
        print(f'Found {result.totalCount} repo(s)')
        return result


    result = search_github(KEYWORDS)

    i = 0
    for element in result:
        if element.owner.type == "User":
            i=i+1
            pool.append(element.owner)
            if i == MAX_RESULT:
                break
    return 

def index(request):
    return render(request, 'index.html')

def search(request):
    
    if request.method == "POST":
        global MAX_RESULT
        global KEYWORDS
        KEYWORDS = request.POST.get('keyword',"adsfdsf"); 
        search_keyword()
        return redirect(results)
    else:
        return render(request, 'search.html')

def fav_history(request):
    all_users = PlatformUser.objects.all()
    return render(request, 'results2.html',{'users': all_users})

def results(request):
    global pool

    if request.method == "POST":
        login = request.POST.get('system')
        index = 0
        for i in range(len(pool)):
            if pool[i].login == login:
                index = i
        #if its not in the db adds it to db
        blog = ""
        auser = pool[index]
        if auser.blog !=None:
            blog = auser.blog.replace("http://","")
            blog = blog.replace("https://","")

        if not PlatformUser.objects.filter(git_id=auser.id):
            user = PlatformUser(git_id = auser.id, name = auser.name, label = "mobile developer",
            avatar_url = auser.avatar_url, favourite = True,html_url=auser.html_url,
            email=auser.email ,login=auser.login, platform_type="GitHub",
            company=auser.company,blog=blog,location=auser.location,bio=auser.bio,followers = auser.followers, following= auser.following,
            public_repos=auser.public_repos, public_gists=auser.public_gists)
            user.save()

        return render(request, 'profile_card.html',{"user":pool[index]})

    
        

    return render(request, 'results.html',{'users':pool})


def results2(request):
    if request.method == "POST":
        login = request.POST.get('system')
        index = 0
    
    all_users = PlatformUser.objects.all()
    for i in range(len(all_users)):
        if all_users[i].login == login:
            print(i)
            index = i

    return render(request, 'profile_card.html',{"user":all_users[index]})
    

    

def profile_card(request,username='default'):
    return render(request,'profile_card.html')

    
def fav_history(request):
    all_users = PlatformUser.objects.all()
    return render(request, 'results2.html',{'users': all_users})



