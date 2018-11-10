# 知乎专栏文章转png（政府性文章需登录）

从个人专栏获取文章列表，从列表中依次访问，获取封面，标题，以及文章内容的节点，
从全屏截图中找到节点的相当位置，拼接形成一张新的png，并以标题+文章ID命名，
保存在data中，后续可扩展，将png转化为PDF

## 运行环境

```
需使用 PhantomJS 浏览器
```

## 运行

```
python3 run.py
```

## 运行效果

```
共 38 篇文章
第 1 页
loading...
1 https://zhuanlan.zhihu.com/p/48042598
2 https://zhuanlan.zhihu.com/p/47097844
3 https://zhuanlan.zhihu.com/p/45079806
4 https://zhuanlan.zhihu.com/p/44965611
5 https://zhuanlan.zhihu.com/p/44534091
6 https://zhuanlan.zhihu.com/p/41640891
7 https://zhuanlan.zhihu.com/p/41472568
8 https://zhuanlan.zhihu.com/p/41056983
9 https://zhuanlan.zhihu.com/p/40450603
10 https://zhuanlan.zhihu.com/p/39615278
11 https://zhuanlan.zhihu.com/p/37407925
12 https://zhuanlan.zhihu.com/p/36492770
13 https://zhuanlan.zhihu.com/p/36367015
14 https://zhuanlan.zhihu.com/p/36260526
15 https://zhuanlan.zhihu.com/p/35558078
16 https://zhuanlan.zhihu.com/p/35442601
17 https://zhuanlan.zhihu.com/p/35223943
18 https://zhuanlan.zhihu.com/p/35188979
19 https://zhuanlan.zhihu.com/p/35171401
20 https://zhuanlan.zhihu.com/p/35145809
第 2 页
loading...
1 https://zhuanlan.zhihu.com/p/34698486
2 https://zhuanlan.zhihu.com/p/34493111
3 https://zhuanlan.zhihu.com/p/34378400
4 https://zhuanlan.zhihu.com/p/34196021
5 https://zhuanlan.zhihu.com/p/32372545
6 https://zhuanlan.zhihu.com/p/31652439
7 https://zhuanlan.zhihu.com/p/31384219
8 https://zhuanlan.zhihu.com/p/31326870
9 https://zhuanlan.zhihu.com/p/31296630
10 https://zhuanlan.zhihu.com/p/30985374
11 https://zhuanlan.zhihu.com/p/30378994
12 https://zhuanlan.zhihu.com/p/30308774
13 https://zhuanlan.zhihu.com/p/30212890
14 https://zhuanlan.zhihu.com/p/30101801
15 https://zhuanlan.zhihu.com/p/29779702
16 https://zhuanlan.zhihu.com/p/29246652
17 https://zhuanlan.zhihu.com/p/28871055
18 https://zhuanlan.zhihu.com/p/28749577
文章已搜索完毕
文章已搜索完毕
共 38 篇文章
文件名为 POINT.小数点数据分析特训营（北京场）正式开营48042598.png
获取到封面
获取到标题
获取到文章
POINT.小数点数据分析特训营（北京场）正式开营48042598.png已生成
还剩37篇文章
文件名为 你要成为小数点社区的第一批用户了47097844.png
获取到封面
获取到标题
获取到文章
你要成为小数点社区的第一批用户了47097844.png已生成
...
```

