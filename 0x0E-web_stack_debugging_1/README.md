## Web stack debugging #1

* Second in a series of debugging tasks

* Current server configurations in `/etc/nginx/sites-enabled`

	```server {
        	listen 8080 default_server;
        	listen [::]:8080 default_server ipv6only=on;

        	root /usr/share/nginx/html;
        	index index.html index.htm;

        	# Make site accessible from http://localhost/
        	server_name localhost;

        	location / {
                	# First attempt to serve request as file, then
                	# as directory, then fall back to displaying a 404.
                	try_files $uri $uri/ =404;
                	# Uncomment to enable naxsi on this location
                	# include /etc/nginx/naxsi.rules
        	}
	```

* This is what's keeping the Nginx installation from listening on port 80
