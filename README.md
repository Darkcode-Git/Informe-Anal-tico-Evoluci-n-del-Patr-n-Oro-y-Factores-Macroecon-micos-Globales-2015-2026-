# Evidencia de aprendizaje (EA3) - Taller: procesamiento de datos en una infraestructura cloud

Este repositorio contiene el desarrollo de la **Evidencia de Aprendizaje 3 (EA3)** para el procesamiento de un dataset sobre factores macroeconómicos y el precio del oro en una infraestructura cloud utilizando Databricks Community Edition.

## 🎯 Objetivo
Buscar/recolectar un conjunto de datos y desplegarlo sobre una infraestructura virtual en Databricks Community Edition, diseñando el esquema de almacenamiento, configurando la arquitectura básica, cargando datos desde Kaggle y validando el procesamiento con Spark y SQL.

## 📂 Archivos del repositorio
- `apellido_nombre_Actividad_2.ipynb`: Jupyter Notebook exportado desde Databricks con todo el desarrollo (esquema, ingesta, validaciones Spark y SQL, conclusiones).
- `scripts/`: Carpeta con los códigos PySpark y SQL extraídos del notebook para referencia rápida.

## ⚙️ Esquema de los datos
El dataset modela la relación de variables macroeconómicas con el oro. 

| Campo | Tipo | Nulabilidad | Descripción |
|-------|------|-------------|-------------|
| Date | DateType | No | Fecha del registro (PK) |
| Gold_Price | DoubleType | Sí | Precio del oro |
| Inflation_Rate | DoubleType | Sí | Tasa de inflación global |
| GDP_Growth | DoubleType | Sí | Crecimiento del PIB |
| Interest_Rate | DoubleType | Sí | Tasa de interés promedio |

## 💻 Código PySpark y SQL 

### 1. Definición del Esquema (PySpark)
```python
from pyspark.sql.types import StructType, StructField, DateType, DoubleType

macro_schema = StructType([
    StructField('Date', DateType(), False),
    StructField('Gold_Price', DoubleType(), True),
    StructField('Inflation_Rate', DoubleType(), True),
    StructField('GDP_Growth', DoubleType(), True),
    StructField('Interest_Rate', DoubleType(), True)
])
```

### 2. Carga y Persistencia de Datos
```python
# Carga de datos
file_path = '/FileStore/datasets/macro_gold_data.csv'
df_macro = spark.read.csv(file_path, header=True, schema=macro_schema)

# Persistencia como tabla
df_macro.write.mode('overwrite').saveAsTable('macroeconomic_gold_data')
```

### 3. Validaciones 

#### En PySpark
```python
import pyspark.sql.functions as F

# Metadatos
df_macro.printSchema()

# Descripción
df_macro.describe().show()

# SELECT y GROUP BY
df_macro.filter(F.col('Gold_Price') > 1200) \
        .groupBy('Date') \
        .agg(F.avg('Gold_Price').alias('Avg_Gold_Price')) \
        .show()
```

#### En Spark SQL
```sql
-- Metadatos
DESCRIBE TABLE macroeconomic_gold_data;
SHOW CREATE TABLE macroeconomic_gold_data;

-- Descripción y Agregaciones
SELECT COUNT(*), AVG(Gold_Price), MAX(Inflation_Rate) 
FROM macroeconomic_gold_data;

-- SELECT y GROUP BY
SELECT Date, AVG(Gold_Price) as Avg_Gold_Price
FROM macroeconomic_gold_data 
WHERE Gold_Price > 1200
GROUP BY Date;
```

## ⚖️ Comparativa: SQL vs Spark
- **SQL**: Facilidad de uso, expresividad declarativa, excelente integración con herramientas BI. Puede ser limitado para pipelines muy complejos o funciones personalizadas (UDFs) avanzadas.
- **Spark (PySpark)**: Alta escalabilidad, APIs ricas (DataFrame, RDD), permite integrar Machine Learning y control detallado del rendimiento, aunque la curva de aprendizaje es más pronunciada.
