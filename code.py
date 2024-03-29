# importando bibliotecas necessárias

from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.functions import split, regexp_extract
from pyspark.sql.functions import col

# Criando SparkContext e carregando os arquivos

sc = SparkContext()
sqlContext= SQLContext(sc)

df_jul = sqlContext.read.textFile("C:/Semantix/access_log_Jul95")
df_aug = sqlContext.read.textFile("C:/Semantix/access_log_Aug95")

# Inserindo e formatando nome das colunas

df_jul_format = df_jul.select(regexp_extract('value', r'^([^\s]+\s)', 1).alias('host'),
regexp_extract('value', r'^.*\[(\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})]', 1).alias('timestamp'),
regexp_extract('value', r'^.*"\w+\s+([^\s]+)\s+HTTP.*"', 1).alias('request'),
regexp_extract('value', r'^.*"\s+([^\s]+)', 1).cast('integer').alias('cod_http'),
regexp_extract('value', r'^.*\s+(\d+)$', 1).cast('integer').alias('tot_byte'))

df_aug_format = df_aug.select(regexp_extract('value', r'^([^\s]+\s)', 1).alias('host'),
regexp_extract('value', r'^.*\[(\d\d/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} -\d{4})]', 1).alias('timestamp'),
regexp_extract('value', r'^.*"\w+\s+([^\s]+)\s+HTTP.*"', 1).alias('request'),
regexp_extract('value', r'^.*"\s+([^\s]+)', 1).cast('integer').alias('cod_http'),
regexp_extract('value', r'^.*\s+(\d+)$', 1).cast('integer').alias('tot_byte'))

# Contabilizando por host

df_jul_format.groupBy('host').count().filter('count = 1').select('host').show()
df_aug_format.groupBy('host').count().filter('count = 1').select('host').show()

# Quantidade de erros 404

df_jul_format.groupBy('cod_http').count().filter('cod_http = "404"').show()
df_aug_format.groupBy('cod_http').count().filter('cod_http = "404"').show()

# Os 5 maiores Request de error 404

df_jul_format.filter('cod_http = "404"').groupBy('request').count().sort(col("count").desc()).show(5, truncate=False)
df_aug_format.filter('cod_http = "404"').groupBy('request').count().sort(col("count").desc()).show(5, truncate=False)

#Quantidade diária de error 404
df_jul_format.filter('cod_http = "404"').groupBy(df_jul_format.timestamp.substr(1,11).alias('day')).count().show()
df_aug_format.filter('cod_http = "404"').groupBy(df_jul_format.timestamp.substr(1,11).alias('day')).count().show()

#Total de Bytes por arquivo
df_jul_format.select('tot_byte').groupBy().sum().show()
df_aug_format.select('tot_byte').groupBy().sum().show()
