# Home

这是一个由浙江大学计算机科学与技术学院学生会为服务全体计算机学院同学所搭建的网页，从[这里](https://zju-cssu-dev.github.io/home/)访问主页。

# 本地构建指南

0. 安装必要工具  
   - **git**：用于克隆仓库  
   - **uv**：用于创建虚拟环境、安装依赖（[安装 uv](https://docs.astral.sh/uv/getting-started/installation/)）。uv 会自动管理 Python，无需单独安装。

1. 将 repo 克隆到本地

```shell
# 使用 HTTPS 协议
git clone https://github.com/ZJU-CSSU-Dev/home.git
# 或使用 SSH 协议
git clone git@github.com:ZJU-CSSU-Dev/home.git
```

2. 进入项目目录，用 uv 创建虚拟环境并安装依赖（含 `mkdocs`、`mkdocs-material` 及第三方插件）

```shell
cd home
uv venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
uv pip install -r requirements.txt
```

3. 启动 MkDocs 本地服务

```shell
# 若已激活虚拟环境，直接执行：
mkdocs serve

# 未激活时也可用（uv 会自动使用项目虚拟环境 cssu）：
uv run mkdocs serve
```

   在浏览器打开 **http://127.0.0.1:8000** 即可预览网站。




