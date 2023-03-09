user { 'holberton':
  ensure     => present,
  managehome => true,
  shell      => '/bin/bash',
}

file { '/etc/security/limits.d/holberton.conf':
  ensure  => file,
  content => "holberton hard nofile 50000\nholberton soft nofile 50000\n",
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
}