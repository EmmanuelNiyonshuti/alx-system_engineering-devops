			0x09. Web infrastructure design
This project delves into the fundamentals of web infrastructure design, providing a comprehensive understanding of various technologies and concepts crucial for building robust and scalable systems. Through the tasks, I gained insights into the roles and importance of web servers and application servers in serving web content and processing dynamic requests efficiently. Additionally, I explored the significance of load balancers in distributing incoming traffic across multiple servers to ensure high availability and fault tolerance. Understanding the difference between HTTP and HTTPS protocols, as well as the importance of SSL/TLS certificates, highlighted the critical aspects of securing web communications and protecting sensitive data from unauthorized access. Moreover, the inclusion of firewalls elucidated the role of network security measures in safeguarding against potential threats and vulnerabilities. Furthermore, the emphasis on monitoring tools underscored the significance of real-time performance monitoring and proactive management to identify and mitigate issues promptly, ensuring optimal system performance and uptime. Overall, this project provided invaluable insights into the core technologies and best practices essential for designing resilient and scalable web infrastructures.

Tasks Overview

0. Simple Web Stack
Description: Design a one-server web infrastructure hosting a website reachable via www.foobar.com.
Diagram File: 0-simple_web_stack.png
Key Components:
1 server
1 web server (Nginx)
1 application server
1 application code base
1 database (MySQL)
Specifics and Issues Explained:
Server role and domain name usage
DNS record type for www.foobar.com
Roles of web server, application server, and database
Communication between server and user's computer
Single Point of Failure (SPOF) and downtime issues during maintenance

1. Distributed Web Infrastructure
Description: Design a three-server web infrastructure hosting www.foobar.com.
Diagram File: 1-distributed_web_infrastructure.png
Key Components:
2 servers
1 web server (Nginx)
1 application server
1 load balancer (HAproxy)
1 application code base
1 database (MySQL)
Specifics and Issues Explained:
Additional elements added and their purpose
Load balancer distribution algorithm and setup type
Primary-Replica database cluster setup and application implications
SPOF, security, and monitoring issues

2. Secured and Monitored Web Infrastructure

Description: Design a three-server web infrastructure hosting www.foobar.com with security measures and monitoring.
Diagram File: 2-secured_and_monitored_web_infrastructure.png
Key Components:
3 firewalls
1 SSL certificate for HTTPS
3 monitoring clients (Sumologic or other)
Specifics and Issues Explained:
Purpose of added elements
Use of firewalls, HTTPS, and monitoring
SSL termination, MySQL writes, and server component homogeneity issues

3. Scale Up
Description: Design a scalable web infrastructure with split components and load balancing.
Diagram File: 3-scale_up.png
Key Components:
1 server
1 load balancer (HAproxy) configured as a cluster
Split components with separate servers for web server, application server, and database
Specifics:
Explanation for additional elements and their purpose


AUTHOR:
NIYONSHUTI Emmanuel