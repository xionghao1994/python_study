# 交叉查询
-- select * from 表A, 表B;

# 链接查询
-- 显示内查询
-- select * from 表A 别名 join 表B 别名 on 条件

-- 隐式内查询
-- select * from 表A,表B where 条件 (不咋用，可不记)

-- 左外查询
-- select * from 表A 别名 left outer join 表B 别名 on 条件

-- 右外查询
-- select * from 表A 别名 right outer join 表B 别名 on 条件 (不咋用，可不记)

-- ------ 子查询-----------
/**
  介绍：
  实际开发中，如果1个查询语句的“查询条件”需要依赖另一个查询语句的“查询结果”，这种写法就叫子查询
  即 1个SQL的查询条件，依赖另1个SQL语句的查询结果，
   外边的查询叫主查询，里面的查询叫子查询
  格式： select * from 表A where 字段 > ( select 列名 from 表B where ...);
  数据量小：IN 子查询可读性更好  where in
  数据量大百万级：JOIN 通常性能更优 where join
 */







