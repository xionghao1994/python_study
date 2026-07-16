"""
深拷贝和浅拷贝
 格式：
  import copy
  # 浅拷贝
  copy(obj)
  # 深拷贝
  deepcopy(obj)
"""

# 三种浅拷贝写法（效果完全一致）
import copy
stu1 = [{"name":"李白"}, 100]

# 方式1 copy模块
stu2 = copy.copy(stu1)
# 方式2 列表切片
stu2 = stu1[:]
# 方式3 list转换
stu2 = list(stu1)

# 三、深拷贝 copy.deepcopy () （完全独立，所有层级全部复制）

