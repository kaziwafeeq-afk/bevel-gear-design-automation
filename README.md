# Bevel Gear Design & Automation Tool

A Python-based engineering tool designed to automate iterative mechanical calculations, stress evaluations, and safety verifications for bevel gear systems.

---

## Project Overview
* **Objective:** Eliminate manual hand-calculation bottlenecks in machine design by creating an interactive Python script that computes gear geometry, module sizing, and wear/bending safety limits.
* **Key Features:**
  * Automated cone angle ($\Delta_1, \Delta_2$) and virtual number of teeth calculations.
  * Lewis form factor evaluations and dynamic module sizing.
  * Comparative wear and compressive stress checks against material allowable limits (C-50 Pinion and C-35 Gear).
  * Structured terminal output using the `tabulate` library for clean presentation.

---

## Input Parameters & Operating Conditions
* **Input Power:** 10 kW
* **Initial Speed (Pinion):** 1440 RPM
* **Final Speed (Gear):** 350 RPM
* **Pressure Angle:** 20 degrees
* **Intersection Angle:** 85 degrees

---

## Sample Results Summary

| Parameter | Value | Unit / Remarks |
| :--- | :--- | :--- |
| **Gear Ratio** | 4.22 | - |
| **Pinion Teeth / Gear Teeth** | 18 / 76 | Min teeth / Hunting teeth added |
| **Module** | 4.0 | mm |
| **Cone Distance ($R$)** | 156.2 | mm |
| **Face Width ($B$)** | 52.07 | mm |
| **Design Compressive Stress** | 602.5 | N/mm² |
| **Induced Compressive Stress** | 459.15 | N/mm² |
| **Design Status** | **Safe** | Induced stress < Allowable limit |

---

## Documentation & Repository Structure
* **[View Python Source Code (`BEVEL GEAR.py`)](./BEVEL%20GEAR.py)**: The complete source code featuring interactive inputs and automated validation logic.
* **[Download Full Assignment Report (PDF)](./DMS%20BEVEL%20GEAR%20ASSIGNMENT%202-1.pdf)**: Complete theoretical derivations and hand-calculation cross-references.
