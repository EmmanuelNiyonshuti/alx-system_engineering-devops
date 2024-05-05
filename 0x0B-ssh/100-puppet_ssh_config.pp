include ::stdlib

#This manifest file will make changes to the ssh client configuration file
#Requirements:
#       -SSH client configuration must be configured to use the private key ~/.ssh/school
#       -SSH client configuration must be configured to refuse to authenticate using a password

file_line{'PasswordAuthentication':
    ensure => 'present',
    line   => 'PasswordAuthentication no',
    match  => '^#?PasswordAuthentication no',
    path   => '/etc/ssh/ssh_config',

}

file_line {'IdentityFile':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
  match  => '^#?~/.ssh/school',
}