--Question 1

select batting_team,sum(total_runs) as Runs_Scored
from deliveries 
group by batting_team;


-- Question 2

SELECT batsman, sum(batsman_runs) as Runs_Scored                                                       
FROM deliveries                                 
WHERE batting_team like 'Royal Challengers Bangalore'                                             
GROUP BY batsman                                     
ORDER BY sum(batsman_runs) DESC                   
LIMIT 10;  




-- Question 3

select country,count(*) as No_of_Umpires
from umpires where country not like 'India'
group by country;




-- Question 4

SELECT season, team, SUM(match_count) AS total_matches_played
FROM (
    SELECT season, team1 AS team, COUNT(*) AS match_count
    FROM matches
    GROUP BY season, team1
    UNION ALL
    SELECT season, team2 AS team, COUNT(*) AS match_count
    FROM matches
    GROUP BY season, team2
) AS subquery
GROUP BY season, team
ORDER BY season, team;



-- Question 5

select season,count(*) as no_of_matches
from matches group by season;



-- Question 6

select season,winner,count(*) AS Winnings 
from matches
group by season,winner
order by season;



-- Question 7

select winner,sum(win_by_runs) Total_Runs_Conceded 
from matches
where season = 2016
group by season ,winner;