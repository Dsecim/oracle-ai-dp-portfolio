# Spark Job — Churn ETL

Este job realiza o processamento dos dados de clientes para o projeto Oracle AI DP:

## Passos executados
1. Leitura de CSV
2. Tipagem de colunas
3. Remoção de duplicados
4. Validações básicas
5. Enriquecimento (faixa_renda)
6. Escrita em Parquet (lake)
7. (Opcional) Escrita no Autonomous Database

## Execução local

```bash
pip install pyspark==3.5.1

spark-submit churn_etl.py \
  --conf spark.app.input_path=data-generator/output/clientes.csv \
  --conf spark.app.output_path=lake/clientes_churn_parquet
