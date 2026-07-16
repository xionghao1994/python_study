# 该文件是 学生管理系统文件，
# 主要完成:学生管理系统的 主要业务逻辑的。
import time;

from student import Student;

class StudentCms(object):
    def __init__(self):
        self.student_list = []  # 用来记录所有学生信息

    # 定义函数 show_view() 用来展示提示界面
    @staticmethod    # 没有self 做输出可以做静态方法
    def show_view():
        print('*' * 20)
        print('欢迎来到学生管理系统界面')
        print('1.添加学生')
        print('2.修改学生')
        print('3.删除学生')
        print('4.查询所有学生')
        print('5.查询单个学生')
        print('6.保存信息')
        print('7.退出系统')
        print('*' * 20)

    # 定义函数 add_student() 表示添加学生
    def add_student(self):
        # 提示用户录入学生信息，并接收
        self.name = input('请录入要添加的学生姓名：')
        self.gender = input('请录入要添加的学生性别：')
        self.age = input('请录入要添加的学生年龄：')
        self.mobile = input('请录入要添加的学生联系方式：')
        self.des = input('请录入要添加的学生描述：')
        # 把上述封装好的学生对象，添加到学生列表中
        stu = Student(self.name, self.gender, self.age, self.mobile, self.des)
        self.student_list.append(stu)
        # 打印提示信息即可
        print(f'添加学生成功')

    # 定义函数 update_student() 表示修改学生
    def update_student(self):
        # 提示用户录入要修改的学生姓名
        # 遍历学生列表，获取每个学生信息
        # 判断当前学生姓名是否和要修改的学生姓名一致
        update_name = input('请输入要修改的学生姓名：')

        for stu in self.student_list:
            if stu.name == update_name:
                # 提示用户输入修改后的信息
                stu.name = input('请输入修改后的学生姓名：')
                stu.gender = input('请输入修改后的学生性别：')
                stu.age = input('请输入修改后的学生年龄：')
                stu.mobile = input('请输入修改后的学生联系方式：')
                stu.des = input('请输入修改后的学生描述：')

                # 核心细节，修改后记得 break
                break
        else:
            print('没有此学生信息，请重新输入！')


    # 定义函数 del_student() 表示删除学生
    def del_student(self):
        del_name = input('请输入要删除的学生姓名：')
        if len(self.student_list):
            for stu in self.student_list:
                if stu.name == del_name:
                    self.student_list.remove(stu)
                    print('删除成功')
        else:
            print('目前没有学生信息，请添加后删除')
    
    # 定义函数 search_one_student() 表示查询单个学生
    def search_one_student(self):
        search_name = input('请输入要查询的学生姓名:')
        if len(self.student_list):
            for stu in self.student_list:
                if stu.name == search_name:
                    print(stu)
                    break
            else:
                print('没有此学生，请重新输入')
        else:
            print('目前还没有学生信息，请添加后查询')

    # 定义函数 search_all_student() 表示查询所有学生
    def search_all_student(self):
        if len(self.student_list):
            for stu in self.student_list:
                print(stu)
                print('-----------------')
        else:
            print('目前没有学生信息,添加后查询')

    # 定义函数 save_student() 表示保存信息 到文件中
    def save_student(self):

        # 拆分版本
        student_dic = [stu.__dict__ for stu in self.student_list]
        # with open('./student.txt', 'w', encoding="utf-8")
        # 把上述的列表嵌套字典，转换乘字符串形式
        # student_data = str(student_dic)

        # 合并版本
        student_data = str([stu.__dict__ for stu in self.student_list])

        # 把上述的字符串(学生信息)写到目的地文件中
        with open('./studentData.txt', 'w', encoding="utf-8") as dest_file:
            dest_file.write(student_data)
            print('保存学生信息成功 \n')
            print('*' * 20)


    # 定义函数 load_student() 表示从文件中 加载学生信息到student_list列表中
    def load_student(self):
        try:
            with open('./studentData.txt', 'r', encoding="utf-8") as src_file:
                student_data = src_file.read() # 一次性读取整个文件的全部内容，返回一整段字符串

                if len(student_data) <= 0:
                    student_data = '[]'

                # eval()去掉两端的引号，是啥就是啥
                # list 转换成列表实例
                list_data = eval(student_data)
                self.student_list = [
                    Student(
                        stu_dict['name'],
                        stu_dict['gender'],
                        stu_dict['age'],
                        stu_dict['mobile'],
                        stu_dict['des']
                    ) for stu_dict in list_data
                ]
                print(f'学生信息加载成功，共 {len(self.student_list)} 名学生:')
                for stu in self.student_list:
                    print(stu)
        except FileNotFoundError:
            with open('./studentData.txt', 'w', encoding="utf-8") as dest_file:
                pass
            self.student_list = []
            print('未找到学生数据文件，已创建新文件')

    # 定义函数start() 表示程序的入口，在这里完成具体逻辑
    def start(self):
        # 加载学生信息
        self.load_student()
        while True:
            # time.sleep(1) # 为了效果明显，模拟系统自动等待，加入休眠线程
            # self.show_view() # 打印选择功能界面
            StudentCms.show_view()

            input_num = int(input('请输入您要操作的编号：'))
            # 根据用户输入的编号，调用对应的功能
            if input_num == 1:
                self.add_student()
                # print('添加学生')
            elif input_num == 2:
                self.update_student()
                # print('修改学生')
            elif input_num == 3:
                self.del_student()
                # print('删除学生')
            elif input_num == 4:
                self.search_all_student()
                # print('查询所有学生')
            elif input_num == 5:
                self.search_one_student()
                # print('查询单个学生')
            elif input_num == 6:
                # print('保存信息')
                self.save_student()
                # 读取文件信息
            elif input_num == 7:

                # 询问用户是否要退出系统
                result = input('您确定要退出系统吗？y/n : \n')
                if result.lower() == 'y':
                    print('退出系统')
                    break
                elif result.lower == 'n':
                    print('取消退出')
                else:
                    print('输入有误，请重新输入！')

                # print('退出系统')
                # break
            else:
                print('输入有误，请重新输入！')


# 测试代码
if __name__ == '__main__':
    stu_cms = StudentCms()
    # 测试提示界面
    # stu_cms.show_view()
    # # 测试学生列表
    # print(f'目前有的学生信息：{stu_cms.student_list}')
    stu_cms.start()