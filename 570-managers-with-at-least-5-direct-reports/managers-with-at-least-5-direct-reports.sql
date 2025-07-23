# Write your MySQL query statement below
select name 
from Employee
where id in
(select e1.id
from Employee e
join Employee e1
on e1.id = e.managerId
group by e.managerId
having count(e1.id) > 4)