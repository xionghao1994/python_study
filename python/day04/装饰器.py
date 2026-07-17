# 装饰器

# 无参无返回值装饰器
def print_info(fn_name):
  def inner():
    print('登录')
    fn_name()
  return inner

@print_info
def login():
  print('登录成功')

# 有参无返回值装饰器
def prin_info(fn_name):
  def inner(a,b):
    print('登录')
    fn_name(a,b)
  return inner

@print_info
def get_sum(a,b):
    sum = a + b
    print(f'求和的结果是{sum}')

# 有参有返回值装饰器
def print_info(fn_name):
  def inner():
     sum = fn_name()
     return sum
  return inner

@print_info
def get_sum():
    sum = 10 + 20
    return sum

# 有参有返回值
def print_info(fn_name):
   def inner(a,b):
      sum = fn_name(a,b)
      return sum
   return inner

@print_info
def get_sum(a,b):
   sum = a + b
   return sum

# 装饰器-可变参数
def print_info(fn_name):
    def inner(*args, **kwargs):
       sum = fn_name(*args, **kwargs)
       return sum
    return inner

@print_info
def get_sum(*args, **kwargs):
   # 定义求和变量
   sum = 0
   # 求所有位置参数的和，即：*args -> 元组
   for i in args:
       sum += i
   # 求所有的关键字参数的和，即：**kwargs -> 字典
   for i in kwargs.values():
       sum += i
   # 返回求和结果
   return sum

# 需求: 定义1个技能装饰 减法运算, 又能装饰加法运算的装饰器, 请用所学, 实现该需求.
def print_info(fn_name):
    def inner(a,b):
      if fn_name.__name__ == '+':
        print('加法运算')
      elif fn_name.__name__ == '-':
        print('减法运算')
      fn_name(a,b)
    return inner

@print_info('+')
def add(a, b):
   result = a + b
   print(f'加法运算的结果是{result}')

@print_info('-')
def sub(a, b):
   result = a - b
   print(f'减法运算的结果是{result}')



if __name__ == '__main__':
#   login()
#    get_sum(1,2)
    # get_sum()

    # get_sum(10, 20)

    # get_sum(10, 20, 30, a=100, b=200, c=300)

    # add(10, 20)
    # sub(10, 20)
