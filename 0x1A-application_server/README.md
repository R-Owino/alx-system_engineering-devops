## Application server

## Background Context
<p>From previous projects, the web infrastructure is already serving web pages via Nginx that was installed in the [first web stack](https://github.com/R-Owino/alx-system_engineering-devops/tree/master/0x0C-web_server) project. While a web server can also serve dynamic content, this task is usually given to an application server.</p> 
<p>In this project I will add this piece to the infrastructure, plug it to Nginx and make is serve the Airbnb clone project.</p>


## Resources
- [Application server vs web server](https://www.nginx.com/resources/glossary/application-server-vs-web-server/)
- [How to Serve a Flask Application with Gunicorn and Nginx on Ubuntu 16.04](https://www.digitalocean.com/blog/introducing-premium-cpu-optimized-droplets)
- [Running Gunicorn](https://docs.gunicorn.org/en/latest/run.html)
- [Be careful with the way Flask manages slash in route - strict_slashes](https://werkzeug.palletsprojects.com/en/0.14.x/routing/)
- [Upstart documentation](https://doc.ubuntu-fr.org/upstart)
