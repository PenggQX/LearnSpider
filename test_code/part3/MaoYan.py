import unittest
import re
import requests
import time
from . import Name

sJsonUrl = "http://httpbin.org/"
sBaseUrl = "http://www.maoyan.com/board/4"
data = {
    'requestCode':'fab8219b454addd43191dc03118cc9b9yxebf'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
}

class RETest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def getpattern(self):
        p = r'<div class="movie-item-info">.*?data-val="{movieId:\d+.*?>(.*?)' \
            r'</a></p>.*?star">(.*?)' \
            r'</p>.*?releasetime">(.*?)' \
            r'</p>'
        return re.compile(p, re.S)

    def getallcontent(self):
        p = self.getpattern()
        lMovie = []
        iTop = 0
        for i in range(10):
            s = self.getcontent(iOffset=i)
            res = p.findall(s)
            for m in res:
                iTop += 1
                lMovie.append(("--------------- %s" % iTop,))
                lMovie.append(m)
        lMovie = [l.strip() for t in lMovie for l in t]
        with open('../others/maoyan_movie.txt', 'w', encoding='utf-8') as f:
            f.write("\n".join(lMovie))

    def getcontent(self, iOffset):
        time.sleep(2)
        if iOffset:
            data['offset'] = iOffset
        r = requests.get(sBaseUrl, data, headers=headers)
        if r.status_code == requests.codes.ok:
            print("============ %s" % iOffset)
            print(len(r.text))
            return r.text
        return ""
        # with open('../others/maoyan.txt', 'r', encoding='utf-8') as f:
        #     lines = f.readlines()
        #     return "".join(lines)

    def test_spider(self):
        self.getallcontent()