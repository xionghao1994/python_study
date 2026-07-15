# 该文件是 学生管理系统文件，
# 主要完成:学生管理系统的 主要业务逻辑的。
import time;

from student import Student;

class StudentCms(object):
    def __init__(self):
        self.student_list = []  # 用来记录所有学生信息

    # 定义函数 show_view() 用来展示提示界面
    def show_view(self):
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
        self.mobile = input('请录入要添加的学生联系方式：')
        self.des = input('请录入要添加的学生描述：')
        # 把上述封装好的学生对象，添加到学生列表中
        stu = Student(self.name, self.gender, self.mobile, self.des)
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
                stu.mobile = input('请输入修改后的学生联系方式：')
                stu.des = input('请输入修改后的学生描述：')

                # 核心细节，修改后记得 break
                break
        else:
            print('没有此学生信息，请重新输入！')


    # 定义函数 del_student() 表示删除学生
    def del_student(self):
        pass
    
    # 定义函数 search_one_student() 表示查询单个学生
    def search_one_student(self):
        pass

    # 定义函数 search_all_student() 表示查询所有学生
    def search_all_student(self):
        if len(self.student_list) > 0 :
            for stu in self.student_list:
                print(stu)
                print('-----------------')
        else:
            print('目前没有学生信息,添加后查询')

    # 定义函数 save_student() 表示保存信息 到文件中
    def save_student(self):
        pass

    # 定义函数 load_student() 表示从文件中 加载学生信息到student_list列表中
    def load_student(self):
        pass

    # 定义函数start() 表示程序的入口，在这里完成具体逻辑
    def start(self):
        # self.load_student()

        while True:
            # time.sleep(1) # 为了效果明显，模拟系统自动等待，加入休眠线程
            self.show_view() # 打印选择功能界面

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
                self.save_student()
                # print('保存信息')
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