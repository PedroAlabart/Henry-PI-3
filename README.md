Se utiliza AWS Glue como orquestador, empleando su módulo de Workflows.

Se crean distintos buckets S3 organizados por capas:

source → datos de entrada.

bronze → datos crudos.

silver → datos transformados.

gold   → datos desnormalizados
athena → resultados de consultas.

Se utiliza AWS Athena para visualizar y consultar los datos ya transformados y agregados del dataset.

![arquitectura](images/architecture.png)

La fuente de datos consta de 2 csv con la siguiente preview:

categorias.csv
![head categorias](images/ejemplo_categorias.png)

productos.csv
![head productos](images/ejemplo_productos.png)
