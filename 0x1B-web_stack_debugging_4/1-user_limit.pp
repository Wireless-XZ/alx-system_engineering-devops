# Change the limits for the holberton user
user_limits { 'holberton':
  limits => {
    'nofile' => {
      soft => '50000',
      hard => '60000',
    },
  },
}

# Set the file permissions for the file you want the holberton user to access
file { '/path/to/file':
  ensure  => present,
  content => "This is the content of the file.\n",
  mode    => '0644',
  owner   => 'root',
  group   => 'root',
}