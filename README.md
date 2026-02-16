# SR 11-7 Model Risk Management (MRM) System

### Quantitative Risk, Validation, Monitoring and Governance Platform

---

## Project Overview

This repository contains a production-ready Model Risk Management (MRM) framework built according to the SR 11-7 regulatory guidelines. 


The system manages the full lifecycle of quantitative financial models, moving beyond simple back-testing to include independent validation, performance monitoring, and formal governance.


---

## Technical Stack

* **Risk Engine:** C++17 for high-performance portfolio aggregation and Monte Carlo simulations.
* **Statistical Validation:** Python 3.9+ utilizing SciPy and NumPy for hypothesis testing (Kupiec POF, Christoffersen).
* **Governance Backend:** Flask-based Model Inventory and API.
* **Monitoring Interface:** Vanilla JavaScript and Tailwind CSS for risk dashboards.
* **Data Management:** Immutable CSV-based logging to ensure a deterministic audit trail.

---

## Market Application and Regulatory Alignment

The architecture is designed to reflect the standards required by Tier-1 banks and asset managers to comply with global regulations:

* **SR 11-7 / OCC 2011-12:** Federal Reserve guidance on model risk management and independent oversight.
* **Basel III / IV:** Regulatory capital requirements and Value-at-Risk (VaR) back-testing standards.
* **Internal Audit:** Providing an automated framework for model inventory and lifecycle state transitions (Draft, Validated, Production, Retired).

---

## System Architecture

### Phase 1: Model Development (C++)

The First Line of Defense. This module calculates the core risk metrics without any validation logic to ensure a strict separation of duties.

* **Historical VaR:** Non-parametric calculation based on empirical P&L distribution.
* **Monte Carlo VaR:** Parametric simulation using 10,000+ iterations to forecast potential losses.
* **Data Output:** Results are exported as immutable snapshots to prevent unauthorized tampering.

### Phase 2: Independent Validation (Python)

The Second Line of Defense. This module independently challenges the outputs of the C++ engine.

* **Kupiec Proportion of Failures (POF):** A Chi-squared test to determine if the number of VaR breaches is statistically significant.
* **Basel Traffic Light System:** Categorizes model performance into Green, Yellow, or Red zones based on a 250-day rolling window.

### Phase 3: Monitoring and Drift Detection

Once a model is in production, this phase tracks its health in real-time.

* **Model Drift:** Detects when market volatility causes the model’s assumptions to fail.
* **Alerting:** Classifies model status as Healthy, Watch, or Escalate based on breach frequency.

### Phase 4: Governance and Audit

The final layer provides a centralized control center for model oversight.

* **Model Registry:** A definitive list of all models, owners, and current approval status.
* **Append-only Logs:** Every action, from a code update to a validation rejection, is recorded for auditors.

---

## Project Structure

```text
SR11_7_MRM_System/
├── risk_engine_cpp/      # Phase 1: C++ Risk Engine & Simulations
├── validation_python/    # Phase 2: Independent Statistical Validation
├── monitoring/           # Phase 3: Performance & Drift Detection
├── backend/              # Phase 4: Governance API & Model Registry
├── frontend/             # Phase 4: Risk Officer Dashboard
├── governance/           # Documentation, Approvals, & Audit Trails
└── data/                 # Input/Output Data (Immutable)

```

---

## Execution Instructions

1. **Compile the Risk Engine**
```bash
g++ -std=c++17 risk_engine_cpp/src/*.cpp -o risk_engine
./risk_engine

```


2. **Execute Validation and Monitoring**
```bash
python3 validation_python/validation_report.py
python3 monitoring/monitoring_report.py

```


3. **Start the Governance Portal**
```bash
cd backend
python3 app.py

```


Access the system at: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Summary of Results

| Metric | Value | Status |
| --- | --- | --- |
| 99% Historical VaR | 1500.00 | Pass |
| 99% Monte Carlo VaR | 2076.00 | Pass |
| Kupiec Test p-value | 0.45 | Accept |
| Basel Classification | Green Zone | Validated |

---

## Author

**Om Barot**
B.Tech IT (2026)
Focus: Quantitative Finance and Model Risk Management


---
