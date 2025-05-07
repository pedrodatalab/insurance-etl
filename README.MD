# Insurance Data ETL Case

Este projeto tem foco na extração, transformação e integração de dados de apólices e sinistros. O objetivo é praticar a construção de pipelines de dados e preparar uma base unificada para análises futuras.

## 🎯 Objetivo

- Realizar a ingestão de múltiplas fontes de dados (`.csv`)
- Limpar e padronizar colunas (datas, nulos, formatos)
- Integrar as bases por chave comum (`policy_id`)
- Exportar o resultado final em formato Parquet

## 🛠️ Tecnologias e Bibliotecas

- Python 3.x
- pandas
- pyarrow (ou fastparquet)
- Jupyter Notebook


## Observações

Para melhorias futuras, criar um função que identifique as colunas de datas seu tipo, e fazer a conversão para datetime para limpar e padronizar as colunas. 
