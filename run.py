# -*- coding:utf-8 -*-

from get_article_urls import get_article_urls
from image_get import get_article_png


if __name__ == '__main__':
    urls_list = get_article_urls('https://www.zhihu.com/people/jiafeimao/posts').get_urls()  #专栏文章主页
    #print(urls_list)
    i = len(urls_list)
    for url in urls_list:
        get_article_png(url).run()
        i = i - 1
print('还剩' + str(i) + '篇文章')
