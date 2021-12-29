import unittest
import requests
import re
from LearnSpider.test_code import Name

sBaseUrl = "http://www.baidu.com/"
sJsonUrl = "http://httpbin.org/"

class RequestTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @Name("Get方法")
    def test_1(self):
        params = {
            'name': 'polo',
            'age': 12
        }
        r = requests.get(sJsonUrl + 'get', params)
        print(r.status_code)
        print(r.text)
        print(r.json())

    @Name("知乎发现")
    def test_explore(self):
        sUrl = 'https://www.zhihu.com/explore'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        }
        r = requests.get(sUrl, headers=headers)
        # print(r.text)
        pattern = re.compile('"title":.*?",', re.S)
        titles = re.findall(pattern, r.text)
        titles = [title[8:] for title in titles if len(title) > 12]
        for title in titles:
            print(title)

    @Name("二进制数据")
    def test_icon(self):
        sUrl = 'https://github.com/favicon.ico'
        r = requests.get(sUrl)
        print(r.content)
        with open('./others/favicon.ico', 'wb') as f:
            f.write(r.content)

    @Name("Post")
    def test_post(self):
        params = {
            'name': 'polo',
            'age': 12
        }
        r = requests.post(sJsonUrl + "post", params)
        print(r.text)
        print(requests.codes.bad_gateway)

    @Name("文件上传")
    def test_upload(self):
        with open('./others/favicon.ico', 'rb') as f:
            files = {'file': f}
            print(files)
            r = requests.post(sJsonUrl + "post", files=files)
            print(r.text)


    @Name("获取Cookies")
    def test_getcookies(self):
        r = requests.get(sBaseUrl)
        print(r.cookies.items())

    @Name("设置Cookies")
    def test_setcookies(self):
        headers = {
            'Cookie': '"ABC"="10000"',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
        }
        r = requests.get(sBaseUrl)
        print(r.cookies.items())

    @Name("会话维持")
    def test_session(self):
        with requests.Session() as r:
            r.get(sJsonUrl + 'cookies/set/abc/10000')
            res = r.get(sJsonUrl + 'cookies')
            print(res.text)

    @Name("先构造Request, 再请求")
    def test_Request(self):
        with requests.Session() as s:
            req = requests.Request('GET', sBaseUrl)
            preppped = s.prepare_request(req)
            r = s.send(preppped)
            print(r.status_code)

