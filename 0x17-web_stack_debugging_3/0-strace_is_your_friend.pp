#fix bad "phpp" line

exec{'fix-word':
  command => 'sed -i "s/\b.phpp\b/.php/g" /var/www/html/wp-settings.php',
  path    => 'usr/local/bin/:/bin/'
}
