import urllib.request
import urllib.parse
import http.cookiejar
import urllib.error
import urllib.parse
import urllib.robotparser
from functools import wraps


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

# 4. 构建请求
def TestRequest():
    url = "http://httpbin.org/post"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Host": "httpbin.org"
    }
    formdata = {
        "hello": "world"
    }
    data = bytes(urllib.parse.urlencode(formdata), encoding="utf-8")
    req = urllib.request.Request(url, data, headers, method="POST")
    response = urllib.request.urlopen(req)
    print(response.read().decode("utf-8"))

# 5. 代理请求
def TestProxy():
    proxy = urllib.request.ProxyHandler({
        'http': 'http://127.0.0.1',
        'https': 'https://127.0.0.1:9743'
    })
    # 构建opener
    opener = urllib.request.build_opener()
    resp = opener.open(sBaseUrl)
    print(resp.getcode())

# 6. Cookies
def TestGetCookie():
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    resp = opener.open(sBaseUrl)
    for item in cookie:
        print(item.name,"=",item.value)

# 7. 保存和读取Cookies
def TestSaveCookies():
    filename = 'cookies.txt'
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    resp = opener.open(sBaseUrl)
    # cookie.header += "zzz"
    cookie.save(ignore_discard=True, ignore_expires=True)
    # 读取
    cookie1 = http.cookiejar.MozillaCookieJar()
    cookie1.load(filename, ignore_discard=True, ignore_expires=True)
    print(cookie1.header)

# 8. 直接设置Cookie
# opener = urllib.request.build_opener()
# cookies = {}
# opener.addheaders.append('Cookie', ';'.join('%s-%s' % (k, v) for k, v in cookies.items())

# 9. 从浏览器获取Cookie

# 10. URLError
def TestURLError():
    try:
        urllib.request.urlopen(sBaseUrl+"error")
    except urllib.error.HTTPError as e:
        print(e.code)
    except urllib.error.URLError as e:
        print(e.reason)

# 11. 测试解析URL
def TestParseURL():
    # 解析
    res = urllib.parse.urlparse(sBaseUrl + "?name=zzz")
    res1 = urllib.parse.urlsplit(sBaseUrl + "?name=zzz")
    # 拼接
    print(urllib.parse.urlunsplit(res1))
    # 断点看其内容
    # scheme //前面的内容，代表协议
    # netloc 域名，www.baidu.com
    # path 访问路径
    # params 参数
    # query 查询条件
    # fragment 描点 用于直接定位页面内部的下拉位置
    # scheme://netloc/path;params?query#fragment
    print(type(res))

# 12. 测试urlencode
def TestUrlencode():
    params = {'id': 1000, 'name': 'zzz'}
    sUrl = '%s?%s' % (sBaseUrl, urllib.parse.urlencode(params))
    print(sUrl)
    #parser_qs or parser_qsl
    res = urllib.parse.urlparse(sUrl)
    print(urllib.parse.parse_qsl(res.query))

# 13. 能否爬取
def TestParserRobots():
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(sBaseUrl + '/robots.txt')
    rp.read()
    print(rp.can_fetch('Baiduspider', 'http://www.baidu.com/p/b1'))
    print(rp.can_fetch('*', 'http://www.baidu.com/p/b1'))


if __name__ == '__main__':
    # TestUrlOpen()
    # TestUrlOpenPost()
    # TestTimeOut()
    # TestRequest()
    # TestProxy()
    # TestGetCookie()
    # TestSaveCookies()
    # TestURLError()
    # TestParseURL()
    # TestUrlencode()
    TestParserRobots()


def Test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("=========测试 ", func.__name__)
        return func(*args, **kwargs)
    return wrapper

def Name(sText = ""):
    def TestWrap(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("=========测试:", sText, func.__name__)
            return func(*args, **kwargs)
        return wrapper
    return TestWrap