#### Xiang Wang @ 2017-02-10 15:30:51

### 基础
* 参考资料
    * [官网教程](https://docs.python.org/3/)
    * [python tips](http://book.pythontips.com/en/latest/index.html)
* [字符串string](./string.md)
* [列表list](list.md)
    * [for else](http://book.pythontips.com/en/latest/for_-_else.html)
        ```
        for item in container:
            if search_something(item):
                process(item)
                break
        else:
            not_found_in_container()
        ```
* [集合set](set.md)
* [时间](time时间.md)
* enumerate
```
    enumerate(['a','b','c'])  // [(0, 'a'), (1, 'b'), (2, 'c')]  但是不是list， 而是一个enumerate对象
```
* [执行顺序](https://docs.python.org/3/reference/expressions.html#evaluation-order)
```
    ()  # 括号内
    **  # 指数
    +x, -x  # 负数
    in, not in, is, is not, <, <=, >, >=  # 比较
    not x  #
    and  #
    or  # and 和 or不是同样的哦。
```
* [Exception报错](./exception.md) [官网](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)
* [class](./class/README.md)
    * [property](./class/property.md) [示例](./class/property.py)


### 包参考
* [csv](./csv.md)
* [re正则表达式](./rematch正则表达式.md)
* [collections](./collections.md)
* [fractions](https://docs.python.org/2/library/fractions.html#fractions.Fraction)
```
    from fractions import Fraction
    f = Fraction(1,3)
    print("1/3 = %d/%d" % (f.numerator, f.denominator))
```
* [json](./json.md)

### 其他包
* [requests](./requests.md) *发送http请求*
* [click](./click.md) *用python写shell命令*
* [jinja模板渲染](./jinjia.md)
* [openpyxl](./openpyxl.md)
* [scrapy](./scrapy/README.md)
* [peewee](./peewee.md) *简单而轻量级的sqlite3 orm，和django很像*
* [mongoengine](./mongoengine.md) *把mongodb当作sql用。那你为什么不直接用mysql啊*
* [flask](./flask.md) *轻量级http服务器*
* [word2html](https://github.com/bradmontgomery/word2html)  *把word转化成html*
* [pillow](./Pillow.md)
* [qiniu](https://developer.qiniu.com/kodo/sdk/1242/python) *调用七牛的api上传文件*
* pyperclip *控制系统剪切板*
    pyperclip.copy('ew') # 把ew放入剪切板
* pip *快速安装包*
    pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==1.11
* [flake8] *检测python代码是不是满足pep8*
* [yapf] *把python的代码格式化*
* urllib
    urllib.parse.urlencode({'key': 'value%&'})
    >>> 'key=value%25%26'
    urllib.parse.quote('&')
    >>> '%26'
