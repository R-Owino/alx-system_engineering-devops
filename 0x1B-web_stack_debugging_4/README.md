## Web stack debugging #4

- Fifth in a series of debugging tasks
<p>In this task, we will test how well our web server setup featuring Nginx is doing under pressure. Using ApacheBench, we see that it's not doing so well: huge amount of failed requests.</p>
<p>ApacheBench allows us to simulate HTTP requests to a web server. In this case, making 2000 requests to the web server with 100 requests at a time results in 679 failed requests</p>

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
