Im going to explain about the infrastructure i use to build the above one server
that host the website that is reachable via www.foobar.com.
in this file im going to explain every components and theirr fanctionality and 
how they are performing certain tasks
1/What is a server?
server is a software or hardware component which help me to serve/provide certain functionality
for a certain program. those program can be web, application, database or file.
when you came to the above diagram....
the server responsible for hosting all components of the above web infrastructure
it contains:- monitor/computer, web server, application server, Database server and application file server
monitor:- is one type of serve which accept a DN (Domain name) command from user through a browser(www.footbar.com)
	DN:- domain name is human readeble name for specific Ip adress which help human to access easly
	DNS:- domain name system is a system which help to convert a given domain name into Ip address
	type of DNS in www.footbar.com is a CNAME record, which stands for Canonical Name
load-balancer (HAproxy):- Distributes incoming traffic across multiple backend servers
	 (Server 1 and Server 2) for load balancing. Acts as a single entry point for clients,
	 distributing requests based on predefined rules
web server(Nginx):-  serves as the front-facing server handling HTTP requests from clients.
	it reseive web request through http and process the reqiuest either static or daynamic
	if it dynamic it will pass the request to the applicatio server or if it is static it will
	response the file from the application file.
Application Server:- it's responsible for executing the application's business logic and generating dynamic content.
	in this server we deploy our code and process our request and give response
Application Files (Codebase): Contains the source code of the website
	It's deployed on the application server and executed upon receiving requests.
Database (MySQL): it is database management system. which help to store
	and manages the website including user information, content, etc.
		Communication among the web infrastructures:-
1. When a user requests www.foobar.com, their computer sends an HTTP request over the internet.
2. DNS resolves www.foobar.com to the server's IP address (8.8.8.8 in this case).
3. load balancer(HAproxy): Distributes incoming traffic across multiple backend servers
4. Nginx, acting as the web server, processes the request.
5. Static content is served directly, while dynamic requests are forwarded to the application server.
6. The application server executes the appropriate codebase to generate the dynamic content.
7. If necessary, the application server interacts with the MySQL database to retrieve or store data.
8. The generated content is sent back to the user's computer as an HTTP response.

		specific explanation
Load Balancer Algorithm:
	HAproxy is configured with a Round Robin distribution algorithm.
	This algorithm routes each new request to the next server in line,
	distributing the load evenly among available backend servers.
Active-Active vs. Active-Passive Setup:
	:-The load balancer enables an Active-Active setup.
	:-In an Active-Active setup, all servers actively handle requests simultaneously,
	distributing the load evenly across them.
	:-an Active-Passive setup involves one server actively handling requests
	while the others remain on standby, only becoming active if the primary server fails.
Database Primary-Replica Cluster:
	In a Primary-Replica cluster, the Primary node handles write operations 
	(e.g., INSERT, UPDATE, DELETE), while Replica nodes (Slaves) replicate 
	data from the Primary node for read operations.

		Difference between primary and secondary replica
	
	:-The Primary node handles write operations, meaning it's responsible for updating the 
	database with new data or changes initiated by the application.
	:-The Replica nodes primarily handle read operations, serving as backup copies of the data 
	and relieving the Primary node's load by handling read queries from the application.

Issues with this Infrastructure:
	Single Points of Failure (SPOF):
		Each component represents a potential single point of failure. If any of these 
		components fail, it could lead to downtime for the website.
	Security Issues:
		Lack of firewall configurations leaves the infrastructure vulnerable to unauthorized access and attacks.

	No Monitoring:
		Without monitoring tools or systems in place, it's challenging to identify performance issues, security 
		breaches, or infrastructure failures in real-time, leading to potential downtime or degraded performance.
