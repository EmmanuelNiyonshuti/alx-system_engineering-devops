#find and fix a bug on apache webserver

include stdlib

service {'apache2':
  ensure => running ,
}
file_line {'correct_class_wp_locale':
  path  => '/var/www/html/wp-settings.php',
  match => '/class-wp-locale.phpp',
  line  => "require_once( ABSPATH . WPINC . '/class-wp-locale.php' );",
}

