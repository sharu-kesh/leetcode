# Write your MySQL query statement below
select a1.machine_id, round(avg(a1.timestamp - a0.timestamp), 3) as processing_time
from Activity a1
join Activity a0
on a1.machine_id = a0.machine_id and a1.process_id = a0.process_id and a1.activity_type = 'end' and a0.activity_type = 'start'
group by machine_id
order by machine_id