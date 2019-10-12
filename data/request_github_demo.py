import requests
import json

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)

r_json = r.json()

total_count = r_json['total_count']
print(total_count)

items = r_json['items']
print(len(items))

# for item in items:
#     print(sorted(item.keys()))

repo_dict = items[0]
print("\nSelected information about first repository:")
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])

# with open('gank_io_fuli.json') as fs:
#     result = json.load(fs)
#
# print(result)
