## Load Balancer

- Distributes load across multiple servers.
- This  distribution ensures reliability, efficiency and availability of the applications.

---

### Context

- A continuation of [0x0C-web_server](https://github.com/R-Owino/alx-system_engineering-devops/tree/master/0x0C-web_server) project, I have now been given 2 additional servers:
	* gc-[STUDENT_ID]-web-02-XXXXXXXXXX
	* gc-[STUDENT_ID]-lb-01-XXXXXXXXXX
- The web stack has been improved so that there is redundancy for our web servers. This allows us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

---

### Resources

- [Introduction to load-balancing and HAproxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts)
- [HTTP header](https://www.techopedia.com/definition/27178/http-header)
- [Debian/Ubuntu HAProxy packages](https://haproxy.debian.net/)
