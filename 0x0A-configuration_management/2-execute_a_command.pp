# manifest that kills a process named killmenow

exec { 'pkill':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  provider => 'shell',
}
