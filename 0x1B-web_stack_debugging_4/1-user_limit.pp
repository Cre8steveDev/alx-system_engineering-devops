# Increasing the Soft and Hard file limit to enable the user holberton to login and open files without errors

exec { 'hard-file-limit-for-holberton-user-increment':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}

exec { 'soft-file-limit-for-holberton-user-increment':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf'
  path    => '/usr/local/bin/:/bin/'
}