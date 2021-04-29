# lit-xsscjd-ace

洛阳理工学院 "学生手册知识竞答" 小助手...

>  这里是 `github actions` 版本

[![QQ Group](https://img.shields.io/badge/QQ%20Group-647027400-red.svg)](https://jq.qq.com/?_wv=1027&k=lz0XyN86)
[![TG Group](https://img.shields.io/badge/TG%20Group-lit_edu-blue.svg)](https://t.me/lit_edu)


## 使用

### 准备

- python3
- requests

### 配置

添加以下 `repository secret`

```
LIT_USERNAME
LIT_PASSWORD
```

默认随机完成用时, 每天8点自动添加一次答题记录, 或者点一下 `star` 也会添加一次

如需自定义请手动编辑 `ci.yaml`

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
