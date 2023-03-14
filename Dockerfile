FROM drupal:9.4.8-php8.1-apache
#RUN apt-get update && apt-get install php-xdebug && apt-get clean && rm -rf /var/lib/apt/lists/*
RUN pecl install xdebug
