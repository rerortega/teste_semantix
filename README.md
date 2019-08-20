# teste_semantix

## Qual o objetivo do comando cache em Spark?
O comando cache é uma técnica de otimização de processos. Retém processos que podem ser utilziados posteriormente de forma intermediária, fazendo com haja rapidez na execução.


## O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?
Sim, devido ao fato de Spark trabalhar com processamento em memória podendo utilizar *cache* em processamentos similares intermediários, por sua vez, MapReduce, grava em disco a cada processamento. Portanto, Spark é muito mais recomendado para algoritmos de machine learning ou qualquer outro tipo de implementação onde há a necessidade de análise em tempo real, do que MapReduce. 

## Qual é a função do SparkContext?



# Referências:
https://docs.databricks.com/delta/delta-cache.html
https://docs.microsoft.com/pt-br/azure/hdinsight/spark/apache-spark-perf
https://www.scala-lang.org/old/sites/default/files/linuxsoft_archives/docu/files/ScalaByExample-pt_BR.pdf
https://dadosdadosdados.wordpress.com/tag/spark/
https://www.scnsoft.com/blog/spark-vs-hadoop-mapreduce
https://medium.com/@bradanderson.contacts/spark-vs-hadoop-mapreduce-c3b998285578
http://developers.socialminer.com/2018/12/07/otimizando-apache-spark-com-s3/
https://data-flair.training/blogs/apache-spark-rdd-persistence-caching/


