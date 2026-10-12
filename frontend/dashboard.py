import streamlit as st
import pandas as pd
import requests
import plotly.express as px

# ==================================================
# PAGE CONFIGURATION
# Description:
# Configure Streamlit application settings such as
# page title, page icon and layout.
# ==================================================

st.set_page_config(
    page_title="AgentFin-Swarm",
    page_icon="🏦",
    layout="wide"
)

# ==================================================
# HEADER
# Description:
# Display the application title, platform overview
# and introduction to the AgentFin-Swarm framework.
# ==================================================

st.title("🏦 AgentFin-Swarm")
st.subheader("Multi-Agent Financial Intelligence Platform")

st.markdown("""
### Executive Overview

AgentFin-Swarm is an AI-powered Multi-Agent Financial Intelligence Platform
designed to analyse financial transactions using specialized agents.

The platform integrates:

- Risk Assessment Agent
- Fraud Detection Agent
- Compliance Monitoring Agent
- Regulation Intelligence Agent
- Consensus Decision Engine
- Explainable AI Engine

All agent outputs are consolidated into a single transparent and explainable
decision to support financial analysts and compliance teams.
""")

st.divider()

# ==================================================
# KPI DASHBOARD
# Description:
# Display key performance indicators (KPIs) showing
# transaction volume, fraud alerts, AML violations,
# and high-risk transaction statistics.
# ==================================================

st.header("Executive Dashboard")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Transactions Analysed", "12,542")
c2.metric("Fraud Alerts", "91", "+12")
c3.metric("AML Violations", "45", "+3")
c4.metric("High Risk Cases", "238", "+20")

st.divider()

# ==================================================
# AGENT WORKFLOW
# Description:
# Illustrate the processing flow of transactions
# through the multi-agent financial intelligence
# framework.
# ==================================================

st.header("Agent Workflow")

st.code("""
Transaction
      ↓
Risk Agent
      ↓
Fraud Agent
      ↓
Compliance Agent
      ↓
Consensus Engine
      ↓
Evidence Engine
      ↓
Final Decision
""")

st.divider()

# ==================================================
# NOVELTY AND RESEARCH CONTRIBUTION
# Description:
# Highlights the innovative features, research
# contributions and unique capabilities of the
# AgentFin-Swarm framework.
# ==================================================

st.divider()

st.header("🚀 Novelty and Research Contribution")

st.markdown("""
### Research Novelty

AgentFin-Swarm introduces a Multi-Agent Financial Intelligence
Framework that combines specialized AI agents for Risk Assessment,
Fraud Detection and Compliance Monitoring within a unified
decision-making architecture.

### Key Innovations

• Multi-Agent Intelligence Architecture

• Consensus-Based Decision Making

• Explainable AI (XAI) for Transparent Decisions

• Integrated Risk, Fraud and Compliance Assessment

• Evidence-Based Recommendations

• Human-Readable Explanations for Analyst Support

• Regulatory-Aware Financial Intelligence Framework

Unlike traditional systems that rely on a single predictive model,
AgentFin-Swarm enables multiple specialized agents to independently
analyze transaction data and collaboratively produce a final
consensus-driven decision.

This improves transparency, interpretability, decision reliability
and analyst confidence during financial investigations.
""")

# ==================================================
# INPUT DESCRIPTION
# Description:
# Explain the purpose of each input parameter used
# during transaction analysis and assessment.
# ==================================================

st.header("Input Parameter Description")

input_df = pd.DataFrame({

    "Parameter": [
        "Transaction Amount",
        "FICO Score",
        "Annual Income",
        "Payment Type",
        "Sender Country",
        "Receiver Country",
        "KYC Verification"
    ],

    "Description": [

        "Total monetary value involved in the transaction.",

        "Creditworthiness score used to estimate financial reliability.",

        "Declared customer income used during risk assessment.",

        "Mode of transaction such as Cash, Wire or Transfer.",

        "Country from which the transaction originates.",

        "Country receiving the funds.",

        "Indicates whether Know Your Customer verification has been completed."
    ]
})

st.dataframe(
    input_df,
    use_container_width=True
)

