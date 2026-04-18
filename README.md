#  ISAC Vehicular Network Simulation

This project implements a **simulation-based performance analysis** of an **Integrated Sensing and Communication (ISAC)** system in vehicular networks using **stochastic geometry**.

---

##  Overview

* Roads are modeled using **Poisson Line Process (PLP)**
* RSUs are distributed using **Poisson Point Process (PPP)**
* A typical user is placed at the origin
* Both **sensing and communication** are analyzed under interference

---

##  Objectives

* Evaluate:

  * **PSP** – Probability of Successful Sensing
  * **CCP** – Communication Coverage Probability
  * **JPISAC** – Joint Performance

* Analyze the **trade-off between sensing and communication**

---

##  System Model

* Roads → PLP

* RSUs → PPP on each road

* Random variables:

  * Distance
  * Fading
  * Antenna gain

* Interference modeled as aggregate contribution from all RSUs

---

##  Key Concepts

* SIR (Signal-to-Interference Ratio)
* Interference-limited system
* Monte Carlo simulation

---

##  Results

The following plots are generated:

1. PSP vs Distance
2. PSP vs Threshold
3. PSP vs Density
4. CCP vs Threshold
5. CCP vs Density
6. JPISAC vs Distance
7. JPISAC vs Threshold
8. PSP vs CCP (Trade-off)
9. PSP & CCP vs β

📷 Results are available in `/results/figures`

---

##  How to Run

```bash
git clone https://github.com/kairo786/isac-vehicular-network-simulation.git
cd isac-vehicular-network-simulation
pip install -r requirements.txt
python plots/run_plots.py
```

---

##  Requirements

* Python 3.x
* NumPy
* Matplotlib

---

##  Project Structure

* `models/` → PLP & PPP generation
* `simulation/` → SIR, interference, metrics
* `plots/` → graph generation
* `utils/` → helper functions

---

## Documentation

*  Research Paper → `/docs/paper.pdf`
*  Presentation → `/docs/presentation.pptx`

---

##  Key Insight

> ISAC systems exhibit a fundamental trade-off between sensing and communication due to shared interference.

---

##  Author

**Ankit Kero**
IIT Patna
