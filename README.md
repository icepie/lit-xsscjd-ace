# lit-xsscjd-ace

洛阳理工学院 "学生手册手册知识竞答" 小助手...

> 某天一气之下做了这玩意...

[![QQ Group](https://img.shields.io/badge/QQ%20Group-647027400-red.svg)](https://jq.qq.com/?_wv=1027&k=lz0XyN86)
[![TG Group](https://img.shields.io/badge/TG%20Group-lit_edu-blue.svg)](https://t.me/lit_edu)


## 使用

### 准备

- python3
- requests

### 配置

打开 `main.py` 编辑以下字段并保存
```python
CONFIG = {
    'username': 'B19000000', # 帐号
    'password': '123456', # 密码
    'dotime': 256, #完成用时 (秒), 建议三十分钟以内
    'sroce': 99 #想达到多少分以上?
}
```

### 运行

```bash
$ python3 main.py
```

接下来不用多说了吧?

## 其他

- 无视三次的限制
- 随机试卷会呗缓存下来...里面有配置可以自己发挥

没别的了...写的很烂不喜勿喷
