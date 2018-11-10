# -*- coding:utf-8 -*-
import os
import re
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
from PIL import Image


class get_article_png(object):
    def __init__(self, url):
        caps = DesiredCapabilities.PHANTOMJS
        caps[
            "phantomjs.page.settings.userAgent"] =  'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
        self.browser = webdriver.PhantomJS(desired_capabilities=caps)
        self.browser.set_window_size(2400, 3000)
        self.wait = WebDriverWait(self.browser, 20)
        self.url = url
        self.answer_pic_num = 1
        self.page_num = 0

    def open(self):
        self.browser.get(self.url)
        basic_title = re.sub('https://zhuanlan.zhihu.com/p/', '', self.url, re.S)
        try:
            t = self.browser.find_element_by_xpath('//*[@id="root"]/div/main/div/article/header/h1').text
            self.title = t + basic_title
            print('文件名为', self.title + '.png')
        except NoSuchElementException:
            # print('未找到标题，文件名设为' + basic_title + '.png')
            self.title = basic_title
        self.scroll_page(10)

    def scroll_page(self, num):
        i = 0
        while i < num:
            self.browser.execute_script("window.scrollBy(0,3000)")
            time.sleep(2)
            i += 1

    def get_screenshot(self):
        screen = self.browser.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screen))
        return screenshot

    def pic_rangle(self, item):
        locations = item.location
        sizes = item.size
        rangle = (int(locations['x']), int(locations['y']), int(locations['x'] + sizes['width']),
                    int(locations['y'] + sizes['height']))
        return rangle

    def get_cover_pic(self):
        try:
            cover = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/img')))
            self.get_screenshot().crop(self.pic_rangle(cover)).save("./log/cover.png")
            print('获取到封面')
        except Exception:
            print('未找到封面')

    def get_header_pic(self):
        try:
            header = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/article/header')))
            self.get_screenshot().crop(self.pic_rangle(header)).save("./log/header.png")
            print('获取到标题')
        except Exception:
            print('未找到标题')

    def get_article_pic(self):
        try:
            article = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/main/div/article/div[1]')))
            self.get_screenshot().crop(self.pic_rangle(article)).save("./log/article.png")
            print('获取到文章')
        except Exception:
            print('未找到文章内容')

    def fix_img(self, img1, img2, img3):
        try:
            img1 = Image.open(img1)
            img2 = Image.open(img2)
            height = img1.height + img2.height
            width = img1.width
            target = Image.new('RGB', (width, height))
            target.paste(img1, (0, 0))
            target.paste(img2, (0, img1.height, width, img1.height + img2.height))
            target.save(img3)
            return True
        except FileNotFoundError:
            print('图片文件未找到')
            return False

    def fix_article(self):
        cover = './log/cover.png'
        header = './log/header.png'
        article = './log/article.png'
        if self.fix_img(cover, header, './data/' + self.title + '.png'):
            self.fix_img('./data/' + self.title + '.png', article,  './data/' + self.title + '.png')
            print(self.title + '.png' + "已生成")
        else:
            if self.fix_img(header, article, './data/' + self.title + '.png'):
                print("未找到封面，" + self.title + '.png' + "已生成")
            else:
                print('该专栏需登录：https://zhuanlan.zhihu.com/p/' + self.title)

    def run(self):
        self.open()
        self.get_cover_pic()
        self.get_header_pic()
        self.get_article_pic()
        self.fix_article()
        try:
            os.remove('./log/cover.png')
        except FileNotFoundError:
            print('删除cover时未找到文件')
        try:
            os.remove('./log/header.png')
        except FileNotFoundError:
            print('删除header时未找到文件')
        try:
            os.remove('./log/article.png')
        except FileNotFoundError:
            print('删除article时未找到文件')


if __name__ == '__main__':
get_article_png('https://zhuanlan.zhihu.com/p/36260526').run()
