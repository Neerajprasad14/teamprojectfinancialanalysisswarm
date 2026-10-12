# AgentFin-Swarm

## Multi-Agent Financial Intelligence Platform

AgentFin-Swarm is an AI-powered Multi-Agent Financial Intelligence Framework designed to analyze financial transactions using specialized agents for:

- Risk Assessment
- Fraud Detection
- Compliance Monitoring
- Regulatory Intelligence
- Consensus-Based Decision Making
- Explainable AI (XAI)
- Real-Time Transaction Processing
- Database-Backed Auditability

---

# Project Overview

Traditional financial intelligence systems often rely on a single decision-making model. AgentFin-Swarm introduces a collaborative Multi-Agent Architecture where independent agents evaluate transactions from different perspectives and collectively generate a transparent, explainable, and consensus-driven decision.

## Core Components

- Risk Agent
- Fraud Agent
- Compliance Agent
- Coordinator Agent
- Consensus Engine
- Evidence Engine
- Regulatory Intelligence Module
- PostgreSQL Repository Layer
- FastAPI Service Layer
- Streamlit Dashboard

---

# Key Features

✅ Multi-Agent Intelligence

✅ Consensus-Based Transaction Assessment

✅ Explainable AI (XAI)

✅ AML & KYC Compliance Monitoring

✅ PostgreSQL Integration

✅ Real-Time Transaction Processing

✅ Regulatory Intelligence

✅ Transaction Audit Trail

✅ Scalable Modular Architecture

✅ Digital Twin-Based Evaluation

---

# Project Structure

```text
AgentFin-Swarm/
│
├── backend/
│   ├── agents/
│   ├── database/
│   ├── models/
│   ├── services/
│   ├── streaming/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── dashboard.py
│   └── requirements.txt
│
├── datasets/
│
├── experiments/
│   ├── centralized_model.py
│   ├── swarm_model.py
│   ├── digital_twin_test.py
│   ├── performance_benchmark.py
│   ├── resilience_test.py
│   ├── statistical_test.py
│   └── generate_graphs.py
│
├── tests/
│
├── docker/
│
├── docs/
│
└── README.md
```

---

# Technology Stack

## Frontend

- Streamlit
- Plotly
- Pandas

## Backend

- FastAPI
- Uvicorn
- PostgreSQL
- Psycopg
- Pydantic

## Analytics & Experiments

- Scikit-Learn
- NumPy
- SciPy
- StatsModels
- Matplotlib
- Seaborn
- NetworkX

---

# Prerequisites

Install the following software before running the application:

- Python 3.11+
- PostgreSQL
- pgAdmin (Optional)
- Visual Studio Code (Recommended)

---

# Environment Setup

Create:

```text
backend/.env
```

Contents:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/agentfin

AML_LIMIT=1000000

KYC_REQUIRED=True

RISK_THRESHOLD=80

FRAUD_THRESHOLD=85
```

---

# Installation

## Clone Repository

```bash
git clone <repository-url>

cd AgentFin-Swarm
```

---

## Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

---

## Install Frontend Dependencies

```bash
pip install -r frontend/requirements.txt
```

---

# PostgreSQL Setup

## Create Database

```sql
CREATE DATABASE agentfin;
```

---

## Test Database Connection

```bash
python -m backend.database.test_connection
```

Expected Output:

```text
Database Connected Successfully.
```

---

## Create Database Tables

```bash
python -m backend.database.init_db
```

Expected Output:

```text
Database tables created successfully.
```

---

# Running the Application

## Start Backend API

```bash
python -m uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

## Start Frontend Dashboard

```bash
streamlit run frontend/dashboard.py
```

Dashboard URL:

```text
http://localhost:8501
```

---

# API Documentation

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Available Endpoints

```http
GET     /health

POST    /risk

POST    /fraud

POST    /compliance

GET     /regulations

POST    /analyze

GET     /transactions
```

---

# API Examples

## Health Check

### Request

```http
GET /health
```

### Response

```json
{
  "service": "AgentFin-Swarm",
  "status": "Healthy",
  "database": "Connected"
}
```

---

## Compliance Analysis

### Request

```json
{
  "transaction": {
    "amount": 2500000,
    "kyc_verified": false
  }
}
```

### Response

```json
{
  "agent": "ComplianceAgent",
  "violations": [
    "AML_THRESHOLD_EXCEEDED",
    "KYC_MISSING"
  ],
  "score": 80,
  "confidence": 0.9
}
```

---

## Full Swarm Analysis

### Request

