-- Implement your solution here
select event_type, sum(case when rn=1 then value else 0 end) - sum(case when rn=2 then value else 0 end) as value
from 
(
    select event_type,value,row_number() over (partition by event_type order by time desc) as rn
    from events
) tmp
group by event_type
having count(*)>1

with deltas as (
    select distinct event_type,
    first_value(value) over (partition by event_type order by time desc) -
    nth_value(value,2) over (partition by event_type order by time desc) as delta
    from events
)
select *
from deltas
where delta is not null order by 1