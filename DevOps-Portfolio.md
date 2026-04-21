# DevOps Portfolio — Muhammed Fahmi

A summary of my hands‑on DevOps experience through personal and home‑lab projects. This is not a code showcase; it's a written record of what I built, the tools I used, and the problems I solved along the way.

> Looking for my work history? See [Professional Experience](./Professional-Experience.md).

---

## Table of Contents

- [Skills and Tools](#skills-and-tools)
- [Projects](#projects)
  - [Home Network Monitor](#home-network-monitor)
  - [Personal Website](#personal-website)
  - [Remote Access with WireGuard VPN](#remote-access-with-wireguard-vpn)
  - [DevOps Learning Lab](#devops-learning-lab)
- [Connect](#connect)

---

## Skills and Tools

| Category | Tools |
|---|---|
| Operating Systems | Linux (Ubuntu, Raspberry Pi OS), macOS |
| Version Control | Git, GitHub |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Web Servers & Reverse Proxies | Nginx |
| Databases | Oracle XE (via Docker) |
| Networking | WireGuard VPN, Port Forwarding, DDNS, Firewall Rules |
| Frontend (basic) | HTML, CSS, JavaScript |
| Backend | Python, Flask |
| Other | Cloudflare (DDNS), VS Code (Remote SSH / Dev Containers) |

---

## Projects

### Home Network Monitor

> A DevOps‑style monitoring system running on a Raspberry Pi with Docker.

**Stack**
- Docker & Docker Compose
- Python / Flask API
- Oracle XE as database
- GitHub Actions for build, test, and image publishing
- Mac Mini as dev environment, Raspberry Pi as production target
- Cloudflare DDNS + WireGuard for remote access

**What I learned**
- Splitting a system into dev vs. production environments while keeping the same container images.
- Running a CI/CD pipeline end‑to‑end on a home project without over‑engineering it.

---

### Personal Website

> Static frontend + Flask backend + Dockerized Oracle DB, fronted by Nginx.

**Stack**
- HTML / CSS / JavaScript frontend
- Flask API backend
- Oracle XE database in a Docker container
- Nginx as reverse proxy
- Docker Compose for multi‑container orchestration
- GitHub Actions CI pipeline
- Tested locally on Mac Mini, deployed on Raspberry Pi

---

### Remote Access with WireGuard VPN

> Secure remote access to my home network using WireGuard on Raspberry Pi.

**Stack**
- WireGuard VPN (configured on Raspberry Pi via PiVPN)
- Cloudflare DDNS for dynamic public IP
- TP‑Link Omada ER605 router: port forwarding & firewall configuration
- Raspberry Pi as the VPN gateway

**Challenges & Fixes**

| Problem | Root cause | Fix |
|---|---|---|
| Handshake failure | Wrong port / NAT configuration | Corrected port forwarding on the Omada router |
| No internet over VPN | Missing routing / IP forwarding | Configured `AllowedIPs` and enabled IP forwarding on the gateway |
| DDNS not updating | Dynamic IP changed, no updater running | Automated updates via a Cloudflare API script |

---

### DevOps Learning Lab

> A simulated DevOps environment to practice microservices, scripting, and multi‑environment workflows.

**Stack**
- Multiple microservices orchestrated with Docker Compose
- Oracle DB containers
- Bash scripts for setup and automation
- Separate test (Mac Mini) and prod (Raspberry Pi) environments

---

## Connect

- **LinkedIn:** [linkedin.com/in/muhammedfahmi](https://www.linkedin.com/in/muhammedfahmi)

> Feel free to reach out on LinkedIn if you'd like to discuss any of these projects or DevOps in general.
