## Web stack debugging #4

Fifth in a series of debugging tasks:

### Task 1

<p>In this task, we will test how well our web server setup featuring Nginx is doing under pressure. Using ApacheBench, we see that it's not doing so well: huge amount of failed requests.</p>

<p>ApacheBench allows us to simulate HTTP requests to a web server. In this case, making 2000 requests to the web server with 100 requests at a time results in 679 failed requests</p>

* Remember we have to have ApacheBench installed. Since I'm using Ubuntu, this is the command I used to install it
```apt-get install apache2-utils```

```
root@2fb6931a06e5:~# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        201 bytes

Concurrency Level:      100
Time taken for tests:   3.045 seconds
Complete requests:      2000
Failed requests:        679
   (Connect: 0, Receive: 0, Length: 679, Exceptions: 0)
Non-2xx responses:      1321
Total transferred:      1069278 bytes
HTML transferred:       681069 bytes
Requests per second:    656.77 [#/sec] (mean)
Time per request:       152.260 [ms] (mean)
Time per request:       1.523 [ms] (mean, across all concurrent requests)
Transfer rate:          342.91 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    1  10.8      0      94
Processing:     1  149  55.0    194     298
Waiting:        1  148  55.0    194     298
Total:          3  150  54.8    196     298

Percentage of the requests served within a certain time (ms)
  50%    196
  66%    198
  75%    198
  80%    199
  90%    199
  95%    200
  98%    200
  99%    201
 100%    298 (longest request)
root@2fb6931a06e5:~# 
```

<p>We need to fix this so we get to 0 failed requests</p>

<p>And when we apply the puppet manifest...</p>

```
root@2fb6931a06e5:~# ab -c 100 -n 2000 localhost/
This is ApacheBench, Version 2.3 <$Revision: 1528965 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient)
Completed 200 requests
Completed 400 requests
Completed 600 requests
Completed 800 requests
Completed 1000 requests
Completed 1200 requests
Completed 1400 requests
Completed 1600 requests
Completed 1800 requests
Completed 2000 requests
Finished 2000 requests


Server Software:        nginx/1.4.6
Server Hostname:        localhost
Server Port:            80

Document Path:          /
Document Length:        612 bytes

Concurrency Level:      100
Time taken for tests:   2.634 seconds
Complete requests:      2000
Failed requests:        0
Total transferred:      1706000 bytes
HTML transferred:       1224000 bytes
Requests per second:    759.40 [#/sec] (mean)
Time per request:       131.683 [ms] (mean)
Time per request:       1.317 [ms] (mean, across all concurrent requests)
Transfer rate:          632.59 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0   15  35.8      1     198
Processing:     1  114  60.5    101     396
Waiting:        1  107  61.9     99     396
Total:          2  129  56.9    102     400

Percentage of the requests served within a certain time (ms)
  50%    102
  66%    130
  75%    196
  80%    197
  90%    199
  95%    201
  98%    203
  99%    204
 100%    400 (longest request)
```

<p>... we get 0 failed requests</p>

### Task 2
<p> In this task, the OS configuration needs to be changed so that it is possible to login with the holberton user and open a file without any error message. Currently, this is what a user gets if s/he tries to log in with the holberton user: </p>

```
root@49e40b5c9e85:~# su - holberton
-su: /etc/profile: Too many open files
-su: /home/holberton/.bash_profile: Too many open files
-su-4.3$ 
-su-4.3$ head /etc/passwd
-su: start_pipeline: pgrp pipe: Too many open files
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
-su-4.3$ 
-su-4.3$ 
-su-4.3$ logout
-su: /home/holberton/.bash_logout: Too many open files
-su: /etc/bash.bash_logout: Too many open files
root@49e40b5c9e85:~# 
```

<p> But then after the manifest with the configuration is applied, we can now login as the holberton user as follows:</p>

```
root@49e40b5c9e85:~# su - holberton
holberton@49e40b5c9e85:~$ head /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
holberton@49e40b5c9e85:~$ 
```
