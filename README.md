# 🛡️ BlackVaultSystems

**BlackVaultSystems** is a high-security, full-stack modular platform designed for encryption, simulation, and deception. It includes three independent but integrated systems: secure messaging, a crypto escrow wallet, and a developer-facing admin decoy environment. All modules are real, production-grade, and hardened — built for developers, security engineers, and high-stakes environments.

---

## 🔧 Included Modules

### 1. `secure-messaging/`
A secure, end-to-end encrypted communication system supporting:
- PGP encryption (optional per message)
- Auto-delete options: 30 seconds, 24 hours, monthly, bi-monthly
- Fully stateless fallback if encryption is not used (message purging enforced)

### 2. `escrow-wallet/`
An escrow transaction UI with:
- Dynamic wallet ID generation
- QR code rendering and copy-to-clipboard
- Backend-safe — no direct chain interaction
- API-ready microservice (`/health`, `/wallet`) with optional QR integration

### 3. `admin-decoy-system/`
A high-interaction fake admin interface built to:
- Mimic real dev tools, settings panels, and API dashboards
- Mislead attackers into simulated environments
- Appear interactive, logged-in, and reactive (but never connected to a real backend)
- Waste time, create dead ends, and mirror live infrastructure

---

## ⚙️ Usage

### Run Locally (with Python or Node.js)
```bash
cd <module-folder>

# For secure-messaging or escrow-wallet
python3 app.py

# For admin-decoy-system
npm install
npm run dev
