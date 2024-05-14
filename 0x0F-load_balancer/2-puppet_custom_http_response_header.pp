#install nginx using apt provider
package{'nginx':
    ensure          => 'installed',
    provide         => 'apt',
    install_options => '-y',
}
#add a custom header X-Served-By with value 
#as the hostname of the server Nginx is running on.
exec { 'add_header':
    command => "sed -i '/http {/a\\tadd_header X-Served-By $(hostname);' /etc/nginx/nginx.conf",
    require => Package['nginx'],
    notify  => Service['nginx'],
}

exec{'test_nginx_config':
    command     => 'nginx -t',
    refreshonly => true,
    subscribe   => File['/etc/nginx/nginx.conf']
}

service {'nginx':
    ensure    => 'running',
    enable    => true,
    subscribe => Exec['add_header'],
}