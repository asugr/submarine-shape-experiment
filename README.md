# 🌊 Why Are Submarines Shaped Like Cigars?

### A computational experiment in fluid drag and underwater vehicle shape

> **How does streamlining affect the drag and propulsion power required by an underwater vehicle?**

**Fluid Dynamics • Mechanical Engineering • Python • Computational Modeling**

---

## 🔬 Research Question

A submarine has to move through a dense fluid while carrying a large internal volume.

So why isn't it shaped like a box?

This project uses a simplified physics model to investigate how **shape, drag coefficient, speed, and frontal area** affect the force and power required to move an underwater vehicle.

The goal is not to reproduce a real submarine exactly. It is to build a transparent computational experiment from first principles.

---

## 🚀 Try the Interactive Experiment

Explore how speed, water density, frontal area, and body shape affect estimated underwater drag.

👉 **[Launch the Submarine Shape Lab](https://asugr-submarine-shape-experiment-appapp-osqxjs.streamlit.app/)**

Try changing the speed and shape and observe how the estimated drag changes.

---

## 📐 The Physics

The simplified drag equation is:

$$D = \\frac{1}{2}\\rho V^2 C_D A$$

where:

- **D** = drag force
- **ρ** = water density
- **V** = vehicle speed
- **Cᴅ** = drag coefficient
- **A** = reference frontal area

The approximate propulsion power required to overcome drag is:

$$P = DV$$

Therefore:

$$D \\propto V^2$$

and:

$$P \\propto V^3$$

> **Increasing speed is expensive because drag grows approximately with the square of speed, while idealized drag power grows with the cube of speed.**

---

## 🧪 The Experiment

I compare three conceptual shapes:

| Shape | Illustrative Cᴅ | Main idea |
|---|---:|---|
| Sphere | 0.47 | Compact but relatively high form drag |
| Blunt cylinder | 1.05 | Strong flow separation and wake |
| Streamlined teardrop | 0.12 | Reduced separation and lower conceptual drag |

The reference frontal area is kept constant for the basic comparison.

> **Important:** These drag coefficients are illustrative educational assumptions, not CFD results or measurements of specific real submarines.

---

## 📊 What the Simulation Shows

At the same speed and frontal area, lowering the drag coefficient produces a large reduction in estimated drag.

The model also demonstrates how rapidly propulsion requirements increase with speed.

For example, doubling speed gives approximately:

- **4× the drag**
- **8× the idealized drag power**

This is why hydrodynamic efficiency matters so much for underwater vehicles.

---

## 🧠 Engineering Interpretation

The "cigar" shape is not about appearance.

A streamlined body can reduce pressure/form drag by allowing water to flow around the vehicle with less separation and a smaller wake.

However, **drag reduction is only one design objective**.

A real submarine must also consider:

- internal volume
- structural strength
- buoyancy
- stability
- maneuverability
- control surfaces
- propulsor interactions
- surface roughness
- noise
- manufacturing constraints

So the engineering problem is not simply:

> "What shape has the lowest drag?"

It is:

> **"What shape provides an effective compromise among competing engineering requirements?"**

---

## 💻 Interactive Experiment

The repository includes a Streamlit prototype where the user can change:

- water density
- vehicle speed
- frontal area
- conceptual body shape

and immediately see the resulting estimated drag and idealized propulsion power.

---

## ⚠️ Model Limitations

This is a **first-principles educational model**, not a submarine design simulator.

The simplified equation does not fully model:

- Reynolds-number effects
- boundary-layer behavior
- skin friction
- detailed flow separation
- appendages
- propulsor/hull interaction
- maneuvering
- free-surface effects
- cavitation

A higher-fidelity investigation could use CFD or experimental measurements.

---

## 🚀 Future Work

Possible extensions:

1. Compare shapes while keeping **volume** rather than frontal area constant.
2. Add a simple Reynolds-number calculation.
3. Separate pressure/form drag and skin-friction drag conceptually.
4. Investigate how length-to-diameter ratio changes estimated drag.
5. Build a physical water-channel experiment.
6. Compare the model with published experimental data.

---

## 📁 Repository Structure

```text
submarine-shape-experiment/
│
├── app/
│   └── app.py
│
├── data/
│   └── processed/
│       └── drag_comparison.csv
│
├── images/
│   ├── drag_vs_speed.png
│   ├── power_vs_speed.png
│   └── drag_coefficient_comparison.png
│
├── notebooks/
│   └── submarine_shape_experiment.ipynb
│
├── src/
│
├── README.md
└── requirements.txt
```

---

## 🎓 Why This Project Matters to Me

This project connects my interest in **Mechanical and Aerospace Engineering** with mathematical modeling and programming.

Instead of only learning the drag equation, I used it to build an experiment:

**Physics → Model → Simulation → Interpretation**

That is the approach I want to continue using in my engineering studies.

---

## 👩‍💻 Part of ScienceBehindIt Engineering Lab

This project is part of my **ScienceBehindIt Engineering Lab**, where I investigate the science behind real-world machines and communicate the results through computational experiments and science communication.
