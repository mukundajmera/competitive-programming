select p.product_id, IFNULL(round(sum(p.price * unit.units) / sum(unit.units),2),0) as average_price  from prices p
left join unitssold unit
on p.product_id = unit.product_id and unit.purchase_date between p.start_date and p.end_date
group by p.product_id