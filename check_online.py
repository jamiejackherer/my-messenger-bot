#To get a list of all online users.
import requests,traceback,json
param = {}
param['q'] = "SELECT uid, name, pic_square, online_presence FROM user WHERE online_presence IN ('active', 'idle') AND uid IN (SELECT uid2 FROM friend WHERE uid1 = me())"
param['access_token'] = '1802541026526492|7RLiplBL2uZ6s8CFSxEIRXp7L5Y'
param['method'] = 'GET'
try:
  response = requests.get("https://graph.facebook.com/fql%22,params=param")
except:
   print traceback.print_exc()
if response.status_code==200:
    for eachItem in json.loads(response.text)['data']:
        print eachItem['name'],'  is  ',eachItem['online_presence']
else:
    print traceback.print_exc()
