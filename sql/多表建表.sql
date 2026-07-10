# 多表建表 之 多对多
# 建表原则:新建中间表，该表至少有2列，充当外键列.分别去关联"多"的两方的主键列
# 学生和老师，订单和商品，学生和选修课

-- 建表
use test01;

-- ------案例------------------------
-- 学生表
create table student(
  sid int primary key auto_increment,
  name varchar(10)
);

-- 选修课表
create table course(
  cid int primary key auto_increment,
  name varchar(10)
);

-- 中间表
create table stu_cor(
    use_id int not null auto_increment,
    sid int,
    cid int
);

-- 中间表和学生表
alter table stu_cor add constraint fk_stu_mid foreign key(sid) references student(sid);
-- 中间表和选修课表
alter table stu_cor add constraint fk_stu_mid foreign key(cid) references student(cid);



/**
  扩展：
   1、case when
     格式：
       case
           when 条件1 then 值1
           when 条件2 then 值2
           when 条件3 then 值3
           ...
           else 值n
        end as 别名
  执行流程:
    1.case.when值选择语句，首先会先判断条件1是否成立，如果成立则执行对应的值1，整个casewhen语句结束.
    2.如果条件1不成立，则会立即执行条件2，看其是否成立，成立走对应的值2，然后整个语句结束.
    3.如果条件2不成立，则会立即执行条件3...依次类推.
    4.如果所有的条件都不成立，则执行 else语句，然后整个case.when结束.

  select
     order_id,customer_id, shipped_date, ship_country,
     case
        when ship_country='France' then '法国'
        when ship_country='Germany' then '德国'
        when ship_country='Brazil' then '巴西'
        else'其它国家'
     end as new_ship_country
  from orders limit 10;

   2、扩展:if()函数.
      格式:if(关系表达式，值1，值2)
      执行流程:先执行关系表达式，看其结果是否成立，成立则返回值1，否则返回值2.
    select i(5>3,'张三','李四'); --张三
    select i(5 <3,'张三','李四); --李四

   需求:统计运输到法国的订单的数量，
   select count(*) from orders where ship_country='France'; -- 77

   select count( if(ship_country='France', 1, null) ) from orders; --77
 */





