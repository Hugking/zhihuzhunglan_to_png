# -*- coding:utf-8 -*-
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver


class get_article_urls(object):
    def __init__(self, url):
        self.basic_url = url
        self.doc_urls = []
        caps = DesiredCapabilities.PHANTOMJS
        caps[
            "phantomjs.page.settings.userAgent"] = \
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) ' \
            'Chrome/57.0.2987.133 Safari/537.36'
        self.broswer = webdriver.PhantomJS(desired_capabilities=caps)
        self.broswer.set_window_size(1400, 500)

    def get_urls(self):
        self.broswer.get(self.basic_url)
        doc_num = self.broswer.find_element_by_xpath('//*[@id="ProfileMain"]/div[1]/ul/li[4]/a/span').text
        print("共", doc_num, "篇文章")
        doc_num = int((int(doc_num) - (int(doc_num) % 20))/20 + 1)
        # print(doc_num)
        for i in range(1, doc_num+1):
            zhuanlan_url = self.basic_url + '?page=' + str(i)
            time.sleep(2)
            print('第', i, '页')
            self.broswer.get(zhuanlan_url)
            tim = 0
            print('loading...')
            while tim < 10:  # 当文章数量多时，把10变大一些
                self.broswer.execute_script("window.scrollBy(0,5000)")
                time.sleep(2)
                tim += 1
            for j in range(1, 21):
                try:
                    doc_url = self.broswer.find_element_by_xpath('//*[@id="Profile-posts"]/div[2]/div[' + str(j) +
                                                                 ']/div/h2/a').get_attribute('href')
                    print(j, doc_url)
                    self.doc_urls.append(doc_url)
                except NoSuchElementException:
                    print('文章已搜索完毕')
        print('共', len(self.doc_urls), '篇文章')
        self.broswer.close()
        return self.doc_urls


if __name__ == '__main__':
    urls_list = get_article_urls('https://www.zhihu.com/people/jiafeimao/posts').get_urls()
    print(urls_list)
