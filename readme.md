# 一个 tsdemo项目 和 python 自动化测试项目

## 全局

使用vscode liveserver 插件模拟数据

## ts 项目

1. 安装`tsc`
2. 运行 `tsc --init` 生成 ts 项目
3. 打开 vscode 监视模式 Terminal -> run build task -> tsc:watch 每次更改会编译
4. 新建 `index.ts`, `index.html` 
5. `index.html` 引用 `index.js`

## python 测试

使用 pytest 测试

1. 安装 `pip install pytest`
2. 创建文件 `test_xx.py` 
3. 创建测试函数 `def test_xxx():xxx` 使用 `assert 语句来`
4. 使用unittest