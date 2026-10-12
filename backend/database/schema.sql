/*
AgentFin-Swarm Database Schema
*/


CREATE TABLE transactions (

    id SERIAL PRIMARY KEY,

    transaction_id VARCHAR(50),

    customer_id VARCHAR(50),

    risk_score FLOAT,

    fraud_score FLOAT,

    compliance_score FLOAT,

    final_score FLOAT,

    threat_level VARCHAR(20),

    evidence TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


CREATE TABLE experiment_results (

    id SERIAL PRIMARY KEY,

    model_name VARCHAR(100),

    accuracy FLOAT,

    precision_score FLOAT,

    recall_score FLOAT,

    f1_score FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);


CREATE TABLE agent_reputation (

    id SERIAL PRIMARY KEY,

    agent_name VARCHAR(50),

    reputation_score FLOAT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

);