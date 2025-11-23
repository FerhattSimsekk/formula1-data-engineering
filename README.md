# 🏎️ Formula 1 Data Engineering Project (Azure Databricks + PySpark)

Bu proje, **Azure Databricks, Spark Core, PySpark, Spark SQL, Delta Lake ve Azure Data Factory** kullanılarak geliştirilmiş uçtan uca bir *Data Engineering (DE)* pipeline uygulamasıdır. Proje kapsamında Formula 1 motor sporları verileri kullanılarak gerçek bir kurumsal veri işleme süreci tasarlanmıştır.

---

## 🚀 Amaç

- Ham veri kaynaklarını Azure Data Lake'e almak  
- Databricks üzerinde PySpark kullanarak temizleme, dönüştürme ve modelleme  
- Delta Lake kullanarak **Lakehouse mimarisi** kurmak  
- Incremental load, Merge, Time Travel gibi profesyonel özellikleri uygulamak  
- Azure Data Factory ile pipeline orkestrasyonu yapmak  

---

## 🧱 Kullanılan Teknolojiler

### 🔹 **Azure**
- Azure Databricks  
- Azure Data Lake Gen2  
- Azure Data Factory  
- Unity Catalog  

### 🔹 **Spark**
- PySpark  
- Spark SQL  
- DataFrame API  
- Window Functions  

### 🔹 **Lakehouse**
- Delta Lake  
- Incremental Load  
- Merge / Upsert  
- Time Travel  
- Vacuum  

---

## 📁 Proje Klasörleri

/includes
|-- common functions, configuration helpers

/ingestion
|-- Ingesting CSV and JSON files into Bronze to silver Layer


/create_raw_tables
|--Creating raw tables

/transformations (Silver → Gold)
|-- join, groupBy, aggregate, window functions

/analysis
|-- Spark SQL ile raporlama ve analiz## 🧪 Gerçeklenen İşlemler

✔ CSV ve JSON ingest  
✔ Schema inference & manual schema  
✔ Lookup tabloları merge  
✔ Full & Incremental load  
✔ Delta formatına geçiş  
✔ Time Travel ile geçmiş veri görüntüleme  
✔ ADF ile pipeline oluşturma  
✔ Notebook parametre geçişleri  
✔ Unity Catalog ile veri yönetişimi  

---

## 📊 Sonuç Örnekleri (Project Outputs)

- Yarış sonuçları analizi  
- Sürücü ve takım performansı  
- Sezon bazlı istatistikler  
- En hızlı tur karşılaştırmaları  
- Power BI bağlantısı üzerinden dashboard oluşturma  

---

## 🎯 Kazanımlarım

Bu proje sayesinde aşağıdaki konularda yetkinlik kazandım:

- Azure Databricks üzerinde uçtan uca veri pipeline kurma  
- PySpark ile profesyonel veri işleme  
- Delta Lake ile Lakehouse mimarisi  
- Notebook workflow & parameterization  
- Azure Data Factory ile orkestrasyon  
- Unity Catalog ile veri yönetişimi  

---
