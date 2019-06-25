# -*- coding: utf-8 -*-
# author zhangwudi
# time 2019-6-25 14:23:47

import requests
from lxml import etree


class BaiduSpider(object):
    def __init__(self):
        self.base_url = "http://www.shicimingju.com"
        self.url = "http://www.shicimingju.com/chaxun/zuozhe/1_{}.html"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
        }

    def get_url_list(self):
        # 18759700
        return [self.url.format(pn) for pn in range(1, 26)]

    def run(self):
        url_list = self.get_url_list()
        for url in url_list:
            # 请求数据获取 html 内容
            response = requests.get(url, headers=self.headers)
            html = response.content.decode('utf-8')
            eroot = etree.HTML(html)

            # 初步提取
            rows = eroot.xpath('/html/body/div[4]/div[2]/div[1]/div[1]/h3/a/@href')
            new_list = []
            for row in rows:
                new_row = self.base_url + row
                new_list.append(new_row)
            for i in new_list:
                response = requests.get(i, headers=self.headers)
                html2 = response.content.decode('utf-8')
                eroot2 = etree.HTML(html2)
                content = eroot2.xpath('//div[@class="shici-container www-shadow-card"]')
                for j in content:
                    title = j.xpath('.//h1[@class="shici-title"]/text()')
                    author = j.xpath('.//div[@class="shici-info"]/a/text()')
                    text = j.xpath('.//div[@class="shici-content"]/text()')
                    f = open("libai.txt", "a", encoding="utf-8")
                    for k in title:
                        print(k)
                        f.write(k.replace(' ', ''))
                    # for x in author:
                    #     f.write("——")
                    #     f.write(x.replace(' ', ''))
                    for z in text:
                        f.write(z.replace(' ', ''))
                    f.close()


if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()