import urllib.request
import urllib.parse

sBaseUrl = "http://www.baidu.com"

# 1. urlopen发送get请求
def TestUrlOpen():
    response = urllib.request.urlopen(sBaseUrl)
    print(type(response)) # HTTPResponse对象
    # print(response.read().decode("utf-8"))
    # 通过断点看 属性和接口
    for sAttr in ('msg', 'version', 'url', 'code', 'headers', 'reason'):
        print("%s: %s" % (sAttr, getattr(response, sAttr)))
    print(response.status)
    print(response.getheader('Server'))

# 2. urlopen发送post请求
def TestUrlOpenPost():
    url = "http://httpbin.org/post"
    formdata = {"world": "hello"}
    response = urllib.request.urlopen(url, bytes(
        urllib.parse.urlencode(formdata), encoding="utf8"))
    print(response.read().decode("utf-8"))

# 3. urlopen time_out参数
def TestTimeOut():
    try:
        response = urllib.request.urlopen(sBaseUrl, timeout=0.01)
        print(response.getcode())
    except Exception as e:
        print(e)



if __name__ == '__main__':
    # TestUrlOpen()
    # TestUrlOpenPost()
    TestTimeOut()