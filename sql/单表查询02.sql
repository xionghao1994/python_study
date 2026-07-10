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

# 分组查询

# 面试题： where 和 having 的区别是什么
-- 答案： where: 组前筛选，后边不能跟聚合函数
--       having: 组后筛选， 后边可以跟聚合函数


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

# 添加表字段
alter table day01 add sex varchar(2);

# 增加表字段
# insert into day01 values
# (null,'张三', '10001', 100),
# (null,'张三', '10002', 100);

select * from day01;

-- 将男女分组
select * from day01 where sex='男';

# 统计每类商品总价（单价>500），筛选总价>2000的分组，按总价升序取最低价分组

-- 创建表
create table if not exists day02(
    id int primary key auto_increment comment '商品主键',
    name varchar(10) not null comment '商品姓名',
    price double not null comment '商品价格',
    category_id int not null comment '商品分类'
);

insert into day02(name,price,category_id) values
('手机1',1200,1),
('手机2',1500,1),
('手机壳',50,1),
('笔记本电脑',3000,2),
('鼠标',120,2),
('平板',2100,3),
('耳机',600,3),
('键盘',450,3),
('冰箱',3200,4),
('洗衣机',2800,4);


-- 基本分组，查分类
select category_id from day02 group by category_id;
-- 解释：SELECT 只有分组字段category_id，符合规则

-- 分组+聚合（统计每组总价）
-- 需求：单价 > 500，按分类算总价，只保留总价 > 2000，总价升序
select
    category_id, # (他有)
    count(price) as total_price -- 聚合函数，允许出现
from
    day02
where
    price > 500 -- 先筛单价500以上商品
group by
    category_id -- 按分类分组  (他就有)
having
    sum(price) > 2000 -- 分组后筛总价大于2000
order by
    total_price; -- 按总价排序

/**
    select 只能写【分组字段】或【SUM/COUNT 等聚合】；
    先 where 过滤单行；
    group by 写你要分组的字段；
    having 过滤聚合总和；
    order by 最后排序。
 */


# limit 分页查询,索引从0开始，如果起始是从0开始，0可以不写直接写5就行
# limit 起始位置, 条数
select * from day02 limit 0,5; # 查询前5条数据

/**
   重点：
   数据总条数 select count(*)
   数据总页数据 一般是10
   每页起始索引 (当前页数 - 1) * 每页的数据条数
   总页数：(总条数 + 每页的数据条数 -1)/每页的数据条数 得出的取整数就行不要余数
      FLOOR(1,4) 求地板数,以最小的数为主
      CEIL(2,4) 天花板数据，以最大的数为主
 */

# distinct 去重查询(少量数据用)
-- 单列去重
select distinct name from day02;
-- 多列去重
select distinct  name, price from day02;

# group by去重（大量数据用,不卡死）
select category_id from day02 group by category_id;


















