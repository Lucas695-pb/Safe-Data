<?php
$CONFIG = array(
    'dbtype' => 'mysql',
    'dbname' => getenv('DB_NAME'),
    'dbuser' => getenv('DB_USER'),
    'dbpassword' => getenv('DB_PASSWORD'),
    'dbhost' => getenv('DB_HOST'),
    'dbport' => getenv('DB_PORT'),
    'trusted_domains' => array(
        0 => 'localhost',
        1 => '127.0.0.1',
        2 => '192.168.1.xxx' # Coloca tu IP local aqui si es necesario
    ),
    'redis' => array(
        'host' => 'redis',
        'port' => 6379,
    ),
    'memcache.local' => '\\OC\\Memcache\\APCu',
    'memcache.locking' => '\\OC\\Memcache\\Redis',
    'datadirectory' => '/var/www/html/data',
    'updatechecker' => true,
    'updater.server.url' => 'https://updates.nextcloud.com/updater_server/',
    'passwordsalt' => 'TU_SAL_AQUI',  // Genera una sal segura
    'secret' => 'TU_SECRETO_AQUI', // Genera un secreto seguro
    'mail_smtpmode' => 'smtp',
    'mail_smtphost' => 'smtp.example.com',
    'mail_smtpport' => 587,
    'mail_smtpauth' => true,
    'mail_smtpname' => 'tu_correo@example.com',
    'mail_smtppassword' => 'tu_contraseña',
    'logfile' => '/var/www/html/data/nextcloud.log',
    'loglevel' => 2,
    'upload_max_filesize' => '10G',
    'max_filesize_animated_gifs' => '10G',
);
