# Increases the amount of traffic an Nginx server can handle
# Increase the ULIMIT of the default file
# Then Restart Nginx to apply 

exec { 'Execute_fix_for_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

exec { 'Restart_Nginx_To_apply_changes':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
