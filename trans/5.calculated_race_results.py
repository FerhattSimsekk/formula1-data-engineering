# Databricks notebook source
dbutils.widgets.text("p_file_date", "2021-03-28")
v_file_date = dbutils.widgets.get("p_file_date")

# COMMAND ----------

# MAGIC %sql
# MAGIC use f1_processed
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC create table f1_presentation.calculated_race_results
# MAGIC using parquet
# MAGIC as
# MAGIC select races.race_year,
# MAGIC constructors.name as team_name,
# MAGIC drivers.name as driver_name,
# MAGIC results.position,
# MAGIC results.points,
# MAGIC 11-results.position as calculated_position
# MAGIC
# MAGIC from
# MAGIC results
# MAGIC join f1_processed.drivers on (results.driver_id=drivers.driver_id)
# MAGIC join f1_processed.constructors on (results.constructor_id=constructors.constructor_id)
# MAGIC join f1_processed.races on (results.race_id=races.race_id)
# MAGIC where results.position<=10

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from f1_presentation.calculated_race_results