```json
{
  "customer": {
    "customer_id": "CUS001",
    "income": 500000,
    "credit_score": 720
  },
  "transaction": {
    "transaction_id": "TXN001",
    "amount": 2500000,
    "country": "UAE",
    "kyc_verified": false
  }
}
```

### Response

```json
{
  "risk": {
    "score": 82
  },
  "fraud": {
    "score": 91
  },
  "compliance": {
    "score": 80
  },
  "final_score": 84.3
}
```

---

# Transaction Persistence Verification

## Retrieve Transactions

### Request

```http
GET /transactions
```

### Response

```json
[
  {
    "id": 1,
    "transaction_id": "TXN001",
    "customer_id": "CUS001",
    "final_score": 84.3
  }
]
```

---

# Streaming Simulation

Run:

```bash
python -m backend.streaming.run_stream
```

Expected Output:

```text
Processing TXN001

Processing TXN002
```

---

# Execution Flow

```text
Customer Transaction
          │
          ▼

Coordinator Agent
          │
          ▼

Risk Agent
Fraud Agent
Compliance Agent
          │
          ▼

Consensus Engine
          │
          ▼

Evidence Engine
          │
          ▼

Repository Layer
          │
          ▼

PostgreSQL Database
          │
          ▼

FastAPI Services
          │
          ▼

Streamlit Dashboard
```

---

# Experiments Module

The Experiments Module is used to validate, benchmark and evaluate the proposed multi-agent framework.

## Experiment Files

### centralized_model.py

Implements a traditional centralized financial intelligence model used as a baseline for comparison.

### swarm_model.py

Implements the proposed Multi-Agent Swarm Intelligence architecture.

### digital_twin_test.py

Creates a digital twin environment for realistic simulation and validation.

### performance_benchmark.py

Measures response time, throughput and scalability.

### resilience_test.py

Evaluates robustness and fault tolerance under failures and disruptions.

### statistical_test.py

Performs statistical analysis on experimental results.

### generate_graphs.py

Generates charts, visualizations and comparative performance reports.

---

# Research Novelty

AgentFin-Swarm introduces a collaborative Multi-Agent Financial Intelligence Framework where specialized agents independently evaluate financial transactions and collectively generate a consensus-driven decision.

## Novel Contributions

- Multi-Agent Financial Intelligence Architecture
- Consensus-Based Decision Making
- Explainable AI for Financial Risk Assessment
- Integrated Risk, Fraud and Compliance Analysis
- Regulatory Intelligence Integration
- Digital Twin-Based Evaluation Framework
- Resilience-Aware Financial Analytics
- Database-Backed Auditability
- Modular Enterprise Architecture

---

# Verification Checklist

```text
✅ PostgreSQL Installed

✅ Database Created

✅ Environment Variables Configured

✅ Database Connection Successful

✅ Tables Created

✅ Backend Dependencies Installed

✅ Frontend Dependencies Installed

✅ FastAPI Running

✅ Streamlit Dashboard Running

✅ Swagger UI Accessible

✅ Risk Agent Operational

✅ Fraud Agent Operational

✅ Compliance Agent Operational

✅ Consensus Engine Working

✅ Swarm Analysis Working

✅ Transactions Persisted

✅ PostgreSQL Integration Verified

✅ Streaming Module Operational

✅ Experimental Evaluation Completed
```

---

# Startup Commands

```bash
cd AgentFin-Swarm

pip install -r backend/requirements.txt

pip install -r frontend/requirements.txt

python -m backend.database.test_connection

python -m backend.database.init_db

python -m uvicorn backend.main:app --reload

streamlit run frontend/dashboard.py
```

---

# System Architecture

```text
┌─────────────────────┐
│    FastAPI Layer    │
└──────────┬──────────┘
           │
           ▼

┌─────────────────────┐
│ Coordinator Agent   │
└──────────┬──────────┘
           │

 ┌─────────┼──────────┐
 ▼         ▼          ▼

Risk     Fraud    Compliance
Agent    Agent      Agent

 └─────────┼──────────┘
           ▼

  Consensus Engine
           │
           ▼

   Evidence Engine
           │
           ▼

 PostgreSQL Database
           │
           ▼

 Dashboard / Reports
```

---

# Future Enhancements

- Agent Memory Systems
- Kafka-Based Real-Time Streaming
- LLM-Powered Regulatory Intelligence
- Multi-Currency Transaction Analysis
- Automated Report Generation
- Dashboard Alert Notifications
- Agent Confidence Scoring
- Cloud Deployment (Azure/AWS/GCP)

---

# License

This project is developed for academic research and educational purposes as part of the M.Tech research work on Multi-Agent Financial Intelligence Systems.