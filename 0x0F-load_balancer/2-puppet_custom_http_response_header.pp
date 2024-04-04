# automate the task of creating a custom HTTP header response, but with Puppet.

exec {'update':
  provider => shell,
  command  => 'sudo apt-get -y update',
  before   => Exec['install Nginx'],
}

exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y install nginx',
  before   => Exec['add_header'],
}

exec { 'allow_nginx_http':
  command => '/usr/sbin/ufw allow "Nginx HTTP"',
  path    => ['/usr/sbin', '/usr/bin', '/bin'],
  unless  => '/usr/sbin/ufw status | grep "Nginx HTTP" | grep ALLOW',
  require => Package['ufw'], # Ensure the ufw package is installed before executing the command
}

$hostname = $facts['networking']['hostname']
$nginx_config = "
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;
    server_name _;
    add_header X-Served-By ${hostname};
    location / {
        try_files \$uri \$uri/ =404;
    }
    if (\$request_filename ~ redirect_me){
        rewrite ^ https://youtube.com permanent;
    }
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}"


file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => $nginx_config,
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}
