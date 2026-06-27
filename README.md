# Quant Engine

> A production-oriented quantitative computing toolkit built from first principles.

---

## Overview

Quant Engine is a long-term project focused on building the computational foundations required for quantitative finance, numerical computing, and scientific software engineering.

Instead of relying immediately on high-level numerical libraries, this repository emphasizes implementing core mathematical algorithms from first principles to develop a deeper understanding of both the mathematics and the engineering behind quantitative systems.

The project evolves from foundational numerical algorithms into complete quantitative finance infrastructure, including pricing models, optimization techniques, simulations, and backtesting systems.

---

## Objectives

- Implement core mathematical algorithms from scratch
- Build reusable numerical computing components
- Develop production-quality Python code
- Learn quantitative finance through implementation
- Emphasize clean software architecture and testing
- Create a portfolio-quality quantitative computing toolkit

---

## Planned Roadmap

### Mathematical Computing

- Linear Algebra
- Numerical Methods
- Calculus-based Algorithms
- Probability & Statistics
- Optimization
- Time Series Analysis

### Quantitative Finance

- Option Pricing
- Portfolio Optimization
- Risk Analytics
- Monte Carlo Simulation
- Factor Models
- Performance Metrics

### Infrastructure

- Data Processing
- Research Utilities
- Visualization
- Benchmarking
- Backtesting Framework
- Financial Data Interfaces

---

## Repository Structure

```text
quant-engine/
│
├── src/
│   └── quant_engine/
│       ├── core/
│       ├── math/
│       ├── statistics/
│       ├── optimization/
│       ├── simulation/
│       ├── pricing/
│       ├── portfolio/
│       ├── risk/
│       ├── timeseries/
│       ├── data/
│       ├── visualization/
│       └── utils/
│
├── tests/
├── examples/
├── notebooks/
├── docs/
├── benchmarks/
│
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

---

## Development Philosophy

Every implementation in this repository should satisfy at least one of the following:

- Introduce a meaningful mathematical algorithm
- Build reusable infrastructure
- Support future quantitative finance modules
- Demonstrate sound software engineering principles
- Be suitable for production-style projects

The focus is on writing code that is modular, testable, documented, and reusable—not simply solving isolated exercises.

---

## Technologies

- Python
- NumPy *(used only where appropriate after first-principles implementations)*
- SciPy
- Matplotlib
- pandas
- pytest

Additional technologies may be incorporated as the project evolves.

---

## Getting Started

### Prerequisites

* Python 3.12 or newer
* Git

Verify your Python version:

```bash
python --version
```

---

### Clone the Repository

```bash
git clone <repository-url>
cd quant-engine
```

---

### Create a Virtual Environment

#### Windows

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

### Install Development Dependencies

```bash
pip install -e ".[dev]"
```

This installs all development tools specified in `pyproject.toml`, including:

* pytest
* black
* ruff

---

### Verify Installation

Run:

```bash
pytest
```

If no tests have been written yet, pytest may simply report that no tests were collected. This confirms the environment is set up correctly.

---

### Formatting

Format the project with:

```bash
black .
```

---

### Linting

Run Ruff:

```bash
ruff check .
```

---

## License

This project is licensed under the MIT License.