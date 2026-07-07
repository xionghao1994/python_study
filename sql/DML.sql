-- DML语句: 数据操作语言，主要是对表数据进行增删改查
-- 关键字： insert(增), delete(删除), update(改), select(查)

-- 先查库
show databases;

-- 切库
use day02;

/**
  增
 1、 insert into 表名(列名1， 列名2) values (数据1， 数据2)
 2、 insert into 表名 values (数据1， 数据2)
  inset into 表名 values
            (值1，值2 ....)
            (值1，值2 ....)
            ...

 细节1： 添加表数据的时候，值的个数和类型要和列名保持一致
 细节2： 如果不写列名，则默认是全列名，即必须给所有的列依次进行赋值
 细节3: 如果是主键列且配合有自增，传值的时候，可以传入null,
 */

insert into base_info(id, name,gender, age) values (1, '张胜男', '女', 20);

insert into base_info values
    (1, '李四', '女', 30),
    (2, '王五', '男', 60),
    (3, '好六', '男', 30);


/**
  改
  格式： update 表名 set 字段名1=新值, 字段名2=新值 where 条件;
 */
 update base_info set id=11, age=300 where id=1;

-- 删除表
    -- 格式: delete from 表名 where 条件
#      truncate table 表名 (重点)
    delete from base_info where id=3;


-- 简单查询，所有表中的数据
select * from base_info;


