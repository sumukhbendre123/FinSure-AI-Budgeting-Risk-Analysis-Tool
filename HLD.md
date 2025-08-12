# FinSure – High Level Design (HLD)

## 📌 Overview
**FinSure** is an AI-enabled personal budgeting and risk-analysis platform that:
- Ingests bank transactions via **third-party banking APIs**
- Creates **category-based budgets** and **forecasts**
- Presents **interactive dashboards** and **savings goals**

## Tech Stack
- **Frontend:** React, Chart.js, Tailwind CSS  
- **Backend:** Python, Django, Django REST Framework  
- **Database:** MySQL  
- **Auth & Security:** Firebase Auth, JWT, OTP  
- **APIs:** Third-party banking API (Setu) (OAuth/REST)  
- **Hosting:** AWS / GCP (Load Balancer, EC2, RDS, S3)

---
# 🎯 Goals & Non-Functional Requirements

## ✅ Functional Goals
1. **Import Transaction History**  
   - Connect to supported banking APIs.  
   - Normalize and label transactions for consistency.  

2. **Budgeting & Analysis**  
   - Provide category-based budget suggestions.  
   - Offer trend analysis and proactive risk alerts.  

3. **Secure User Authentication & Authorization**  
   - OTP-based onboarding.  
   - JWT-based session management.  

4. **Interactive Dashboards**  
   - Display goals, forecasts, and risk metrics.  
   - Provide real-time updates where possible.

---

## ⚙️ Non-Functional Requirements

### 🔐 Security & Privacy
- PCI-aligned handling of financial data.  
- Encryption at rest and in transit (TLS, AES-256).  

### 📈 Availability
- Target **99.9% uptime** for core services: authentication, transaction sync, and dashboards.  

### 📊 Scalability
- Support user growth from **10k → 1M users**.  
- Stateless service architecture with **horizontal scaling**.

### ⚡ Latency
- Dashboard interactions: **< 300ms** for cached data.  
- Heavier analytics tasks processed asynchronously.

### 📜 Compliance & Auditability
- Retain transaction history as per regulatory requirements.  
- Maintain audit logs and track user consent.

## 🏗 Architectural Diagram

<img src="https://github.com/user-attachments/assets/1e74206c-8a31-4c94-ace4-3b6e2ae4967d" alt="FinSure Architecture" width="700" height="900">

## 3. Core Components

### 3.1 Frontend (React + Chart.js)
- Responsive web interface for user interaction.  
- Visualizes spending trends, budget progress, and risk metrics using interactive charts.  
- Communicates with backend APIs via HTTPS.  

### 3.2 Backend Services (Django + Django REST Framework)
- Acts as the primary API layer for the frontend.  
- Manages transaction processing, AI budget categorization, and savings recommendations.  
- Integrates with banking APIs to fetch and update transaction data.  

### 3.3 Banking API Integration Layer
- Connects to third-party banking APIs via secure OAuth or token-based authentication.  
- Normalizes transaction data into a consistent internal format.  

### 3.4 AI Budgeting & Risk Analysis Engine
- Categorizes expenses using predefined rules and AI classification models.  
- Generates personalized budget suggestions based on historical spending patterns.  
- Performs risk analysis by evaluating spending-to-income ratios and forecasting potential shortfalls.  

### 3.5 Database Layer (MySQL)
- Stores user profiles, transaction history, categorized budgets, and AI-generated recommendations.  
- Implements encryption at rest for sensitive fields.  

### 3.6 Authentication & Security
- User authentication handled via Firebase Auth.  
- OTP verification for login and sensitive actions.  
- JWT tokens for secure API calls.  
- All data transfers encrypted using TLS.  

---

## 4. Data Flow

**1. User Login**
- User logs in via Firebase Auth with OTP verification.  
- Backend issues a JWT token upon successful authentication.  

**2. Transaction Fetching**
- Frontend requests transaction data via Django APIs.  
- Backend calls third-party banking APIs securely and stores normalized data in MySQL.  

**3. AI Categorization & Recommendations**
- Transaction data sent to the AI engine for categorization and risk assessment.  
- Budget suggestions stored in the recommendation database.  

**4. Dashboard Rendering**
- Frontend fetches processed data from backend APIs.  
- Chart.js visualizes expense breakdowns, savings progress, and forecast trends.  

---

## 5. Non-Functional Requirements (NFRs)
- **Scalability:** Backend services horizontally scalable using container orchestration (Kubernetes/Docker).  
- **Security:** End-to-end encryption, secure API access, and compliance with data privacy standards (e.g., GDPR).  
- **Performance:** API responses under 300ms for typical queries.  
- **Reliability:** 99.9% uptime target with monitoring and logging.  



  

