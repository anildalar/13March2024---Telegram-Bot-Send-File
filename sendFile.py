#import moduleName
import requests


#moduleName.methodName()

url = 'https://api.telegram.org/bot6382859668:AAFI5niH0r-L0bFyjvW6-wL75W1OK5lSv6A/sendDocument'

f = open("a.png", "rb")

fls = {'document': f}
dt = {'chat_id': "857452709"}


response = requests.post(url,files=fls, data=dt)

if response.status_code == 200:
    print('File Sent Successfully :) ')
    pass
else:
    print('Unable to Send File :( ')
    pass


f.close()

