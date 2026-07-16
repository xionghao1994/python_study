"""
  操作文件的步骤：
    1.打开文件
    2.读写文件
    3.释放资源

 扩展： with open语句，它会在内容执行完毕后，自动释放资源，无需我们
 再次手动close了
 格式：
   with open(....) as 变量名：
    逻辑代码
 特点：
   逻辑代码执行完毕后，会自动释放with后边定义的变量对象
"""

# 需求：往文件1.txt中写入一句话
# 1.打开文件
dest_file = open('./1.txt', 'w', encoding="utf-8")
# 2.读写数据
dest_file.write('好好学习，天天向上')
# 3.释放资源
dest_file.close()

# with open写法（推荐方式）
with open ('./1.txt', 'w', encoding="utf-8") as dest_file:
    dest_file.write('高阶python阶段了，要继续努力！')

# 读写文件
# with open ('./1.txt', 'w', encoding="utf-8") as dest_file,open ('./1.txt', 'r', encoding="utf-8") as src_file:
#     dest_file.write('高阶python阶段了，要继续努力！')