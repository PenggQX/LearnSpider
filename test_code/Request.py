import unittest
from functools import wraps
import requests

def Test(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("=========测试 ", func.__name__)
        return func(*args, **kwargs)
    return wrapper

class RequestTest(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @Test
    def test_1(self):
        print("aaaaaaaaaaa")
        print(requests)

