# Write your MySQL query statement below

select DISTINCT t1.num as ConsecutiveNums
from Logs as t1
inner join Logs as t2 on t1.id + 1 = t2.id 
inner join Logs as t3 on t1.id + 2 = t3.id
where t1.num = t2.num and t2.num = t3.num;