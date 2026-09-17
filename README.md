# Docker Compose Networking Lab

A professional Linux, Docker, networking, and DevOps homelab project built on Ubuntu Server using Docker Compose.

The project demonstrates container networking, reverse proxying, backend-to-database communication, persistent storage, service health checks, infrastructure monitoring, and Git/GitHub workflow.

## Architecture

```text
Windows Host
     |
     | VirtualBox NAT
     |
Ubuntu Server
     |
     | Docker Compose
     |
     +-----------------------------+
     |                             |
     |                         Frontend Network
     |                             |
     |                         Nginx Container
     |                         /            \
     |                        /              \
     |                 Website             Backend API
     |                                      |
     |                                 Backend Network
     |                                      |
     |                         +------------+------------+
     |                         |            |            |
     |                    PostgreSQL   Prometheus     cAdvisor
     |                         |            |            |
     |                         |         Grafana         |
     |                         |                         |
     |                    Persistent Data         Container Metrics
     |                         
     +-----------------------------------------------+
```

## Technologies

* Ubuntu Server
* Docker
* Docker Compose
* Nginx
* Python
* PostgreSQL
* Prometheus
* Grafana
* cAdvisor
* Git
* GitHub
* VirtualBox
* UFW

## Project Structure

```text
docker-compose-lab/
│
├── README.md
├── compose.yaml
│
├── website/
│   └── index.html
│
├── nginx/
│   └── default.conf
│
├── backend/
│   ├── app.py
│   └── Dockerfile
│
├── database/
│   └── init.sql
│
└── monitoring/
    └── prometheus.yml
```

## Services

### Nginx

Nginx acts as the frontend web server and reverse proxy.

Responsibilities:

* Serves the static website
* Proxies requests to the Python backend
* Connects the frontend and backend Docker networks

### Python Backend API

A lightweight Python HTTP API running inside its own container.

The API:

* Provides a health endpoint
* Connects to PostgreSQL
* Retrieves service information from the database
* Returns JSON responses

### PostgreSQL

PostgreSQL provides the database layer for the application.

The database contains a `services` table with information about the services running in the lab.

PostgreSQL is not exposed directly to the Windows host. It is accessible through the internal Docker backend network.

### Prometheus

Prometheus collects infrastructure metrics from the monitoring stack.

The configuration includes monitoring targets for:

* Prometheus
* cAdvisor

### Grafana

Grafana provides visualization of the infrastructure metrics collected by Prometheus.

The dashboard includes monitoring for:

* Container CPU usage
* Container memory usage
* Network receive traffic
* Network transmit traffic
* Container availability

### cAdvisor

cAdvisor collects Docker container resource metrics and exposes them to Prometheus.

Metrics include:

* CPU usage
* Memory usage
* Network traffic
* Container status

## Docker Networking

The project uses two separate Docker bridge networks.

### Frontend Network

Used for communication between:

* Nginx
* Network testing container

### Backend Network

Used for communication between:

* Nginx
* Python backend
* PostgreSQL
* Prometheus
* Grafana
* cAdvisor

This separation demonstrates basic network segmentation inside Docker.

The Nginx container is connected to both networks, allowing it to act as the communication point between the frontend and backend layers.

## Health Checks

Docker Compose health checks are configured for the infrastructure services.

PostgreSQL uses `pg_isready` to verify database availability.

The Python backend uses its `/health` endpoint to verify that the API is responding.

The backend also depends on PostgreSQL becoming healthy before starting.

This demonstrates service dependency management and basic application health monitoring.

## Ports

| Service       | Ubuntu Port | Purpose                |
| ------------- | ----------: | ---------------------- |
| SSH           |          22 | Remote administration  |
| Apache        |          80 | Initial web server lab |
| Compose Nginx |        8082 | Main application       |
| cAdvisor      |        8080 | Container metrics      |
| Prometheus    |        9090 | Metrics and monitoring |
| Grafana       |        3000 | Monitoring dashboard   |

VirtualBox forwards selected Ubuntu ports to the Windows host.

Current Windows access includes:

| Service       | Windows Host Port |
| ------------- | ----------------: |
| SSH           |              2222 |
| Apache        |              8080 |
| Compose Nginx |              8082 |
| Prometheus    |              9090 |
| Grafana       |              3000 |

## Example Application Flow

A request to the application follows this architecture:

```text
Windows Browser
      |
      | HTTP
      v
VirtualBox Port Forwarding
      |
      v
Ubuntu Server
      |
      v
Nginx
      |
      | Reverse Proxy
      v
Python Backend
      |
      | SQL Query
      v
PostgreSQL
      |
      v
JSON Response
      |
      v
Nginx
      |
      v
Windows Browser
```

## Monitoring Flow

```text
Docker Containers
       |
       v
    cAdvisor
       |
       v
   Prometheus
       |
       v
     Grafana
       |
       v
Monitoring Dashboard
```

## Git Workflow

The project is version controlled using Git and hosted on GitHub.

Typical workflow:

```bash
git status
git add .
git commit -m "Update project"
git push
```

## What I Practiced

### Linux & System Administration

* Linux command-line administration
* SSH remote administration
* File and directory management
* Service troubleshooting
* UFW firewall configuration
* Network troubleshooting

### Networking

* TCP/IP fundamentals
* IP addressing
* Port forwarding
* NAT
* Docker bridge networking
* Container-to-container communication
* Internal Docker DNS
* Network segmentation

### Docker

* Docker containers
* Docker images
* Dockerfiles
* Docker port mapping
* Docker volumes
* Bind mounts
* Container health checks
* Docker networks
* Container troubleshooting

### Docker Compose

* Multi-container application deployment
* Service dependencies
* Persistent volumes
* Multiple networks
* Environment configuration
* Health checks
* Infrastructure orchestration

### Web & Backend

* Nginx web server
* Nginx reverse proxy
* Python HTTP API
* REST-style JSON responses
* PostgreSQL database integration
* Backend-to-database communication

### Monitoring

* Prometheus
* Grafana
* cAdvisor
* Container resource monitoring
* CPU monitoring
* Memory monitoring
* Network traffic monitoring
* Infrastructure dashboards

### DevOps & Version Control

* Git
* GitHub
* Infrastructure configuration
* Docker Compose deployment
* Documentation
* Troubleshooting and validation

## Security Considerations

This project is designed as a local homelab and learning environment.

The current configuration uses demonstration credentials directly in the Compose configuration and application code. In a production environment, these credentials should be moved to environment variables, Docker secrets, or another secure secrets-management solution.

The PostgreSQL database is kept on the internal Docker backend network rather than being directly exposed to the host.

## Future Improvements

Possible future improvements include:

* Moving credentials to `.env` or Docker secrets
* Adding automated health-check scripts
* Adding automated deployment with CI/CD
* Implementing configuration management
* Adding more advanced Prometheus alerting
* Expanding the network automation component

## Goal of the Project

The goal of this homelab is to combine Linux administration, computer networking, Docker, backend services, databases, monitoring, and DevOps practices into one practical infrastructure project.

It is designed as a portfolio project demonstrating hands-on experience with deploying, networking, monitoring, troubleshooting, and maintaining a multi-container environment.

