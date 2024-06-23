#find and fix a bug on apache2 webserver

exec {'fix-wordpress-website':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
