# ------建库，切库，查表------------
create database if not exists day05;

use day05;

show tables;

-- 建表
create table product
(
    id int primary key auto_increment,
    name varchar(10),
    price double,
    category_id varchar(32)
);

create table productGood
(
    id int primary key auto_increment,
    name varchar(10),
    price double,
    category_id varchar(32)
);

-- 添加表数据
insert into product values
(null, '张三1', 100,'0.01'),
(null, '张三2', 1010,'0.01'),
(null, '张三3', 1200,'0.01'),
(null, '张三4', 12020,'0.01'),
(null, '张三5', 100,'0.01'),
(null, '张三6', 1020,'0.01'),
(null, '张三7', 10230,'0.01'),
(null, '张三8', 300,'0.01'),
(null, '张三9', 1010,'0.01'),
(null, '张三10', 1200,'0.01');

insert into productGood values
(null, '李四', 100,'0.01'),
(null, '李四2', 1010,'0.01'),
(null, '李四', 1200,'0.01'),
(null, '李四', 12020,'0.01'),
(null, '李四5', 100,'0.01'),
(null, '李四6', 1020,'0.01'),
(null, '李四7', 10230,'0.01'),
(null, '李四', 300,'0.01'),
(null, '李四9', 1010,'0.01'),
(null, '李四10', 1200,'0.01');

-- 查询表
select * from product;

select * from productGood;

# 两种写法一样
select * from productGood where name='李四';
select * from productGood where name in ('李四');

-- 查询不是李四的人员
select * from productGood where name not in ('李四');

# 下面也可以用not in 写法
select * from productGood where price != 100;
select * from productGood where price >= 100;
select * from productGood where price <= 100;

# 查询价格100-1000之间的商品
select * from product where price between 100 and 1000;
# 等价于
select * from product where price >= 100 and price <= 800;

# 查询没有分类的商品
select * from product where category_id is not null;

-- 查询表列
select name, price from product;

-- 查询以什么开头的所有数据
select * from productGood where name like '李%'; # 查询1个字的所有name
select * from productGood where name like '李_'; # 查询2个字的所有name
select * from productGood where name like '李__'; # 查询3个字的所有name

-- 查询第二个字为什么的所有商品
select * from productGood where name like '_四%';


-- 将所有商品价格+10进行显示
select name, price+10 from product;

-- 起别名 as 别名，as 也可以不写省略
-- select name, price as 价格 from product as p;
select name, price as 价格 from product;

update product set category_id=null where name='张三5';

--  案例1单表查询，简单查询
/**
  单表查询的完整语法：
     select
          distinct 列1, 列2 ...
     from
         数据表名
     where
        组前筛选
     group by
        分组字段
     having
       组后筛选
     order by
       排序字段 [desc | asc]
     limit
       起始索引,数据条数
 */

# select
#     distinct name, price
# from
#      product
# where
#     price > 100




