from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, DateType, DoubleType
import pyspark.sql.functions as F
from datetime import date

def main():
    print("Iniciando la ejecución principal de la Actividad 2...")
    
    # Iniciar SparkSession
    spark = SparkSession.builder \
        .appName("Actividad_2_Macroeconomia_Oro") \
        .master("local[*]") \
        .getOrCreate()
        
    print(f"Versión de Spark: {spark.version}")
    
    # 1. Definición del esquema
    macro_schema = StructType([
        StructField('Date', DateType(), False),
        StructField('Gold_Price', DoubleType(), True),
        StructField('Inflation_Rate', DoubleType(), True),
        StructField('GDP_Growth', DoubleType(), True),
        StructField('Interest_Rate', DoubleType(), True)
    ])
    print("\nEsquema definido correctamente.")
    
    # 2. Lectura/Generación de datos (Mocking para ejecución local)
    print("Generando datos de prueba simulando la carga de Kaggle...")
    data = [
        (date(2015, 1, 1), 1200.5, 1.2, 2.5, 0.5),
        (date(2016, 1, 1), 1250.0, 1.5, 2.8, 0.75),
        (date(2026, 1, 1), 2100.0, 3.5, 1.5, 4.5)
    ]
    df_macro = spark.createDataFrame(data, schema=macro_schema)
    
    # 3. Mostrar Metadatos y Descripción
    print("\n--- Esquema del DataFrame ---")
    df_macro.printSchema()
    
    print("\n--- Descripción de los Datos ---")
    df_macro.describe().show()
    
    # 4. Persistencia simulada (vista temporal para SQL)
    df_macro.createOrReplaceTempView('macroeconomic_gold_data')
    print("Vista temporal 'macroeconomic_gold_data' creada exitosamente.")
    
    # 5. Validaciones
    print("\n--- Consulta PySpark (SELECT y GROUP BY) ---")
    df_macro.filter(F.col('Gold_Price') > 1200) \
            .groupBy('Date') \
            .agg(F.avg('Gold_Price').alias('Avg_Gold_Price')) \
            .show()
            
    print("\n--- Consulta Spark SQL ---")
    spark.sql("""
        SELECT COUNT(*) as Total_Records, 
               AVG(Gold_Price) as Avg_Gold, 
               MAX(Inflation_Rate) as Max_Inflation 
        FROM macroeconomic_gold_data
    """).show()
    
    print("Ejecución finalizada con éxito.")
    spark.stop()

if __name__ == "__main__":
    main()
