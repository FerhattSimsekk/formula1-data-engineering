-- Databricks notebook source
select driver_name,
count(*) as race_counts,
sum(calculated_position) as total_points,
round(avg(calculated_position),2) as avg_points
from f1_presentation.calculated_race_results
group by driver_name
having count(*)>=50
order by avg_points desc 

-- COMMAND ----------

select driver_name,
count(*) as race_counts,
sum(calculated_position) as total_points,
round(avg(calculated_position),2) as avg_points
from f1_presentation.calculated_race_results
where race_year between 2011 and 2020
group by driver_name
having count(*)>=50
order by avg_points desc 

-- COMMAND ----------

select driver_name,
count(*) as race_counts,
sum(calculated_position) as total_points,
round(avg(calculated_position),2) as avg_points
from f1_presentation.calculated_race_results
where race_year between 2001 and 2010
group by driver_name
having count(*)>=50
order by avg_points desc 