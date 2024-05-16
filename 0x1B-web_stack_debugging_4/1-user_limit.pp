# Set limits for all users
file { '/etc/security/limits.conf':
  ensure  => present,
  content => "* hard nofile 65536\n* soft nofile 65536\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}

# Apply the limits
exec { 'apply_limits':
  command => '/bin/systemctl daemon-reexec',
  path    => ['/bin', '/sbin', '/usr/bin', '/usr/sbin'],
  require => File['/etc/security/limits.conf'],
}

