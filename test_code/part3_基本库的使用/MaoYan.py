import unittest
import requests
import re
import time
from . import Name

sJsonUrl = "http://httpbin.org/"
sBaseUrl = "http://www.maoyan.com/board/4"
data = {
    'requestCode':'628bd00fa405ed46172adf6fc19a971ckugrl'
}
headers = {
    'Cookies': '__mta=49689241.1640780728659.1640782751776.1640783295885.9; uuid_n_v=v1; uuid=66D4904068A211EC9A7335D0F2FDBB1BDCF03AF6F6A84D5F97F79C471DC8F61C; _csrf=7082800cb10410f45d0cab5781c4bb5ee963aca78eb8166174c467d9953fb6c9; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1640780729; _lxsdk_cuid=17e0627092ec8-0e1960dd3d391f-3b39580e-1fa400-17e0627092fc8; _lxsdk=66D4904068A211EC9A7335D0F2FDBB1BDCF03AF6F6A84D5F97F79C471DC8F61C; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1640783296; _lxsdk_s=17e06270931-aad-94d-32f||19',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}

class RETest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def getcontent(self):
        # time.sleep(5)
        # r = requests.get(sBaseUrl, data, headers=headers)
        # return r.text
        with open('../others/maoyan.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return "".join(lines)

    def test_spider(self):
        content = self.getcontent()
        p = r'<div class="movie-item-info">.*?data-val="{movieId:\d+.*?>(.*?)' \
            r'</a></p>.*?star">(.*?)' \
            r'</p>.*?releasetime">(.*?)' \
            r'</p>'
        res = re.findall(p, content, re.S)
        for r in res:
            print("--------------------")
            for t in r:
                print(t.strip())