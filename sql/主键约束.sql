# 主键约束
/**
  概念：约束就是在数据类型的基础上，对某列值进一步限定
  目的：保证数据的完整性和安全性

  分类：
     1、单表约束
        主键约束（primary key），一般结合自增 auto_increment 一起使用，缺点：非空，唯一，一般是数字时
        非空约束（not null）
        唯一约束（unique）
        默认约束（default）

     2、多表约束
        外键约束（foreign key）
 */

-- 先切库
/**
   创建用 IF NOT EXISTS：存在才建
   删除用 IF EXISTS：存在才删
 */

-- ---------创建，切库，查表---------------------
-- 如果存在day03就删除day03数据库
drop database if exists day03;

-- 创建day03数据库
create database day03;

-- 切库，切到day03
use day03;

-- 查看day03里面所有的表
show tables;

-- ----------创建学生表，字段（id, name, gender, age）------------------------------
-- 创建学生表
create table student_info(
    id int primary key auto_increment,
    name varchar(10),
    gender varchar(10),
    age int
);

-- 新增学生表数据(多条)
insert into student_info values
     (1, '剑神', '女', 30 ),
     (2, '剑豪', '男', 40),
     (3, '亚瑟', '女', 50);

-- 新增单条学生数据
insert into student_info values (null, '李四', '男', 60);

-- 加了主键约束，写null会自增，不用手动添加
insert into student_info values (null, '王五', '男', 70);


-- 修改学生表数据
desc student_info;

-- 删除学生表数据

delete from student_info where gender='男';

truncate table student_info;# 暴力直接把原表数据清空了

-- 查看表数据
select * from student_info;


/**
  重点：
   扩展-delete from 和 truncate table的区别
   delete from 只删除表数据，不会重置主键ID
   truncate table 相当于把表摧毁了，然后创建一张和原来的一张一模一样的新表，会重置主键ID
   delete from 属于DML语句，可以结合事务一起使用
   truncate table 属于DDL语句
 */

 # -------------约束详解：掌握所有常用表的约束(主键，非空，唯一，默认)------------------------------------

-- 创建表
drop database if exists day04; # 每次先删除这个表在创建

-- 创建表
create database day04;

-- 使用表
use day04;

-- 查看下表
show tables;

-- 建表， teacher(老师表), 字段(id, 主键约束，name 非空， phone 唯一约束， address 默认 北京)
create table teacher(
    id int primary key auto_increment,
    name varchar(10) not null,
    phone varchar(11) unique,
    address varchar(100) default '北京' # 默认北京
);

desc teacher;

-- 添加数据
insert into teacher values(null, '小林', 16619941730, '北京');

insert into teacher values(null, '李四', '18736019320', '天津');

insert into teacher(name) values('熊浩');

-- 查询数据
select * from teacher;


-- ------扩展： 备份表数据--------------------------------
-- 备份只会备份表数据，列名，数据类型，不会备份约束比如主键约束和非空约束

show tables;
-- 备份表，不存在
-- 格式：create table 表名 select * from 原表名 where 条件...;

create table teacherNew select * from teacher;

-- 备份表，存在

-- 查看备份表的数据
select * from teacherNew;

-- 根据紧急情况下的”数据恢复“

-- 清空备份表数据
truncate table teacherNew;

-- 查看数据表的约束
desc teacher;
desc teacherNew;










