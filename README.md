# 🏦 Banking API - Test Automation Suite

A full-stack **API Test Automation Project** for a mock banking system, developed as part of an SDET internship preparation for **CRED**.

Built using **Flask**, **Pytest**, **Docker**, and **Jenkins**, this project demonstrates backend development, RESTful API automation, CI/CD integration, and containerized testing workflows.

---

## 📌 Features

### ✅ Core API Endpoints
| Method | Endpoint            | Description                      |
|--------|---------------------|----------------------------------|
| GET    | `/api/balance`      | Retrieve current balance         |
| POST   | `/api/deposit`      | Deposit funds                    |
| POST   | `/api/withdraw`     | Withdraw funds                   |
| POST   | `/api/accounts`     | Create a new account             |
| GET    | `/health`           | Health check of the API          |

---

## 🧪 Test Automation

- Written using `pytest` + `requests`
- Covers:
  - ✅ Valid and invalid deposits
  - ✅ Valid and edge-case withdrawals
  - ✅ Balance retrieval
  - ✅ Error handling for invalid inputs

---

## 🐳 Docker Setup

### 📁 Project Structure

.
├── app/
│ ├── init.py
│ └── routes/
│ ├── init.py
│ └── banking.py # Main API logic
├── tests/
│ └── test_banking_api.py # All automated test cases
├── main.py # Flask entrypoint
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile

---

### 🛠️ Build & Run

 in bash
#### Build Docker image
docker-compose build

#### Start Flask app
docker-compose up -d

#### Run tests inside container
docker exec -it banking_api pytest -v tests/

### ⚙️ Jenkins CI/CD Integration

✅ Pulls latest code from GitHub

✅ Builds the Docker image

✅ Runs pytest inside the container

✅ Health-check validation via curl

✅ Cleans up Docker on failure

Jenkinsfile is located in root and fully declarative.

### 📂 API Sample (via Postman / curl)

#### Health check
curl http://localhost:5000/health

#### Deposit funds
curl -X POST http://localhost:5000/api/deposit -H "Content-Type: application/json" -d '{"amount": 1000}'

### 📄 Technologies Used

Python 3.11

Flask

Pytest & Requests

Docker & Docker Compose

Jenkins

GitHub Actions (Optional CI)

Postman (for manual API testing)

💼 Why This Project?

This project demonstrates real-world backend testing workflows, built for demonstrating:

🔍 API automation skills

⚙️ CI/CD integration

🧪 Test coverage with assertions and edge cases

🐳 Docker containerization & debugging

🧠 SDET mindset: testing from a developer’s lens

📧 Author

Venkateswara Sahu
B.Tech CSE, Class of 2026
GitHub Profile

---
