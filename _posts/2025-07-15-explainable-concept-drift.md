---
layout: post
title: "Explainable Concept Drift Using MLP-Based Non-Linear Causality | ICCCNT 2025"
date: 2025-07-15
author: Pradeep Pant
categories: [Research, Process Mining, Machine Learning]
tags: [Concept Drift, Process Mining, Causality, MLP, Explainable AI, IEEE, PhD]
excerpt: "Published at IEEE ICCCNT 2025, this work proposes an explainable framework for concept drift detection using MLP-based non-linear causal modeling in process mining."
---

# When Concept Drift Is More Than a Distribution Shift  
## Explaining Process Changes Using Non-Linear Causality

In July 2025, I presented my research paper titled:

**“Explainable Concept Drift in Process Mining Using MLP-Based Non-linear Causality Detection”**

at the **16th International IEEE Conference on Computing, Communication and Networking Technologies (ICCCNT 2025)** held at IIT Indore.

This work forms part of my ongoing PhD research in process mining, causal inference, and adaptive MLOps systems.

---

Machine learning models rarely fail dramatically.

They degrade quietly.

Accuracy drops slowly.  
Predictions become unstable.  
Business impact appears before monitoring dashboards raise alarms.

In process-driven systems — banking, manufacturing, healthcare — this degradation is often caused by **concept drift**.

But here’s the real issue:

Most systems can detect *that* something changed.  
Very few can explain *why* it changed.

This research focuses on closing that gap.

---

# The Limitation of Traditional Drift Detection

Most drift detection techniques rely on:

- Statistical change detection  
- Window-based distribution comparison  
- Linear Granger causality  
- Error monitoring  

These methods tell us:

> Something changed.

But they rarely tell us:

> What caused the change?

And critically, traditional Granger causality assumes **linear relationships**.

Real-world business processes are rarely linear.

- Workload impacts turnaround time in complex ways.  
- Customer attributes influence outcomes non-linearly.  
- Resource allocation interacts dynamically with control-flow behavior.  

Linear tools miss these hidden dependencies.

---

# Reframing Drift: A Change in Causal Structure

Instead of asking:

> Has the data distribution shifted?

I asked:

> Has the causal structure between process variables changed?

Event logs contain:

- **Primary features** → control-flow patterns  
- **Secondary features** → contextual attributes (age, workload, resource usage)

If contextual features begin influencing process behavior differently over time, that signals structural drift.

To capture this, the proposed framework combines:

- Process mining  
- Change point detection (PELT)  
- Non-linear causal modeling using MLP  
- Statistical validation via Wilcoxon test  

---

# The Core Idea

Two predictive models are trained:

**Model 1:**  
Uses only primary process features.

**Model 2:**  
Uses both primary and secondary contextual features.

If Model 2 significantly reduces prediction error (validated statistically), we infer:

> Contextual variables are causally influencing process behavior.

This transforms drift detection into **causal drift explanation**.

---

# Why MLP Instead of Linear Granger?

Traditional Granger causality detects only linear relationships.

However, real systems exhibit:

- Sinusoidal patterns  
- Exponential growth effects  
- Non-linear lag interactions  
- Multi-variable dependencies  

MLPs (Multilayer Perceptrons) naturally capture these complex patterns.

The framework:

- Uses lag-based time windows  
- Employs 2–3 hidden layers with ReLU activation  
- Applies dropout + early stopping  
- Evaluates using Mean Squared Error  
- Validates significance using Wilcoxon signed-rank test  

If contextual variables consistently improve predictive performance — and the improvement is statistically significant — we identify a causal influence.

---

# Experimental Validation

The framework was validated on:

### ✔ Synthetic CPI-generated datasets  
Controlled drift injection (sudden, gradual, recurring).

### ✔ BPI Challenge 2017 dataset  
31,000+ real loan application event logs.

### ✔ Large high-dimensional synthetic dataset  
Complex non-linear functions (sin, log, exp, sqrt) with injected drift.

Results showed:

- Consistent MSE reduction when contextual variables were included  
- Over 85% statistically significant improvements  
- Detection of non-linear dependencies missed by linear methods  
- Low false causal detection  

This demonstrates robustness, sensitivity, and statistical grounding.

---

# Why This Matters for Industry

In production ML systems, monitoring typically answers:

- Is performance degrading?
- Is data distribution changing?

But organizations need:

- What caused the degradation?
- Which contextual factors changed?
- Is the drift operational, behavioral, or structural?

This work moves toward:

> Drift Detection → Drift Explanation → Root-Cause Insight

This aligns strongly with my broader PhD direction on:

**Process-Mining–Driven Observability for Self-Adaptive MLOps Pipelines**

The long-term vision is to build ML systems that do not just detect failure — but understand structural change.

---

# Limitations & Future Work

- Fixed lag windows may miss dynamic temporal structures  
- Pairwise modeling limits multivariate causal discovery  
- Real logs lack ground-truth causal labels  
- Hyperparameter tuning remains critical  

Future directions include:

- Neural Granger frameworks  
- Transformer-based temporal modeling  
- Multivariate structural causal models  
- Online adaptive drift monitoring  

---

# Conference Presentation

This research was presented at:

**16th International IEEE Conference on Computing, Communication and Networking Technologies (ICCCNT 2025)**  
IIT Indore, July 6–11, 2025

You can view the presentation certificate below.

![ICCCNT 2025 Certificate](/data/images/tech/ICCCINT_certificate_2025.jpg)

---

# Final Thoughts

Concept drift detection is no longer enough.

Modern ML systems must be:

- Causally aware  
- Non-linearity capable  
- Statistically validated  
- Interpretable  

Drift is not merely a statistical anomaly.

It is a signal that the system’s environment, structure, or context has changed.

Understanding *why* it changed is where intelligent systems begin.