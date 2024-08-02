select a.machine_id,
Round(AVG(b.timestamp - a.timestamp),3) as processing_time
 from Activity a, Activity b
where a.machine_id = b. machine_id
and a.process_id = b.process_id
AND a.activity_type = 'start'
AND b.activity_type = 'end'
group by a.machine_id