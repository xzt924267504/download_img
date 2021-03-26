import requests
import random
from contextlib import closing
import re
class Download_setu():
    def __init__(self):
        self.headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,"
                      "image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0"
        }
        self.url = "https://www.412bbfe04acb0995.com"
    def get_html(self,url):
        self.response = requests.get(url,headers = self.headers)
        self.response.encoding = self.response.apparent_encoding
        # print(self.response.text)
        self.response_text = self.response.text

    def get_re_half_http(self):
        self.half_http = re.findall(r'<a href="(.*?.html)" target="_blank">', self.response_text)

    def splicing_url(self):
        with open('./splicing_url.txt', 'w', encoding='utf8')as f:
            for list in self.half_http:
                complete_url = self.url + list
                print(complete_url)
                # f.write(complete_url+'\n')
            f.close()
    def new_download_img(self,url):
        url = url
        img_url = url
        aa = random.randint(1, 10000000)
        with closing(requests.get(img_url, stream=True)) as response:
            chunk_size = 1024  # 单次请求最大值
            content_size = int(response.headers['content-length'])  # 内容体总大小
            data_count = 0
            with open(r'./leaen_download_img/img_download/img{}.png'.format(aa), "wb") as file:
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    data_count = data_count + len(data)
                    now_jd = (data_count / content_size) * 100
                    print("\r 文件下载进度：{}%({}KB/{}KB) - {}"
                          .format(int(now_jd), int(data_count / 1024), int(content_size / 1024), img_url), end=" ")
        print('')



if __name__ == '__main__':
    url = "https://www.412bbfe04acb0995.com/tupian/list-%E5%81%B7%E6%8B%8D%E8%87%AA%E6%8B%8D.html"
    do = Download_setu()
    do.get_html(url)
    do.get_re_half_http()
    do.splicing_url()



















'''
  <li><a href="(链接后半)" title="(标题)" target="_blank"><span>(日期)</span>
  卡亚欧偷乱精同美

'''