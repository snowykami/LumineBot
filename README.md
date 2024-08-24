<h1 align="center"><i>✨ LumineBot ✨ </i></h1>

<h3 align="center">基于 liteyukibot 的 聊天机器人 应用程式</h3>

## 简介

https://bot.liteyuki.icu

## 💿 安装

请使用 git 进行版本控制
把仓库clone到本地

    git clone https://github.com/snowykami/LumineBot


## 使用
### 安装依赖
- 0.先进入项目目录
```shell
cd LumineBot
```

- 1.创建虚拟环境
```shell
python venv .venv
```
- 2.激活虚拟环境
```shell
source .venv/bin/activate # on linux
.venv\Scripts\activate # on windows
```
- 3.安装pdm包管理器
```shell
pip install pdm
```
- 4.安装依赖
```shell
pdm install
```

### 运行
请先激活虚拟环境，同上

```shell
python main.py
```

### 更新
```shell
git pull
pdm install
```