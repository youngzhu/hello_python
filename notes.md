# 1. 命名规范
Python中推荐“小写字母+_”的方式命名变量或文件。

大写字母另有用处？
首字母大写表示类（class）。

# 2. 创建虚拟环境
```bash
python -m venv xx-env
source myenv/bin/activate  # Linux/macOS
myenv\Scripts\activate     # Windows
```

- 适用于纯 Python 项目，轻量级
- 适用于需要管理多种语言依赖的项目。如科学计算、数据科学等领域，因为这些领域通常需要复杂的依赖关系。
