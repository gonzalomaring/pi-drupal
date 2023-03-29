# Recolección de logs de Drupal

Para esta tarea usaremos Grafana, Loki y Fluent Bit para la recolección de logs sobre un escenario con Drupal, MariaDB y HAProxy

## Versión Actual

Actualmente estamos usando una imagen de Drupal creada por mi, en la cual ya nos encontramos el Drupal funcionando en su versión 9.4. Las credenciales por defecto son "admin:admin" y por defecto se conectará a una base de datos llamada "drupal", al usuario "user" con contraseña "clave".

Si deseamos usar otra imagen, recomendaría "drupal:9.4-php8.0-apache-bullseye".

Antes de bajar el contenedor MariaDB es necesario ejecutar el siguiente comando:

~~~
docker exec drupal mysqldump -u user -pclave drupal -h mariadb > mariadb/drupal.sql
~~~


### Próximas mejoras del escenario

Está planificado añadir monitorización.