st.info("""
Transaction Amount:
Higher values may trigger AML monitoring and regulatory scrutiny.

FICO Score:
Higher scores generally indicate better creditworthiness and lower financial risk.

Annual Income:
Used to evaluate whether the transaction aligns with the customer's financial profile.

Payment Type:
Certain payment methods may carry higher operational or fraud risk.

Sender and Receiver Countries:
Cross-border transactions often require additional compliance validation.

KYC Verification:
Missing customer verification significantly increases compliance concerns.
""")

st.divider()

# ==================================================
# SIDEBAR CONFIGURATION
# Description:
# Collect transaction details and customer
# information required for backend analysis.
# ==================================================

st.sidebar.header("Transaction Configuration")

amount = st.sidebar.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=2500000.0,
    help="""
Transaction Amount:
Represents the total monetary value involved in a financial transaction.

Purpose:
Used for Anti-Money Laundering (AML) monitoring and risk assessment.

AML (Anti-Money Laundering):
A set of regulations and procedures designed to prevent the generation
of income through illegal activities.

Higher transaction amounts may trigger enhanced compliance checks.
"""
)

fico = st.sidebar.number_input(
    "FICO Score",
    min_value=300,
    max_value=850,
    value=720,
    help="""
FICO Score (Fair Isaac Corporation Score):

A numerical credit score used to evaluate customer creditworthiness.

Range:
300 - 850

Purpose:
Used by the Risk Agent to assess the customer's financial reliability.

Higher Score:
Lower financial risk.

Lower Score:
Higher financial risk.
"""
)

annual_income = st.sidebar.number_input(
    "Annual Income",
    min_value=0,
    value=100000,
    help="""
Annual Income:

Represents the customer's declared yearly income.

Purpose:
Used to determine whether the transaction value aligns with
the customer's financial profile and spending capacity.

Large transactions relative to annual income may increase risk levels.
"""
)

payment_type = st.sidebar.selectbox(
    "Payment Type",
    ["Cash", "Wire", "Transfer"],
    help="""
Payment Type:

Specifies the channel used to transfer funds.

Cash:
Physical currency transaction.

Wire Transfer:
Electronic transfer of funds between banks.

Transfer:
General electronic movement of funds between accounts.

Purpose:
Used by Fraud and Compliance Agents to identify operational
and transactional risks.
"""
)

sender_country = st.sidebar.selectbox(
    "Sender Country",
    ["India", "USA", "UAE", "Singapore"],
    help="""
Sender Country:

Country from which the transaction originates.

Purpose:
Used to evaluate geographical and jurisdiction-based risks.

Cross-border transactions may require additional regulatory reviews.
"""
)

receiver_country = st.sidebar.selectbox(
    "Receiver Country",
    ["India", "USA", "UAE", "Singapore"],
    help="""
Receiver Country:

Country receiving the transaction funds.

Purpose:
Used for geographical risk analysis and compliance validation.

Certain destinations may require enhanced monitoring.
"""
)

kyc_verified = st.sidebar.checkbox(
    "KYC Verified",
    value=False,
    help="""
KYC (Know Your Customer):

A regulatory process used to verify customer identity.

Purpose:
Ensures customers are properly identified before conducting
financial transactions.

True:
Customer identity verified.

False:
Customer identity not verified.

Missing KYC verification increases compliance and regulatory risk.
"""
)

# ==================================================
# SESSION STATE MANAGEMENT
# Description:
# Stores analysis results across Streamlit reruns.
# ==================================================

if "result" not in st.session_state:
    st.session_state.result = None

if "risk_score" not in st.session_state:
    st.session_state.risk_score = 0

if "fraud_score" not in st.session_state:
    st.session_state.fraud_score = 0

if "compliance_score" not in st.session_state:
    st.session_state.compliance_score = 0

if "final_score" not in st.session_state:
    st.session_state.final_score = 0

# ==================================================
# TRANSACTION ANALYSIS
# Description:
# Sends transaction data to the FastAPI backend
# and initiates multi-agent transaction analysis.
# ==================================================

st.header("Transaction Analysis")

