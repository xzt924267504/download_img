import requests
from PIL import Image
from io import BytesIO
import re
import random
import threading
from contextlib import closing

class demo():
    def __init__(self):
        self.li = []

    def response(self,url):
        # 获取整个页面
        response = requests.get(url)
        self.responsetext = response.text
        return self.responsetext


    def rehtml(self):
        # 正则匹配页面的html后缀
        html = re.findall(r'href="(.*?.html)">',self.responsetext)
        for i in html:
            self.response(i)
            # 正则匹配页面的img
            img = re.findall(r'<p><img src="(.*?)" alt="',self.response(i))
            # 匹配成功的加到__init的li列表
            self.li.append(img)

    def new_download_img(self):
        for i in self.li:
            for j in i:
                img_url = j
                aa = random.randint(1, 1000000)
                with closing(requests.get(img_url, stream=True)) as response:
                    chunk_size = 1024  # 单次请求最大值
                    content_size = int(response.headers['content-length'])  # 内容体总大小
                    data_count = 0
                    with open('./img_download/img{}.jpg'.format(aa), "wb") as file:
                        for data in response.iter_content(chunk_size=chunk_size):
                            file.write(data)
                            data_count = data_count + len(data)
                            now_jd = (data_count / content_size) * 100
                            print("\r 文件下载进度：{}%({}KB/{}KB) - {}"
                                  .format(int(now_jd), int(data_count/1024), int(content_size/1024),img_url), end=" ")
                print('')



if __name__ == '__main__':
    d = demo()
    d.response("http://lab.scrapyd.cn")
    d.rehtml()
    d.new_download_img()








"""

# 请求下载地址，以流式的。打开要下载的文件位置。
with requests.get('http://down.360safe.com/setup.exe', stream=True) as r, open('setup.exe', 'wb') as file:
# 请求文件的大小单位字节B
total_size = int(r.headers['content-length'])
# 以下载的字节大小
content_size = 0
# 进度下载完成的百分比
plan = 0
# 请求开始的时间
start_time = time.time()
# 上秒的下载大小
temp_size = 0
# 开始下载每次请求1024字节
for content in r.iter_content(chunk_size=1024):
file.write(content)
# 统计以下载大小
content_size += len(content)
# 计算下载进度
plan = (content_size / total_size) * 100
# 每一秒统计一次下载量
if time.time() - start_time > 1:
    # 重置开始时间
    start_time = time.time()
    # 每秒的下载量
    speed = content_size - temp_size
    # KB级下载速度处理
    if 0 <= speed < (1024 ** 2):
        print(plan, '%', speed / 1024, 'KB/s')
    # MB级下载速度处理
    elif (1024 ** 2) <= speed < (1024 ** 3):
        print(plan, '%', speed / (1024 ** 2), 'MB/s')
    # GB级下载速度处理
    elif (1024 ** 3) <= speed < (1024 ** 4):
        print(plan, '%', speed / (1024 ** 3), 'GB/s')
    # TB级下载速度处理
    else:
        print(plan, '%', speed / (1024 ** 4), 'TB/s')
    # 重置以下载大小

"""
'''
 url = 'https://download.jetbrains.com/idea/ideaIU-2018.2.1.exe'
    with closing(requests.get(url, stream=True)) as response:
        chunk_size = 1024  # 单次请求最大值
        content_size = int(response.headers['content-length'])  # 内容体总大小
        data_count = 0
        with open('idea.exe', "wb") as file:
            for data in response.iter_content(chunk_size=chunk_size):
                file.write(data)
                data_count = data_count + len(data)
                now_jd = (data_count / content_size) * 100
                print("\r 文件下载进度：%d%%(%d/%d) - %s" % (now_jd, data_count, content_size, url), end=" ")
'''



