### 安装
找到pip.exe, 通过pip安装  
pip install requests

安装有问题时可能需要升级pip  
python -m pip install --upgrade pip

---
### Get请求
    request.get(url, params=None, **kwargs)

kwargs用来传递hearder,cookie等信息

如果返回的结果是json格式的，可以直接调用json()方法返回字典 

#### 抓取二进制数据
    r.content： 二进制数据
---
### Post请求

### 状态码查询
    request.codes
---

### 高级用法
#### 文件上传
    request.post(url, files=files)

#### Cookies
    获取打印cookies
    print(r.cookies.items())

    设置cookies,将浏览器cookies复制到header中

#### 会话维持
    request.Session().get(...)

#### 设置代理
    proxies = {
        “http": ...,
        "https": ...,
    }

#### 身份认证
    from request.auth import HTTPBasicAuth
    r = request.get(url, auth=HTTPBasicAuth('username', 'password')