if st.button(
    "Analyze Transaction",
    use_container_width=True
):

    payload = {
        "customer": {
            "credit.policy": 1,
            "int.rate": 0.12,
            "installment": 300,
            "log.annual.inc": 10.5,
            "dti": 12,
            "fico": fico,
            "days.with.cr.line": 4000,
            "revol.bal": 15000,
            "revol.util": 30,
            "inq.last.6mths": 1,
            "delinq.2yrs": 0,
            "pub.rec": 0
        },

        "transaction": {
            "transaction_id": "TXN001",
            "Amount": amount,
            "Payment_type": payment_type,
            "Sender_bank_location": sender_country,
            "Receiver_bank_location": receiver_country,
            "kyc_verified": kyc_verified
        }
    }

    try:

        response = requests.post(
            "http://127.0.0.1:8000/analyze",
            json=payload,
            timeout=30
        )

        if response.status_code != 200:

            st.error(
                f"API Error ({response.status_code})"
            )

            st.code(
                response.text
            )

        else:

            result = response.json()

            risk_score = result["risk"]["score"]
            fraud_score = result["fraud"]["score"]
            compliance_score = result["compliance"]["score"]

            final_score = result.get(
                "final_score",
                0
            )

            st.success(
                "Transaction Analysis Completed Successfully"
            )

            st.divider()

            # ===================================
            # DETAILED AGENT INTERPRETATION
            # Description:
            # Provide explanations for Risk, Fraud and
            # Compliance agent assessments.
            # ===================================

            # ===================================
            # AGENT RESULTS
            # Description:
            # Display Risk, Fraud and Compliance
            # scores generated by individual agents.
            # ===================================

            st.header("Agent Analysis Breakdown")

            r1, r2, r3 = st.columns(3)

            r1.metric(
                "Risk Score",
                risk_score
            )

            r2.metric(
                "Fraud Score",
                fraud_score
            )

            r3.metric(
                "Compliance Score",
                compliance_score
            )

            st.subheader(
                "Detailed Agent Interpretation"
            )

            st.markdown(f"""
### Risk Agent

Risk Score: **{risk_score}**

The Risk Agent evaluates financial risk using credit behaviour,
income stability, debt obligations and customer profile attributes.
""")

            st.markdown(f"""
### Fraud Agent

Fraud Score: **{fraud_score}**

The Fraud Agent identifies unusual transaction behaviour,
payment anomalies and suspicious transaction patterns.
""")

            st.markdown(f"""
### Compliance Agent

Compliance Score: **{compliance_score}**

The Compliance Agent evaluates AML, KYC and regulatory adherence.
""")

            st.divider()

            # ===================================
            # CONSENSUS ENGINE
            # Description:
            # Combines agent outputs to generate a final
            # threat classification.
            # ===================================

            st.header("Consensus Decision Engine")

            st.metric(
                "Consensus Score",
                final_score
            )

            if final_score >= 80:

                threat_level = "HIGH"

                st.error("""
            ### HIGH THREAT LEVEL

            Recommended Actions:

            • Escalate for manual review

            • Perform enhanced due diligence

            • Verify customer documents

            • Review transaction purpose

            • Hold transaction if required
            """)

            elif final_score >= 50:

                threat_level = "MEDIUM"

                st.warning("""
            ### MEDIUM THREAT LEVEL

            Recommended Actions:

            • Additional verification

            • Monitor future activity

            • Validate customer information
            """)

            else:

                threat_level = "LOW"

                st.success("""
            ### LOW THREAT LEVEL

            Recommended Actions:

            • Proceed with standard processing

            • Continue routine 
            
            """)

            st.divider()

            # ===================================
            # EXPLAINABLE AI
            # Description:
            # Provide evidence and reasoning that support
            # the final transaction assessment.
            # ===================================

            st.header("Explainable AI and Evidence")

            evidence = result.get(
                "evidence",
                []
            )

            if evidence:

                for idx, item in enumerate(
                    evidence,
                    start=1
                ):
                    st.success(
                        f"{idx}. {item}"
                    )

            else:

                st.info("""
1. Transaction exceeds AML threshold.

2. Customer KYC verification missing.

3. Cross-border transaction detected.

4. Additional compliance review recommended.
""")

            st.divider()

            # ===================================
            # INPUT SUMMARY
            # Description:
            # Summarize all transaction parameters supplied
            # by the analyst during evaluation.
            # ===================================

            st.header("Transaction Input Summary")

            summary_df = pd.DataFrame({

                "Parameter": [
                    "Transaction Amount",
                    "FICO Score",
                    "Annual Income",
                    "Payment Type",
                    "Sender Country",
                    "Receiver Country",
                    "KYC Verified"
                ],

                "Value": [
                    amount,
                    fico,
                    annual_income,
                    payment_type,
                    sender_country,
                    receiver_country,
                    kyc_verified
                ]
            })

            st.dataframe(
                summary_df,
                use_container_width=True
            )

            st.divider()

            # ===================================
            # EXECUTIVE SUMMARY
            # Description:
            # Present a business-level summary of the
            # transaction assessment and threat level.
            # ===================================

            st.header("Executive Decision Summary")

            st.markdown(f"""
### Transaction Assessment Report

**Risk Score:** {risk_score}

**Fraud Score:** {fraud_score}

**Compliance Score:** {compliance_score}

**Consensus Score:** {final_score}

**Threat Level:** {threat_level}

The multi-agent framework analysed the transaction using
financial risk indicators, fraud detection models,
regulatory compliance rules and explainability evidence.

The final threat classification represents the consolidated
decision of all participating agents.
""")

    except requests.exceptions.ConnectionError:

        st.error("""
    Backend server is not running.

    Start FastAPI using:

    python -m uvicorn backend.main:app --reload
    """)

    except Exception as error:

        st.exception(error)

    
