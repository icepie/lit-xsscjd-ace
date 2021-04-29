# lit-xsscjd-ace

洛阳理工学院 "学生手册知识竞答" 小助手...

> 某天一气之下做了这玩意...

[![The CI Test](https://github.com/icepie/lit-xsscjd-ace/actions/workflows/ci.yaml/badge.svg)](https://github.com/icepie/lit-xsscjd-ace/actions/workflows/ci.yaml)
[![QQ Group](https://img.shields.io/badge/QQ%20Group-647027400-red.svg)](https://jq.qq.com/?_wv=1027&k=lz0XyN86)
[![TG Group](https://img.shields.io/badge/TG%20Group-lit_edu-blue.svg)](https://t.me/lit_edu)


## 使用

### 准备

- python3
- requests

### 配置

> 当然你也可以选择直接运行

打开 `main.py` 编辑以下字段并保存
```python
CONFIG = {
    'username': 'B19000000', # 帐号
    'password': '123456', # 密码
    'dotime': 256, # 完成用时 (秒), 建议三十分钟以内
    'score': 99 # 想达到多少分以上?
}
```

### 运行

```bash
$ python3 main.py
```

接下来不用多说了吧?

## 其他

- 无需题库

- 无视三次的限制

- 每次运行就是添加一次答题记录...即使你中止程序也会记录为最后的分数

- 随机试卷会被缓存下来(位置在`obj`文件夹下)...里面有配置可以自己发挥

- 哦对了...用本程序商用盈利者没🐎..

没别的了...写的很烂不喜勿喷
