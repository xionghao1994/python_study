"""
    描述：
    os 是 Python内置标准库，不是第三方包，无需额外安装，直接 import os 即可使用；
    作用：跨操作系统操作目录、文件、系统路径，兼容 Windows/macOS/Linux；
    调用格式：os.函数名()
"""

"""
    函数功能	关键注意点
    os.getcwd()	获取当前工作目录	所有相对路径的基准路径
    os.chdir(path)	切换工作目录	切换后相对路径参考位置同步改变
    os.mkdir(path)	创建单个文件夹	文件夹已存在会直接报错
    os.rmdir(path)	删除文件夹	只能删空文件夹，有文件会报错
    os.rename(old, new)	文件 / 文件夹重命名	支持移动文件到同盘其他目录
    os.listdir(path)	列出目录一级内容	只返回当前层文件 / 文件夹名，不递归子目录
"""

"""
    关键知识点补充（踩坑提醒）
    os 是内置库：不用pip install，直接 import；
    mkdir仅创建单级目录，多级文件夹要用os.makedirs()；
    rmdir硬性限制：仅能删除完全空白文件夹，包含文件 / 子文件夹会报错；
    chdir切换目录后，所有相对路径都会以新目录为准，操作完建议切回原目录；
    listdir仅返回名称字符串，不会区分是文件还是文件夹，如需判断类型需要搭配os.path。
"""

# 导入os 内置模块
import os

# 1. getcwd() 获取当前工作目录
current_path = os.getcwd()
print('获取当前工作目录', current_path)

# 2. mkdir() 创建文件夹 
try:
    os.mkdir('test')
    print('创建文件夹成功')
except FileExistsError:
    print('文件夹已存在，创建失败')

# 3. listdir() 列出目录下所有一级内容 
dir_list = os.listdir(current_path)
print('列出当前目录下所有一级内容', dir_list)

# 4. chdir() 切换工作目录 
os.chdir("test_dir")
print('切换工作目录到', os.getcwd())

#  在新目录创建子文件夹
os.mkdir("inner_folder")

# 切回原始目录
os.chdir(current_path)
print("切回原始工作目录：", os.getcwd())


# 5. rename() 重命名文件夹
# 重命名 test_dir/inner_folder → test_dir/new_inner
os.rename("test_dir/inner_folder", "test_dir/new_inner")
print("文件夹重命名完成")

# 6. rmdir() 删除空文件夹
# 先删除内层空文件夹
os.rmdir("test_dir/new_inner")
print("空文件夹 new_inner 删除成功")
# 此时test_dir内部为空，可以删除
os.rmdir("test_dir")
print("空文件夹 test_dir 删除成功")

# 拓展演示：rmdir无法删除非空文件夹（取消注释测试报错）
# os.mkdir("temp")
# with open("temp/test.txt", "w") as f:
#     f.write("测试文件")
# os.rmdir("temp") # 文件夹内有文件，执行直接报错