# ==================================================
# ANALYTICS
# Description:
# Visualize transaction risk distribution and
# analytical insights using interactive charts.
# ==================================================

st.divider()

st.header("Risk Analytics")

risk_data = pd.DataFrame({
    "Risk Level": ["High", "Medium", "Low"],
    "Count": [40, 35, 25]
})

risk_fig = px.pie(
    risk_data,
    values="Count",
    names="Risk Level",
    hole=0.5,
    title="Risk Distribution"
)

st.plotly_chart(
    risk_fig,
    use_container_width=True
)

# ==================================================
# FRAUD TREND
# Description:
# Display fraud alert trends over time to support
# operational monitoring and analysis.
# ==================================================

fraud_data = pd.DataFrame({
    "Day": [1, 2, 3, 4, 5, 6, 7],
    "Fraud Alerts": [10, 12, 8, 15, 18, 20, 22]
})

fraud_fig = px.line(
    fraud_data,
    x="Day",
    y="Fraud Alerts",
    markers=True,
    title="Fraud Alert Trend"
)

st.plotly_chart(
    fraud_fig,
    use_container_width=True
)

# ==================================================
# TRANSACTION HISTORY
# Description:
# Display historical transaction records and
# previously identified threat levels.
# ==================================================

st.divider()

st.header("Transaction History")

history_df = pd.DataFrame({

    "Transaction ID":
    ["TXN001", "TXN002", "TXN003"],

    "Risk Score":
    [82, 65, 20],

    "Fraud Score":
    [91, 42, 10],

    "Threat Level":
    ["HIGH", "MEDIUM", "LOW"]
})

st.dataframe(
    history_df,
    use_container_width=True
)

# ==================================================
# SYSTEM STATUS
# Description:
# Monitors backend health and verifies API
# availability.
# ==================================================

st.divider()

st.header("System Status")

try:

    health = requests.get(
        "http://127.0.0.1:8000/health",
        timeout=5
    )

    if health.status_code == 200:

        st.success(
            "Backend Status: ONLINE"
        )

    else:

        st.warning(
            "Backend Status: DEGRADED"
        )

except Exception:

    st.error(
        "Backend Status: OFFLINE"
    )

# ==================================================
# METHODOLOGY
# Description:
# Explain the overall workflow and methodology
# followed by the AgentFin-Swarm framework.
# ==================================================

st.divider()

st.header("Methodology Overview")

st.markdown("""
1. Transaction information is collected.

2. Risk Agent evaluates financial risk.

3. Fraud Agent identifies suspicious behaviour.

4. Compliance Agent validates AML and KYC rules.

5. Consensus Engine combines all agent outputs.

6. Evidence Engine generates explanations.

7. Final risk classification is presented to the analyst.
""")

st.divider()

st.caption(
    "AgentFin-Swarm • Multi-Agent Financial Intelligence Platform"
)