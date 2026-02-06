🏦 SR 11-7 Model Risk Management System

End-to-End Quantitative Risk, Validation, Monitoring \& Governance Platform

📌 Overview



This repository implements a production-grade Model Risk Management (MRM) system inspired by the SR 11-7 regulatory framework, covering the entire lifecycle of quantitative financial models:



Architecture → Model Development → Independent Validation → Ongoing Monitoring → Governance \& Audit



The project is designed as a final-year B.Tech capstone and is fully aligned with MSc Quantitative Finance / Financial Engineering expectations.



Unlike typical academic projects that stop at model computation, this system emphasizes model trustworthiness, statistical validation, monitoring, and governance — the core of real-world quantitative risk management.







🎯 Key Objectives



Build mathematically sound risk models



Enforce independent validation (no self-validation)



Detect model deterioration over time



Maintain auditability and governance discipline



Present results through a clean, minimal interface



Core insight:



In real quantitative finance, building the model is only a small part. Most of the work lies in validating, monitoring, and governing models.







🧠 Quantitative Concepts Explained (Beginner Friendly)

| Concept                 | Meaning                                                    | Where Implemented |

| ----------------------- | ---------------------------------------------------------- | ----------------- |

| \*\*VaR (Value at Risk)\*\* | Maximum expected loss over a horizon at a given confidence | Phase 2           |

| \*\*Historical VaR\*\*      | Empirical quantile of historical P\&L                       | Phase 2           |

| \*\*Monte Carlo VaR\*\*     | Parametric simulation using statistical assumptions        | Phase 2           |

| \*\*Backtesting\*\*         | Comparing predicted risk vs realized outcomes              | Phase 3           |

| \*\*Kupiec Test (POF)\*\*   | χ² test for VaR breach frequency                           | Phase 3           |

| \*\*Basel Traffic Light\*\* | Regulatory model performance classification                | Phase 3           |

| \*\*Model Drift\*\*         | Deterioration of model performance over time               | Phase 4           |

| \*\*Model Governance\*\*    | Ownership, approval, auditability                          | Phase 5           |





Phase 1 → Architecture \& Governance Design

Phase 2 → Risk Model Development (C++)

Phase 3 → Independent Validation (Python)

Phase 4 → Ongoing Monitoring \& Drift Detection

Phase 5 → Governance, Audit \& User Interface





Pillar 1 (Model Development) → C++ Risk Engine

Pillar 2 (Independent Validation) → Python Validation Engine

Pillar 3 (Ongoing Monitoring \& Governance) → Monitoring + Dashboard + Audit





🔢 Phase-by-Phase Breakdown



🔹 Phase 1 — Architecture \& Governance Foundation



Designed system structure before coding



Defined model lifecycle states



Created model inventory and audit framework



Enforced separation of responsibilities







🔹 Phase 2 — Risk Model Development (C++)



Models implemented:



Portfolio P\&L aggregation



Historical VaR (non-parametric)



Monte Carlo VaR (parametric simulation)



Design principles:



Deterministic outputs



Reproducible results



No validation logic inside the risk engine



Outputs written as immutable CSVs







🔹 Phase 3 — Independent Model Validation (Python)



Validation methods:



VaR backtesting



Kupiec Proportion of Failures test



Basel Traffic Light classification



Benchmark comparison between models



Key rule enforced:



Validation code never recalculates VaR — it only evaluates outputs from Phase 2.



Models are explicitly accepted or rejected based on statistical evidence.







🔹 Phase 4 — Ongoing Monitoring \& Drift Detection



Monitoring features:



Rolling breach windows (30 / 60 / 90 days)



Volatility and stability tracking



Alert classification (Healthy / Watch / Escalate)



Early-warning signals for deterioration



This phase answers:



“Is the model still behaving as expected today?”







🔹 Phase 5 — Governance, Audit \& User Interface



Governance features:



Model inventory with ownership and lifecycle state



Approval workflow



Append-only audit logs



Executive summaries



Interface:



Lightweight Flask backend



Minimal HTML/CSS/JavaScript dashboard



Upload-and-view functionality only



No recalculation or parameter changes via UI



This phase enables auditability without touching the models.





📁 Project Structure

SR11\_7\_MRM\_System/

├── risk\_engine\_cpp/        # Phase 2: C++ risk models

├── validation\_python/     # Phase 3: Independent validation

├── monitoring/            # Phase 4: Monitoring \& drift detection

├── backend/               # Phase 5: Flask governance backend

├── frontend/              # Phase 5: Dashboard UI

├── governance/             # Model registry, approvals, audit logs

├── data/                   # Immutable CSV inputs \& outputs

└── README.md





⚙️ How to Run (Local)

1️⃣ Compile and Run Risk Engine

g++ -std=c++17 risk\_engine\_cpp/src/\*.cpp -o risk\_engine

./risk\_engine



2️⃣ Run Independent Validation

python3 validation\_python/validation\_report.py



3️⃣ Run Monitoring

python3 monitoring/monitoring\_report.py



4️⃣ Launch Governance Dashboard

cd backend

python3 app.py





Access dashboard at:



http://127.0.0.1:5000







📊 Example End-to-End Results

Phase 2:

&nbsp; Historical VaR = 1500

&nbsp; Monte Carlo VaR = 2076



Phase 3:

&nbsp; Backtesting → Basel RED

&nbsp; Kupiec Test → Statistical rejection



Phase 4:

&nbsp; Rolling 30-day breaches = 1

&nbsp; Model Health = HEALTHY



Phase 5:

&nbsp; Dashboard reflects live status

&nbsp; Audit trail updated







🎓 Academic \& MSc Quant Relevance



This project demonstrates:



Mathematical modelling (risk \& probability)



Statistical hypothesis testing



Systems engineering



Risk-aware thinking



Regulatory discipline



Clean multi-language architecture (C++ / Python)









🚀 Potential Extensions



Expected Shortfall (CVaR)



GARCH-based volatility modelling



Multi-asset portfolios



Correlation modelling



Advanced drift detection methods



Real-time market data feeds







⚠️ Disclaimer



This is an academic implementation inspired by SR 11-7 guidance.

It is intended for educational and research purposes only and is not a certified regulatory system.







🏁 Final Note



This project shows that quantitative finance is not just about building models, but about:



validating them, monitoring them, governing them, and knowing when to reject them.





Author: OM BAROT

Degree: B.Tech IT (2026)

Focus: Quantitative Finance / Model Risk



