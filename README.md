# abmSEIDR
Agent-Based SEIRD Modelling of a Closed Community



## Overview

Agent-based modeling system simulating disease spread through Susceptible-Exposed-Infected-Deceased-Recovered populations. Combines Jupyter Notebook analysis (`SEIDR Model.ipynb`) with interactive GUI application.

## Features

- 🦠 Agent-based epidemic modeling
- 📈 Real-time visualization
- 🎛️ Interactive parameter controls
- 📊 Simulation statistics (peak infections, mortality rates)
- 📁 Modular architecture

## Installation

```bash
pip install numpy scipy matplotlib
```

## Usage

```bash
python main.py
```

## Project Structure

```
abmSEIDR/
├── SEIDR Model.ipynb		  # Data analysis notebook
├── main.py			  # Application entry point
└── seidr_model/
    ├── model.py		  # Core agent simulation logic
    └── app.py			  # GUI interface components
```

## Model Parameters

- **Infection Rate (β)**: Probability of disease transmission
- **Incubation Period (σ)**: Days before showing symptoms
- **Recovery Rate (γ)**: Chance of recovery from infection
- **Mortality Rate (μ)**: Risk of death from infection

## GUI Features

- Slider controls for real-time parameter adjustment
- Dynamic matplotlib visualization
- Statistics panel showing key epidemic metrics
- Responsive design with Tkinter

## Data Analysis

The economic analysis implemented by Jupyter Notebook and discussion are presented in the report.
