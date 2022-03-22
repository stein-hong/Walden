#URLError
# import urllib.request
# import urllib.error
#
# url=''
# try:
#     response=urllib.request.urlopen(url)
# except urllib.error.URLError as e:
#     print(e.reason)


#HTTPError
import urllib.request
import urllib.error


url=''

try:
    response=urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    print('code:'+e.code+'\n')
    print('reason:'+e.reason+'\n')
    print('headers:'+ e.headers + '\n')