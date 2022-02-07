# py-dbt-html-docs
python script para convertir un schema.yml de dbt en una tabla HTML

### Qué es [DBT](https://docs.getdbt.com/) ?

### De qué se trata esto?
Cuando comienzas a usar DBT para hacer modelos de datos, 
comienzas a escribir sobre el significado de las columnas de las tablas resultantes. 
Si no usas DBT en la nube, vas a ver que cuando corres el servidor de documentación de dbt
```dbt docs generate && dbt docs serve ```, en las descripciones de los campos, si son exageradamente grandes,
se pierden en la vista... Para poder leerlos bien, es necesario darle doble click a la descripción.

Este pequeño script, muestra cada columna con el detalle de su descripción ingresada
en el archivo yaml, en formato HTML.