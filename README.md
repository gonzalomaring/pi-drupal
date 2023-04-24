# Monitorización de escenario

Usaremos varias herramientas para monitorizar el escenario, siendo éste compuesto por un CMS Drupal y MariaDB

## Balanceador de carga

El balanceador elegido es HAProxy siendo Round Robin el método de balanceo escogido.

## Recolección de logs de Drupal

Para esta tarea usaremos Loki + Fluent Bit, siendo Grafana el panel elegido para visualizar dichos logs.

## Monitorización

El escenario estará montado en Docker usando Docker-Compose, por lo que usaremos Prometheus + Node Exporter para monitorizar la máquina host.


