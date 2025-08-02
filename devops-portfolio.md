
# 🛠️ DevOps Portfolio – Muhammed Fahmi

Welcome! This repository is a summary of my hands-on experience in DevOps, showcasing the tools and practices I applied across several personal projects. This is not a code showcase but rather a documentation of what I’ve built and learned.

---

## 🧠 Skills and Tools I’ve Worked With

- **Operating Systems:** Linux (Ubuntu, Raspberry Pi OS), macOS
- **Version Control:** Git, GitHub
- **Containerization:** Docker, Docker Compose
- **CI/CD:** GitHub Actions
- **Web Servers & Reverse Proxies:** Nginx
- **Databases:** Oracle XE (via Docker)
- **Networking:** VPN (WireGuard), Port Forwarding, DDNS, Firewall Rules
- **Frontend Dev:** HTML, CSS, JavaScript (basic)
- **Backend Dev:** Python, Flask
- **Others:** Cloudflare (DDNS), VS Code (Remote SSH/Docker Dev)

---

## 🚀 Projects & What I Used

### 📦 Home Network Monitor

> A DevOps-style monitoring system running on Raspberry Pi and Docker.

**Tools & Tech:**
- Docker & Docker Compose
- Python Flask API
- Oracle XE as database
- CI/CD: GitHub Actions (build, test, push images)
- Mac Mini as dev environment / Raspberry Pi as production
- Cloudflare DDNS + WireGuard/for remote access

---

### 🌐 Personal Website

> Static frontend + Flask backend + Dockerized Oracle DB

**Tools & Tech:**
- HTML/CSS + JS for frontend
- Flask API for backend
- Oracle XE DB (via Docker container)
- Nginx as reverse proxy
- Docker Compose for multi-container setup
- CI pipeline with GitHub Actions
- Testing locally on Mac Mini, deploying on Raspberry Pi

---

### 🛡️ Remote Access with WireGuard VPN

> Set up secure remote access to my home network using WireGuard and Raspberry Pi.

**Tools & Tech:**
- WireGuard VPN (configured on Raspberry Pi using PiVPN)
- Cloudflare DDNS for dynamic IP
- TP-Link Omada ER605 router: port forwarding & firewall configuration
- Raspberry Pi used as a VPN gateway

**Challenges & Solutions:**
- ❗ **Handshake failure** due to wrong port/NAT config ➜ ✅ Fixed by correcting port forwarding on TP-Link Omada router
- ❗ **No internet over VPN** ➜ ✅ Resolved with proper routing config (`AllowedIPs` and IP forwarding)
- ❗ **DDNS not updating** ➜ ✅ Used Cloudflare API script to automate DDNS updates

---

### 🔄 DevOps Learning Lab

> Simulated DevOps environment with microservices

**Tools & Tech:**
- Multiple microservices in Docker Compose
- Oracle DB containers
- Bash scripts for automation
- Separate test (Mac Mini) vs prod (Raspberry Pi) environments

---

## 🔗 Connect with Me

- LinkedIn: [linkedin.com/in/muhammedfahmi](https://www.linkedin.com/in/muhammedfahmi)

---

> 💡 *Feel free to reach out on LinkedIn if you’d like to discuss any of these projects or DevOps in general!*