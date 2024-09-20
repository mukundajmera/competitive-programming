# Write your MySQL query statement below
select 
contest_id, 
round(count(distinct user_id) * 100 /(select count(user_id) from Users) ,2) as percentage
from  Register
group by contest_id
order by percentage desc,contest_id
-- select r.contest_id,
--  round(count(distinct u.user_id) * 100 / (select count(user_id) from Users) , 2) as percentage
-- from Register r
-- left join  Users u 
-- on r.user_id  = u.user_id
-- group by r.contest_id
-- order by percentage DESC, r.contest_id
