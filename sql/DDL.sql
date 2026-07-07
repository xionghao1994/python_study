# 数据库基本操作

-- 上来要切库，不然会报错

-- 查看所有数据库
show databases;

-- 创建数据库
create database day03;

-- 创建数据库，手动指定 utf8mb4编码（推荐---重点掌握）
create database day04 charset utf8mb4;

-- 安全创建（库存在不报错，脚本标准写法）
create database if not exists day02 charset utf8mb4;

-- 查看单个数据库详情（字符集，排序规则）
show create database day02;

-- 修改数据库字符集
alter database day02 charset utf8mb4 collate utf8mb4_unicode_ci;

-- 删除数据库（谨慎，库内数据全部清空）
drop database if exists day01;

-- 切换/进入指定数据库（切库 推荐---重点掌握）
use day02;

-- 查询当前正使用的数据库
select database();



# 创建数据库: 使用CREATE DATABASE 数据库名语句
# 查看数据库: 使用SHOW DATABASES命令
# 删除数据库: 使用DROP DATABASE 数据库名语句
# 切换数据库: 使用USE 数据库名命令


/**
    创建数据表
    格式：[if not exists] 可写可不写
     create table [if not exists] 数据表名 (
       列名1 数据类型 [约束],
       列名1 数据类型 [约束],
       .....
     );
 */

-- 需求： 创建学生表 student, 字段（学生编号，姓名，非空约束，性别，年龄）
create table if not exists student_info (
    id int,
    name varchar(10) not null,
    gender varchar(2),
    age int(100)
);

-- 查看单个数据库的详情信息（码表）
show create table student_info;

-- 查看表的字段有哪些（重点要掌握）
desc student_info;

-- 修改数据表的（表名）
-- 格式： rename table 旧表名 to 新表名;
rename table student_info to base_info;

-- 删除指定表
drop table student_info;



# --------------- DDL ----------------------------------------

-- 查看表的所有列
desc table base_info;

-- 绘表，新增列，这个语句还有可能会用到， 理解即可
-- 格式： alter table 表名 add 列名 数据类型 [约束];  not null 是这个不能为空
alter table base_info add class varchar(10) not null;


-- 修改列，数据类型和约束
-- 格式： alter table 表名 modify 列名 数据类型[约束]
alter table base_info modify class int not null;


-- 修改列，列名，数据类型 和约束
-- 格式： alter table 表名 change 旧列名 新列名 数据类型[约束]
alter table base_info change class classNew int not null;



-- 删除指定的列
-- 格式: alter table 表名 drop 列
alter table base_info drop classNew;

