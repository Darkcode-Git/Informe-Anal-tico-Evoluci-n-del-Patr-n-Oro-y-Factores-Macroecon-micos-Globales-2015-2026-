from pyspark.sql.types import StructType, StructField, DateType, DoubleType
import pyspark.sql.functions as F

# 1. Definición del esquema
macro_schema = StructType([
    StructField('Date', DateType(), False),
    StructField('Gold_Price', DoubleType(), True),
    StructField('Inflation_Rate', DoubleType(), True),
    StructField('GDP_Growth', DoubleType(), True),
    StructField('Interest_Rate', DoubleType(), True)
])

# 2. Lectura de datos
file_path = '/FileStore/datasets/macro_gold_data.csv'
df_macro = spark.read.csv(file_path, header=True, schema=macro_schema)

# 3. Persistencia
df_macro.write.mode('overwrite').saveAsTable('macroeconomic_gold_data')

# 4. Validaciones
df_macro.printSchema()
df_macro.describe().show()

# Consulta SELECT y GROUP BY
df_macro.filter(F.col('Gold_Price') > 1200) \
        .groupBy('Date') \
        .agg(F.avg('Gold_Price').alias('Avg_Gold_Price')) \
        .show()
