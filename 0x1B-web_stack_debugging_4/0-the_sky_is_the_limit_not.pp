file_line { 'nginx_worker_connections':
  path  => '/etc/nginx/nginx.conf',
  line  => 'worker_connections 4048;',
  match => '^worker_connections',
}

file_line { 'nginx_multi_accept':
  path  => '/etc/nginx/nginx.conf',
  line  => 'multi_accept on;',
  match => '^#multi_accept',
}

file_line { 'nginx_types_hash_max_size':
  path  => '/etc/nginx/nginx.conf',
  line  => 'types_hash_max_size 4048;',
  match => '^types_hash_max_size',
}

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}