import requests
import uuid

url = 'http://gank.io/api/data/%E7%A6%8F%E5%88%A9/10/1'
r = requests.get(url)

if not r.ok:
    print("error")

r_json = r.json()

items = r_json['results']

# r_img = requests.get(items[0]['url'])
# with open(str(uuid.uuid1()) + '.png', 'w') as f:
#     f.write(r_img.next)

for item in items:
    img_url = item['url']
    r_img = requests.get(img_url, allow_redirects=True)

    with open(str(uuid.uuid1()) + '.png', 'wb') as f:
        f.write(r_img.content)
