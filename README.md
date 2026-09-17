# Docker Compose Networking Lab

A hands-on Linux, networking, Docker, and DevOps lab built using Ubuntu in VirtualBox.

## Technologies

- Ubuntu Linux
- Docker
- Docker Compose
- Nginx
- Git
- GitHub
- VirtualBox

## Architecture

Windows Host
    |
    | VirtualBox NAT
    |
Ubuntu Server
    |
    | Docker Compose
    |
Nginx Container
    |
    | Port 80
    |
Website

## Ports

| Service | Host Port | Container Port |
|--------|-----------|----------------|
| Apache | 8080 | 80 |
| SSH | 2222 | 22 |
| Nginx | 8081 | 80 |
| Docker Compose Nginx | 8082 | 80 |

## What I Practiced

- Linux command-line administration
- SSH remote administration
- UFW firewall configuration
- Network troubleshooting
- VirtualBox NAT and port forwarding
- Docker containers
- Docker port mapping
- Docker volumes
- Docker Compose
- Nginx
- Git version control
- GitHub
