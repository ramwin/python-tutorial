** Xiang Wang @ 2016-05-26 15:30:51 **

# Menu
* [Official Document](https://docs.python.org/3/library/re.html#module-re)
* [test regrex](https://regex101.com/#python)

# 基础知识
* 匹配规则
    * `\d`  *数字*
    * `\D`  *非数字*
    * `\s`  *空白字符*
    * `\S`  *非空白字符*
    * `\w`  *单词字符*
    * `\W`  *非单词字符*
    * `(a|bc|d)  *a或者bc或者c*
    * `[a-z]` * 小写字母

* 方法
    re.compile(r'(?P<id>\d+)we').match('123we').group('id')
    re.sub(r'(00)*$', '', '100000')  # 把匹配到的数据变成空

# 例子
* 找到字符串里面符合规则的字符串
```
    a = re.compile(r'^数据更新时间：(?P<time>[0-9: -]*)').match('数据更新时间：2016-05-25 16:00:00')
    print(a.groupdict())
```

* 把字符串里面符合规则的字符进行替换
```
    re.splite(r'\.0*', text)
```


* 删除字符串里面符合规则的字符串

5. # [Regular Expression Examples](https://docs.python.org/3/library/re.html#regular-expression-examples)
    5. ## [Text Munging](https://docs.python.org/3/library/re.html#text-munging)
    ```
    >>> def repl(m):
    ...     inner_word = list(m.group(2))
    ...     random.shuffle(inner_word)
    ...     return m.group(1) + "".join(inner_word) + m.group(3)
    >>> text = "Professor Abdolmalek, please report your absences promptly."
    >>> re.sub(r"(\w)(\w+)(\w)", repl, text)
    'Poefsrosr Aealmlobdk, pslaee reorpt your abnseces plmrptoy.'
    >>> re.sub(r"(\w)(\w+)(\w)", repl, text)
    'Pofsroser Aodlambelk, plasee reoprt yuor asnebces potlmrpy.'
    ```