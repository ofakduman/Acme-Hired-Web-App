from django.shortcuts import redirect, render
from github import Github
from multiprocessing import context
from platformUsers.models import PlatformUser 
# Create your views here.
MAX_RESULT = 20

def index(request):
    print("index1 e girdis")
    return render(request, 'index.html')

    

# def search(request):
#     # ACCESS_TOKEN = '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'
#     # def search_github(keywords):
#     #     g = Github(ACCESS_TOKEN)
#     #     keywords = [keyword.strip() for keyword in keywords.split(',')]
#     #     query = '+'.join(keywords) + '+in:readme+in:description'
#     #     print("keywords: " , keywords  , "\nquery: "  , query)
#     #     result = g.search_repositories(query, 'stars', 'desc')
#     #     print(f'Found {result.totalCount} repo(s)')
#     #     return result
        

#     # if request.method == "POST":
#     #     keyword = request.POST.get('keyword',"adsfdsf"); 
#     #     result = search_github(keyword)
#     #     llist = []
#     #     i = 0
#     #     for element in result:
#     #         if element.owner.type == "User":
#     #             i=i+1
#     #             llist.append(element.owner)
#     #             if i == MAX_RESULT:
#     #                 break
    
#     #     return redirect('results',{'users':llist})
#     # else:
#     #     return redirect('search')

#     return render(request, 'index.html')


def results(request, pool):
    print(type(pool))
    print("1result")
    return render(request, 'results.html')


