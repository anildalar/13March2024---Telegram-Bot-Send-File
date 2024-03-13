#import moduleName
import requests


#moduleName.methodName()

url = 'https://api.telegram.org/bot6382859668:AAFI5niH0r-L0bFyjvW6-wL75W1OK5lSv6A/sendMessage?chat_id=857452709&text=Anil3'
hdrs= {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Connection":"keep-alive"
}
response = requests.get(url,headers=hdrs)

if response.status_code == 200:
    print('Sent Successfully :) ')
    pass
else:
    print('Unable to Send :( ')
    pass

