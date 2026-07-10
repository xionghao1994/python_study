# 自查询:左表和右表是同一个表，根据连接查询条件查询两个表中的数据。

# 案例4:多表查询之 自关联(自连接)查询详解
# 概述:表自己和自己做关联查询，就称之为:自连接(自关联)查询.
# 一般用于:省市区三级联动.

use test01,

-- 创建省份表
create table if not exists provinces(
    id varchar(20) primary key comment '省份编码',
    name varchar(50) not null comment '省份名称'
) comment '省份表',

-- 创建城市表
create table if not exists city(
     id varchar(20) primary key comment '城市编码',
     name varchar(50) not null comment '城市名称',
     province_id varchar(20) not null comment '所属省份编码',
     foreign key (province_id) references provinces(id)
) comment '城市表',

-- 创建区县表
create table if not exists province(
    id varchar(20) primary key comment '区县编码',
    name varchar(50) not null comment '区县名称',
    city_id varchar(20) not null comment '所属城市编码',
    foreign key (city_id) references cities(id)
) comment '区县表',

-- ==================== 插入数据 ====================

-- 插入省份数据
insert into provinces values
('410000','河南省'),
('410000','河北省'),
('410000','湖北省');


-- 插入城市数据
insert into city values
('410100','郑州市','410000'),
('410200','开封市','410000'),
('410300','洛阳市','410000'),
('410400','平顶山市','410000'),
('410500','安阳市','410000'),

-- 插入郑州市下辖区县
insert into province values ('410102','中原区','410100'),
('410103','二七区','410100'),
 ('410104','管城回族区','410100'),
 ('410105','金水区','410100'),
 ('410106','惠济区','410100'),
('410108','郑东新区','410100'),
 ('410122','中牟县','410100'),
 ('410181','巩义市','410100'),
 ('410182','荥阳市','410100'),
('410183','新密市','410100'),
 ('410184','新郑市','410100'),
 ('410185','登封市','410100');



select * from areas,

truncate table cities;
drop table cities;

-- 查所有的省市区信息
# select
#     province.id, province.title
#     city.id, city.title,
#     county.id, count.title
# from
#     areas as county                              -- 县区表
# join areas as city on county.pid = city.id       -- 市表
# join areas as province on city.pid = province.id,-- 省表




