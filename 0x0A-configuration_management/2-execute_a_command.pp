# This manifest file kills a process named killmenow

exec {'kill_process':
command => '/usr/bin/pkill killmenow',
}