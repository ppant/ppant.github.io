---
layout: post
title: "Explainable Concept Drift Using MLP-Based Non-Linear Causality | ICCCNT 2025"
date: 2025-07-15
author: Pradeep Pant
categories: [Research, Process Mining, Machine Learning]
tags: [Concept Drift, Process Mining, Causality, MLP, Explainable AI, IEEE, PhD]
excerpt: "An explainable framework for concept drift detection using MLP-based non-linear causal modeling in process mining."
---

```When Concept Drift Is More Than a Distribution Shift Explaining Process Changes Using Non-Linear Causality```

**"Most systems can detect that something changed.  Very few can explain why it changed"**

In July 2025, I presented my research paper titled:
**Explainable Concept Drift in Process Mining Using MLP-Based Non-linear Causality Detection**

at the 16th International Conference on Computing, Communication and Networking Technologies (ICCCNT 2025) held at IIT Indore.

This work forms part of my **ongoing PhD research** in *process mining, causal inference, and adaptive MLOps systems*.

---

Machine learning models rarely fail dramatically. They degrade quietly. Accuracy drops slowly.  
Predictions become unstable. Business impact appears before monitoring dashboards raise alarms.

In **process-driven systems** — banking, manufacturing, healthcare — this degradation is often caused by **concept drift**.

But the real challenge is this:

> Systems usually detect **that drift occurred**,  
> but they rarely explain **what caused it**.

This research focuses on closing that gap.

---

## The Limitation of Traditional Drift Detection

Most drift detection techniques rely on:

- Statistical change detection  
- Window-based distribution comparison  
- Linear **Granger causality**  
- Prediction error monitoring  

These approaches are useful, but they mainly detect **symptoms** rather than **causes**.

Traditional Granger causality also assumes **linear relationships**.

However, real-world business processes rarely behave linearly.

Examples include:

- Workload affecting turnaround time in complex ways  
- Customer attributes influencing outcomes non-linearly  
- Resource allocation interacting dynamically with control-flow behavior  

Linear tools often miss these hidden dependencies.

---

## Reframing Drift: A Change in Causal Structure

Instead of asking:

> **Has the data distribution shifted?**

I asked a different question:

> **Has the causal structure between process variables changed?**

Event logs typically contain two categories of information.

### Primary Features
Control-flow patterns representing **how the process executes**.

### Secondary Features
Contextual attributes such as **age, workload, or resource usage**.

If contextual variables begin influencing process behavior differently over time, it indicates **structural drift**.

To capture this, the proposed framework combines:

- **Process mining**
- **Change point detection (PELT)**
- **Non-linear causal modeling using MLP**
- **Statistical validation via Wilcoxon test**

---

## Core Idea of the Framework

Two predictive models are trained.

### Model 1
Uses only **primary process features**.

### Model 2
Uses both **primary and contextual features**.

If Model 2 significantly improves prediction accuracy, we infer:

> **Contextual variables are causally influencing process behavior.**

This converts traditional drift detection into:

### **Causal Drift Explanation**

---

## Why Use MLP Instead of Linear Granger?

Traditional Granger causality identifies only **linear dependencies**.

Real-world systems often contain:

- Sinusoidal patterns  
- Exponential effects  
- Non-linear lag relationships  
- Multi-variable interactions  

**Multilayer Perceptrons (MLPs)** can naturally model these complex relationships.

The framework therefore:

- Uses **lag-based time windows**
- Employs **2–3 hidden layers with ReLU activation**
- Applies **dropout and early stopping**
- Evaluates performance using **Mean Squared Error (MSE)**
- Validates causal significance using the **Wilcoxon signed-rank test**

If contextual variables consistently reduce prediction error — and the improvement is statistically significant — they likely represent **true causal influence**.

---

## Experimental Validation

The framework was evaluated using three datasets.

### Synthetic CPI-generated datasets
Controlled experiments with:

- sudden drift
- gradual drift
- recurring drift

### BPI Challenge 2017 dataset
A real-world dataset containing:

**31,000+ loan application event logs**

### Large synthetic non-linear dataset
High-dimensional time series including functions such as:

- sin
- log
- exp
- sqrt

with injected drift.

### Key Results

- Consistent **MSE reduction** when contextual variables were included
- **Over 85% statistically significant improvements**
- Detection of **non-linear dependencies missed by linear models**
- **Low false causal detection**

These results demonstrate strong **robustness, sensitivity, and statistical reliability**.

---

## Why This Matters for Industry

In production ML systems, monitoring usually answers:

- Is model performance degrading?
- Is the data distribution changing?

But organizations need deeper insight:

- What caused the degradation?
- Which contextual factors changed?
- Is the drift **operational, behavioral, or structural**?

This research moves toward a more powerful paradigm:

> **Drift Detection → Drift Explanation → Root Cause Insight**

It also aligns with my broader **PhD research direction**:

### Process-Mining–Driven Observability for Self-Adaptive MLOps Pipelines

The long-term goal is to build ML systems that:

> **do not just detect failure — but understand structural change.**

---

## Limitations & Future Work

Some challenges remain:

- Fixed lag windows may miss dynamic temporal dependencies
- Pairwise modeling limits full multivariate causal discovery
- Real-world logs lack ground-truth causal labels
- Hyperparameter tuning remains important

Future directions include:

- Neural Granger approaches
- Transformer-based temporal modeling
- Multivariate structural causal models
- Online adaptive drift monitoring

---

## Conference Presentation

This research was presented at **ICCCNT 2025**, held at **IIT Indore (July 6–11, 2025)**.

Presentation certificate:

![ICCCNT 2025 Certificate](/data/images/tech/ICCCINT_certificate_2025.jpg)

---

## Final Thoughts

Concept drift detection alone is no longer sufficient.

Modern ML systems must be:

- **Causally aware**
- **Non-linear**
- **Statistically validated**
- **Interpretable**

Drift is not merely a statistical anomaly.

> It is a signal that the system’s **environment, structure, or context has changed**.

Understanding **why it changed** is where intelligent systems truly begin.