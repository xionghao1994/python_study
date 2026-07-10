/**
  多表查询（实际开发用的最多-重点）
  基本格式： select * from 表A,表B;(实际开发不用，会产生大量的脏数据)
 */

 -- 切库
USE day05;

-- 交叉查询(没人用)
select * from product, productgood;

-- 连接查询
# 内连接（常用）

-- 显式格式 select * from A join B on 关联条件 where
-- inner关键字可以省略，简写为join
-- 关联条件必须使用on关键字指定

-- 隐式格式 select * from A,B where 关联条件
-- 通过where子句指定关联条件
-- 实际开发中更常用显式写法

# 外连接

-- 左外连接(高频) left join
-- 描述：以左边表全部数据为主，右表匹配不到填充 null
-- 适用：查所有商品，哪怕商品没有分类也要展示出来

-- 右连接 right join （极少用，基本都可以用左连接完全替代）
-- 以右边表全部数据为主，左表匹配不到填充 null


/**
   多表查询 1 vs 多
 */

# 多表约束详解
# 概述
# 它是用来描述多表关系的，一般在外表（从表）中做限定。
# 格式
# 场景 1：建表时创建
# [constraint 外键约束名] foreign key(外键列名) references 主表名(主键列名)
# 场景 2：建表后创建
# alter table 表名 add [constraint 外键约束名] foreign key(外键列名) references 主表名(主键列名);
# 场景 3：删除外键约束
# alter table 表名 drop foreign key 外键约束名;


-- 1、建库，切库，查表
drop database if exists test01; # 如果有这个库就删除-防止重复

create database if not exists test01; # 创建数据库

use test01; # 使用数据库

show tables; # 查表

-- 2、建表，部门表
create table dept(
   id int primary key auto_increment,
   name varchar(20)
);

-- 3、建表，员工表，先不加约束，我们插入数据看看
create  table employee(
    id int primary key auto_increment,
    name varchar(20),
    salary int,
    dept_id int,
    constraint fk_dept_em foreign key(dept_id) references dept(id) # fk = foreign key 关连dept employee
);

-- 4、添加数据 主键
insert into dept values
(null, '人事部'),
(null, '财务部'),
(null, '研发部');

-- 外键表
insert into employee values
                     (null, '小刚', 1800, 1),
                     (null, '小李', 1200, 2),
                     (null, '小熊', 13000, 3);

# 外表的外键必须在主表里面的主建里有这个

-- 手动删除 外键约束，观察表的关系，
alter table employee drop foreign key fk_dept_em;

-- 重新添加外键约束，会失败，因为有脏数据 掌握
alter table employee add foreign key(dept_id) references dept(id);


select * from dept;
select * from employee;













