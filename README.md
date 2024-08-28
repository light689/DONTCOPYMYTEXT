# 字体转换工具 (FONT_CONVERT.PY)

## 简介
`font_convert.py` 是一个用于转换字体的 Python 脚本。它使用 `fontTools` 库来加载和修改字体文件，通过替换字符映射表中的字符来生成新的字体文件。

## 功能
- 加载输入字体文件。
- 访问并修改字符映射表 (cmap)。
- 根据自定义逻辑替换字符。
- 保存修改后的字体文件。

## 使用方法
1. 安装 `fontTools` 库：
    ```bash
    pip install fonttools
    ```
2. 将 `font_convert.py` 脚本放置在合适的位置。
3. 运行脚本（请提前准备好input.otf）：
    ```bash
    python font_convert.py
    ```

## 注意事项
- 确保输入文件是有效的字体文件。
- 输出文件将覆盖同名文件，请谨慎操作。

## 依赖
- `fontTools` 库

## 作者
- lightworld689

## 许可证
- AGPL 3.0
