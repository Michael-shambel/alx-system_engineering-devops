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
Firewalls:
	Each server is equipped with a firewall to control incoming and outgoing network traffic, 
	providing an additional layer of security.
	help prevent unauthorized access, malicious attacks, and data breaches by filtering network
	traffic based on predefined rules.
SSL Certificate (HTTPS):
	SSL certificate is installed on the load balancer to enable HTTPS encryption for serving
	It protects sensitive information such as user credentials, payment details, and personal
	data from eavesdropping and tampering.
Monitoring Clients:
	Monitoring clients are deployed on each server to collect performance metrics, logs, and other relevant data.
	essential for detecting and diagnosing issues, optimizing performance, ensuring compliance, and making informed 
	decisions about infrastructure management and scaling.
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
Firewalls:
        Each server is equipped with a firewall to control incoming and outgoing network traffic,
        providing an additional layer of security.
        help prevent unauthorized access, malicious attacks, and data breaches by filtering network
        traffic based on predefined rules.
SSL Certificate (HTTPS):
        SSL certificate is installed on the load balancer to enable HTTPS encryption for serving
        It protects sensitive information such as user credentials, payment details, and personal
        data from eavesdropping and tampering.
Monitoring Clients:
        Monitoring clients are deployed on each server to collect performance metrics, logs, and other relevant data.
        essential for detecting and diagnosing issues, optimizing performance, ensuring compliance, and making informed
        decisions about infrastructure management and scaling.
Issues with this Infrastructure:
	Terminating SSL at the Load Balancer Level:
		Terminating SSL at the load balancer level means that decrypted traffic is forwarded to 
		backend servers, potentially exposing sensitive data within the internal network.
	Single MySQL Server Accepting Writes:
		Having only one MySQL server capable of accepting writes creates a single point of failure
		for write operations.
		If the primary database server fails, it can result in data loss or service interruption 
		until the server is restored or failover mechanisms are activated.
	Uniformity of Server Components:
		Having servers with identical components might lead to homogeneity, making the entire 
		infrastructure vulnerable to the same types of failures or security breaches.
