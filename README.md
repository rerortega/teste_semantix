# teste_semantix

## Qual o objetivo do comando cache em Spark?
O comando cache é uma técnica de otimização de processos. Retém processos que podem ser utilziados posteriormente de forma intermediária, fazendo com que haja rapidez na execução.


## O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?
Sim, devido ao fato de Spark trabalhar com processamento em memória podendo utilizar *cache* em processamentos similares intermediários, por sua vez, MapReduce, grava em disco a cada processamento. Portanto, Spark é muito mais recomendado para algoritmos de machine learning ou qualquer outro tipo de implementação onde há a necessidade de análise em tempo real, do que MapReduce. 

## Qual é a função do SparkContext?
A função SparkContext é um objeto de configuração do Spark para as aplicações. Configurando a forma de como irá acessar os clusters, atribuição de nome para aplicação, acesso ou bloqueio de aplicações, entre outras configuraçãoes. 

## Explique com suas palavras o que é Resilient Distributed Datasets (RDD).
Os RDDs, de forma macro, é uma forma de armazenamento de dados que são distribuídos em várias máquinas (como se fossem tabelas), possibilitando a leitura de forma mais veloz. Os RDDs são imutáveis. Há possibilidade de, basicamente, somente duas operações: Transformations (map, filter, join, union, etc) e Actions (reduce, count, first, etc) e cada vez que os RDDs sofrem estas operações, o RDD original não é modificado, é gerado um novo.

## Explique o que o código Scala abaixo faz.
- Carrega o arquivo em uma variável com o nome *textFile*
- Introduz cada palavra separada por " " dentro da variável *counts*
- Contabiliza a quantidade de vezes que cada palavra apareceu no arquivo
- Salva o resultado num arquivo texto. 
 

# Referências:
https://docs.databricks.com/delta/delta-cache.html
https://docs.microsoft.com/pt-br/azure/hdinsight/spark/apache-spark-perf
https://www.scala-lang.org/old/sites/default/files/linuxsoft_archives/docu/files/ScalaByExample-pt_BR.pdf
https://dadosdadosdados.wordpress.com/tag/spark/
https://www.scnsoft.com/blog/spark-vs-hadoop-mapreduce
https://medium.com/@bradanderson.contacts/spark-vs-hadoop-mapreduce-c3b998285578
http://developers.socialminer.com/2018/12/07/otimizando-apache-spark-com-s3/
https://data-flair.training/blogs/apache-spark-rdd-persistence-caching/
https://www.infoq.com/br/articles/mapreduce-vs-spark/



