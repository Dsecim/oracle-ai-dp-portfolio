from pyspark.sql import SparkSession, functions as F
from pyspark.sql.types import IntegerType, LongType


def main():
    spark = (
        SparkSession.builder
        .appName("ai-dp-churn-etl")
        .getOrCreate()
    )

    # ============================
    # Parâmetros (podem vir do OCI Data Flow)
    # ============================
    input_path = spark.conf.get(
        "spark.app.input_path",
        "data-generator/output/clientes.csv"
    )

    output_path = spark.conf.get(
        "spark.app.output_path",
        "lake/clientes_churn_parquet"
    )

    # ============================
    # Leitura
    # ============================
    df = spark.read.option("header", True).csv(input_path)

    print("Schema original:")
    df.printSchema()

    # ============================
    # Tipagem
    # ============================
    df = (
        df
        .withColumn("customer_id", F.col("customer_id").cast(LongType()))
        .withColumn("idade", F.col("idade").cast(IntegerType()))
        .withColumn("renda", F.col("renda").cast(IntegerType()))
        .withColumn("tempo_cliente", F.col("tempo_cliente").cast(IntegerType()))
        .withColumn("qtd_chamados", F.col("qtd_chamados").cast(IntegerType()))
        .withColumn("atraso_pagamento", F.col("atraso_pagamento").cast(IntegerType()))
        .withColumn("churn", F.col("churn").cast(IntegerType()))
    )

    # ============================
    # Qualidade básica
    # ============================
    df = df.dropDuplicates(["customer_id"])

    df = df.filter(F.col("customer_id").isNotNull())

    # ============================
    # Enriquecimento
    # ============================
    df = df.withColumn(
        "faixa_renda",
        F.when(F.col("renda") < 4000, "baixa")
         .when(F.col("renda").between(4000, 8000), "media")
         .otherwise("alta")
    )

    # ============================
    # Escrita no Data Lake (Parquet)
    # ============================
    (
        df.write
        .mode("overwrite")
        .parquet(output_path)
    )

    print(f"Dados gravados em: {output_path}")

    # ============================
    # (Opcional) Escrita no Autonomous DB
    # ============================
    # df.write \
    #   .format("jdbc") \
    #   .option("url", "<JDBC_URL>") \
    #   .option("dbtable", "CLIENTES_CHURN") \
    #   .option("user", "<USER>") \
    #   .option("password", "<PASSWORD>") \
    #   .mode("append") \
    #   .save()

    spark.stop()


if __name__ == "__main__":
    main()
