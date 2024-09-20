# Write your MySQL query statement below
select round(count(A1.player_id) / (select count(distinct A3.player_id) from Activity A3),2) as fraction
from Activity A1
where (A1.player_id, DATE_SUB(A1.event_date, INTERVAL 1 DAY)) in (
        select A2.player_id, min(A2.event_date) from Activity A2
        group by A2.player_id
)