from urllib.parse import urlencode

OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_params = {
    'client_id': 7240520,
    # 'redirect_uri': '',
    'display': 'popup',
    'scope': 'groups',
    'response_type': 'token',
}

if __name__ == '__main__':
    print('?'.join((OAUTH_URL, urlencode(OAUTH_params))))

   # a77c6f0084336c2a55a5a4b14676b3b4272afada7b2c0e5f9878f2fa1cf14e5152915a2f8e45612a6e42f

# # token = '7615775cc19b9d451d1ba51c247423ceb5910704991584ab8f2da374d6fcfd7d921a5ed80a68404655fe9'
# token = '822a71a525f535063c2ff43461daa22ab70110fd874d879fee14aa179eb7ed440fc3fcd3785647b46697e'
#
# with open('tokenfile.txt') as f:
#     t = f.read()
# print(t)