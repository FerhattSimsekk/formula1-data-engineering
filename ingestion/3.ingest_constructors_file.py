# Databricks notebook source
dbutils.widgets.text("p_data_source", "")
v_data_source = dbutils.widgets.get("p_data_source")

# COMMAND ----------

dbutils.widgets.text("p_file_date", "2021-03-21")
v_file_date = dbutils.widgets.get("p_file_date")

# COMMAND ----------

# MAGIC %run ../includes/configuration
# MAGIC

# COMMAND ----------

# MAGIC %run ../includes/common_functions

# COMMAND ----------

constructors_schema = "constructorId INT, constructorRef STRING, name STRING, nationality STRING, url STRING"

# COMMAND ----------

constructor_df=spark.read.json(f"{raw_folder_path}/{v_file_date}/constructors.json",schema=constructors_schema)

# COMMAND ----------

display(constructor_df)

# COMMAND ----------

from pyspark.sql.functions import col,current_timestamp,lit

# COMMAND ----------

constructor_dropped_df=constructor_df.drop(col('url'))

# COMMAND ----------

constructor_final_df=constructor_dropped_df.withColumnRenamed('constructorId','constructor_id')\
.withColumnRenamed('constructorRef','constructor_ref') \
.withColumn("data_source", lit(v_data_source)) \
.withColumn("file_date", lit(v_file_date))



# COMMAND ----------

constructor_final_df=add_ingestion_date(constructor_final_df)

# COMMAND ----------

display(constructor_final_df)

# COMMAND ----------

constructor_final_df.write.mode('overwrite').format("delta").saveAsTable("f1_processed.constructors")

# COMMAND ----------

# MAGIC %fs ls /mnt/formula1dltr/processed/constructors

# COMMAND ----------

display(spark.read.format('delta').load("/mnt/formula1dltr/processed/constructors"))

# COMMAND ----------

dbutils.notebook.exit("Success")