# Databricks notebook source
# MAGIC %md
# MAGIC ### Ingest races.csv file

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Step 1 - Read the CSV file using the spark dataframe reader API

# COMMAND ----------

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

from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DateType

# COMMAND ----------

races_schema = StructType(fields=[StructField("raceId", IntegerType(), False),
                                  StructField("year", IntegerType(), True),
                                  StructField("round", IntegerType(), True),
                                  StructField("circuitId", IntegerType(), True),
                                  StructField("name", StringType(), True),
                                  StructField("date", DateType(), True),
                                  StructField("time", StringType(), True),
                                  StructField("url", StringType(), True) 
])

# COMMAND ----------

races_df = spark.read \
.option("header", True) \
.schema(races_schema) \
.csv(f"{raw_folder_path}/{v_file_date}/races.csv")

# COMMAND ----------

display(races_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Step 2 - Add ingestion date and race_timestamp to the dataframe

# COMMAND ----------

from pyspark.sql.functions import current_timestamp, to_timestamp, concat, col, lit,coalesce,when,concat_ws

# COMMAND ----------

from pyspark.sql.functions import when

races_clean = races_df.withColumn(
    "time",
    when(col("time") == "\\N", None).otherwise(col("time"))
)

# COMMAND ----------


races_with_timestamp_df = races_clean.withColumn(
    "race_timestamp",
    to_timestamp(
        concat(col("date"), lit(" "), coalesce(col("time"), lit("00:00:00"))),
        "yyyy-MM-dd HH:mm:ss"
    )
).withColumn("data_source", lit(v_data_source)) \
 .withColumn("file_date", lit(v_file_date))   


# COMMAND ----------

races_with_timestamp_df=add_ingestion_date(races_with_timestamp_df)

# COMMAND ----------

display(races_with_timestamp_df)

# COMMAND ----------

races_with_timestamp_df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Step 3 - Select only the columns required & rename as required

# COMMAND ----------

races_selected_df = races_with_timestamp_df.select(
    col('raceId').alias('race_id'),
    col('year').alias('race_year'),
    col('round'),
    col('circuitId').alias('circuit_id'),
    col('name'), 
    col('ingestion_date'),     # CSV’den gelen tarih
    col('race_timestamp')                   # timestamp olarak birleşmiş tarih+saat
   
)

# COMMAND ----------

display(races_selected_df)

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Write the output to processed container in parquet format

# COMMAND ----------

races_selected_df.write.mode("overwrite").partitionBy('race_year').format("delta").saveAsTable("f1_processed.races")

# COMMAND ----------

# MAGIC %fs ls /mnt/formula1dltr/processed/races

# COMMAND ----------

display(spark.read.format('delta').load('/mnt/formula1dltr/processed/races'))

# COMMAND ----------

dbutils.notebook.exit("Success")