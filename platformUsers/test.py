from github import Github
llist = []


ACCESS_TOKEN = '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'
g = Github(ACCESS_TOKEN)
print(g.get_user().get_repos())



keywords = ['django','flask','python']

def search_github(keywords):
    
    query = '+'.join(keywords) + '+in:readme+in:description'
    print("keywords: " , keywords  , "\nquery: "  , query)
    result = g.search_repositories(query, 'stars', 'desc')

    print(f'Found {result.totalCount} repo(s)')
    i = 0
    for repo in result:
        i=i+1
        if(i==5):
            break
    return result
        
result = search_github(keywords)


i = 0

for element in result:
    i=i+1
    llist.append(element)
    if(i==10):
        break

