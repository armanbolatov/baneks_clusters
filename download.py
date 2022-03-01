import vk_api
import csv

login, password = 'login', 'password'
vk_session = vk_api.VkApi(login, password)

try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)

tools = vk_api.VkTools(vk_session)

wall = tools.get_all('wall.get', 100, {'owner_id': -45491419})
print('Posts count:', wall['count'])
if wall['count']:
    print('First post:', wall['items'][0], '\n')
if wall['count'] > 1:
    print('Last post:', wall['items'][-1])

headers = ['id', 'text']
with open('posts.csv', 'w', encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    for i in range(wall['count']):
        post = wall['items'][i]['text'].replace('\n', ' ').replace('\r', '')
        if len(post.split()) > 0:
            writer.writerow([i, "%s" % post])
