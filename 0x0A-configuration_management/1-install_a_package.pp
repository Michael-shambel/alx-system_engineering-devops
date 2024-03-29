#!/usr/bin/pup
# install flask from pip3 Version must be 2.1.0

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.0.3',
  unless  => '/usr/bin/pip3 show Flask | grep -q "Version: 2.1.0"',
}
