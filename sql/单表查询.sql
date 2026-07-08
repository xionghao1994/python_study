/**
  单表查询
  []是代表可选，实际写法不能写[]只写asc 或者 desc
 */

 # 1、排序查询
-- 格式： select * from 数据表名 order by 字段1 [asc | desc], 字段2 [asc | desc] ....
-- 排序规则
-- asc：升序（默认可省略）
-- desc：降序

# 使用价格排序（降序）
# select * from product order by price;  #不写默认升序
# select * from product order by price desc; # 降序


# 2、聚合查询
/**
  功能分类：
    ：统计表的总行数（总条数）
    ：最大值，仅对数字列有效
    ：最小值，仅对数字列有效
    ：求总和，仅对数字列有效
    ：平均值，仅对数字列有效
  面试题：count(*), count(1), count(列) 如果列里面没null,他们的条数是一样的
  count(列)如果里面有null,统计的条数就不是总条数
  执行效率： count(主键列)>count(1)>count(*)>count(普通列)
 */
-- count
# 基本语法：select count(*) from 表名;  统计表的总行数
# 推荐写法 select count(*) as 别名 from 表名;  统计表的总行数

-- max
# 基本语法：select max(列名) from 表名; 求某列最大值

-- min
# 基本语法：select min(列名) from 表名，求某列最小值

-- sum
# 基本语法：select sum(列名) from 表名，求某列总和

-- avg
# 基本语法：select avg(列名) from 表名，求某列平均值

-- round
# 基本语法：select round(数值, 小数位数);四舍五入保留指定位数
# 实际应用：
# 示例：select round(avg(price), 2) avg_price from product得到1346.38
# 单独测试：select round(3.12545, 2)结果为3.13

-- -------案例------------------------------

# 创建库
create database test;

# 切库
use test;

# 创建表
create table if not exists day01(
   id int primary key auto_increment,
   name varchar(100),
   idCard varchar(10) unique,
   price double
);

# 增加表字段
insert into day01 values
(null,'张三', '10001', 100),
(null,'张三', '10002', 100);
