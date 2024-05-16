#increase the amount of traffic on th enginx server

#increase UNILIMT 
$ulimit_value = '4096'
file { '/etc/default/nginx':
  ensure  => present,
  content => "ULIMIT=\"-n ${ulimit_value}\"\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

#restart nginx
exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => 'etc/init.d/'
}
