-- Implement your solution here
select b.team_id, b.team_name, COALESCE(sum(num_points),0) as num_points from 
teams b 
left join
(select host_team as team_id, score as num_points from
    (select *, 
    case when host_goals>guest_goals then 3
    when host_goals=guest_goals then 1
    else 0
    end as score
    from matches) temp1
union all
select guest_team as team_id, score as num_points from
    (select *, 
    case when guest_goals>host_goals then 3
    when host_goals=guest_goals then 1
    else 0
    end as score
    from matches) temp2
) a on a.team_id=b.team_id
group by b.team_id, b.team_name
order by num_points desc, b.team_id;