# ssh config file using puppet

file { '/root/.ssh/config':
  ensure => file,
  mode   => '0600',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  content => "
  35.153.232.94
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
}
