file{'/etc/ssh/ssh_config':
  ensure  => 'present',
  content => "\
HOST 34.232.68.210
        HOSTNAME 34.232.68.210
        user ubuntu
        PasswordAuthentication no
        IdentityFile ~/.ssh/school
	",
}
