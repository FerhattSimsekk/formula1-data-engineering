-- Databricks notebook source
select * from f1_presentation.calculated_race_results

-- COMMAND ----------

select team_name,
count(*) as race_counts,
sum(calculated_position) as total_points,
avg(points) as avg_points,
count(1) as total_races
from f1_presentation.calculated_race_results

group by team_name
having count(*)>=100
order by avg_points desc


-- COMMAND ----------

select team_name,
count(*) as race_counts,
sum(calculated_position) as total_points,
avg(points) as avg_points,
count(1) as total_races
from f1_presentation.calculated_race_results
where race_year between 2011 and 2020
group by team_name
having count(*)>=100
order by avg_points desc


-- COMMAND ----------

select team_name,
count(*) as race_counts,
sum(calculated_position) as total_points,
avg(points) as avg_points,
count(1) as total_races
from f1_presentation.calculated_race_results
where race_year between 2001 and 2010
group by team_name
having count(*)>=100
order by avg_points desc