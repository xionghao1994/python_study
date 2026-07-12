
# ** 以下是34个练习题**

# 需求1:选中employees 表的所有数据


# 需求2:查询每个客户的ID， company name, contact name, contact title,city,和 country.并按照国家名字排序


# 替换快捷键:ctrl+ 字母R
# 需求3:查询每一个商品的product_name,category_name,quantity_per_unit
# unit_price,units_in_stock 并且通过 unit_price 字段排序
# 方式1:显示内连接


# 方式2:隐式内连接。



# 需求4:列出所有提供了4种以上不同商品的供应商列表所需字段:supplier_id，and products_count(提供的商品种类数量).company_name,



# 需求5:提取订单编号为10250的订单详情，显示如下信息:



# 需求6:收集运输到法国的订单的相关信息，包括订单涉及的顾客和员工信息，下单和发货日期等.


# 需求7:提供订单编号为10248的相关信息，
# 包括product name,unit price (在 order_items 表中),quantity (数量),
# company_name(供应商公司名字，起别名 supplier)


# 需求8: 提取每件商品的详细信息，包括 商品名称(product_name)，供应商的公司名称(company_name，在 suppliers表中),
#  类别名称 category_name,商品单价unit_price,和每单位商品数量quantity per unit


# 需求9:另一种常见的报表需求是查询某段时间内的业务指标，我们统计2016年7月的订单数量，



# 需求11:统计每个供应商供应的商品种类数量，结果返回供应商IDsUpplier_id
# ，公司名字company_name，商品种类数量(起别名products_count )使用 products 和 suppliers 表.


# 需求12:我们要查找ID为10250的订单的总价(折扣前)，SUM(unit_price * quantity)


# 需求13:统计每个员工处理的订单总数，结果包含员工IDemployee_id，
# 姓名first_name 和last_name.处理的订单总数(别名 orders_count)

# 需求15:计算每个员工的订单数量

# 需求16:计算每个客户的下订单数结果包含:用户id、用户公司名称、
# 订单数量(Customer_id,company_name,orders_count)


# 需求17:统计2016年6月到2016年7月用户的总下单金额并按金额从高到低排序


# 需求18:统计客户总数和带有传真号码的客户数量
# 需要字段:all_customers_count 和 customers_with_fax_count



