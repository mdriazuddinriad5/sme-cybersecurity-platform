# Week 1 – Specification Refinement and Setup Decisions

## 1. Project Objective

The Part B implementation continues the Part A project:

**Development of an Intelligent Real-Time Cybersecurity Monitoring, Intrusion Detection and Risk Prioritisation Platform for SMEs**

The prototype is designed to help SMEs identify suspicious network activity and prioritise security alerts according to their potential organisational risk.

The core workflow remains:

**Monitor → Detect → Assess Risk → Prioritise → Alert → Human Investigation**

## 2. Scope Refinement

Following the Part A review, the project scope has been refined to keep the Part B prototype achievable.

### Included in the MVP

- Network-security event data ingestion
- Machine-learning-based intrusion detection
- Binary classification of Normal vs Attack traffic
- Contextual risk assessment
- Alert prioritisation
- Alert presentation through a lightweight interface
- Human review of generated alerts
- Logging of important system activities

### Outside the Initial MVP

- Full enterprise SOC functionality
- Automated attack remediation
- Physical security monitoring
- ISO 27001 certification or compliance auditing
- Employee security-awareness training
- Production deployment to a live SME network

These items remain outside the MVP because the Part B implementation period is limited and the project should prioritise a stable, testable prototype.

## 3. Dataset Decision

UNSW-NB15 was selected as the initial benchmark dataset for the intrusion-detection component.

The project uses the prepared training and testing datasets.

Initial modelling will focus on:

**Normal traffic vs Attack traffic**

Attack-category classification may be investigated later if the core binary detection pipeline performs reliably.

## 4. Architecture

The refined implementation architecture is:

**Dataset / Network Events → Data Processing → ML Intrusion Detection → Risk Assessment → Priority Calculation → Alert → Dashboard → Human Investigation**

Supporting components include:

- persistent data storage
- application logging
- access control
- system-health monitoring

Detection confidence and organisational risk will remain separate concepts. A high-confidence detection does not automatically mean that the event has the highest business risk.

## 5. Initial Technology Stack

- Python 3.12
- pandas for data ingestion and processing
- scikit-learn for the planned ML baseline
- FastAPI for the proposed backend API
- SQLite for initial persistent storage
- pytest for automated testing
- Git and GitHub for version control

## 6. Initial Non-Functional Requirements

The prototype should be:

- **Maintainable:** use modular Python components.
- **Testable:** core components should support automated testing.
- **Traceable:** important processing activities should be logged.
- **Secure:** sensitive information and credentials must not be hardcoded.
- **Usable:** alerts should be understandable to SME users.
- **Efficient:** the prototype should operate on ordinary computing hardware without requiring a dedicated GPU.

## 7. Week 1 Risks and Mitigation

### Dataset representativeness
UNSW-NB15 is a benchmark dataset and may not perfectly represent modern live SME network traffic.

**Mitigation:** Clearly document this limitation and avoid claiming that benchmark performance equals real-world SME performance.

### Class imbalance
Different attack categories have different numbers of records.

**Mitigation:** Later evaluation will consider precision, recall and F1-score rather than relying only on accuracy.

### Integration complexity
The complete project contains detection, risk assessment, prioritisation, persistence and dashboard components.

**Mitigation:** Follow an MVP-first implementation and integrate components incrementally.

### Sensitive security data
A real deployment could process sensitive network-security information.

**Mitigation:** Minimise stored information, avoid hardcoded credentials and introduce access-control mechanisms as the prototype develops.

## 8. Week 1 Implementation Status

Completed during the initial setup:

- Python development environment established
- Virtual environment created
- Required Python libraries installed
- Modular project folder structure created
- Initial CSV data loader implemented
- Application logging implemented
- Initial automated data-loader tests implemented
- UNSW-NB15 training and testing datasets acquired locally
- Training dataset successfully ingested and inspected
- Git repository created
- Initial project commit created and pushed to GitHub

The ML model, contextual risk engine and dashboard are not claimed as completed in Week 1. These components will be developed incrementally during the next implementation stages.