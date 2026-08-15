# Quant Engine

> A production-oriented quantitative computing and trading systems toolkit built from first principles.

---

## Overview

Quant Engine is a long-term engineering project focused on building the computational foundations used in quantitative finance and financial systems.

The project combines:

- Numerical computing
- Statistics
- Time-series analysis
- Quantitative finance
- Performance engineering
- Market-data processing
- Backtesting
- Risk management
- Trading infrastructure

The goal is not to build a strategy collection or rely on existing trading frameworks.

Instead, the project focuses on understanding and implementing the underlying computational primitives and infrastructure required to build quantitative systems.

Where appropriate, algorithms are implemented from first principles.

Where performance-oriented numerical computation is the subject of study, optimized libraries such as NumPy are deliberately used and analyzed rather than avoided.

---

## Objectives

The project aims to develop the ability to:

- Implement mathematical and statistical algorithms
- Build reusable numerical computing components
- Process financial time-series data
- Design vectorized numerical operations
- Understand memory and computational performance
- Build backtesting infrastructure
- Build portfolio and risk engines
- Process streaming market data
- Implement order-book and execution systems
- Profile and optimize computational bottlenecks
- Integrate Python research code with high-performance C++

The final objective is to develop software suitable for a portfolio demonstrating quantitative engineering and financial systems engineering skills.

---

# Roadmap

## Stage 0 — Mathematical Foundations

Theory-only study covering:

- Probability
- Statistics
- Linear Algebra
- Calculus
- Optimization
- Time Series
- Numerical Methods

These foundations support the computational work implemented in the repository.

---

# Stage 1 — Numerical & Quantitative Computing

## Module 1 — NumPy Fundamentals

- ndarray
- Array operations
- Broadcasting
- Views vs Copies
- Memory layout
- Vectorized computation
- Basic numerical/statistical operations
- Financial return calculations

## Module 2 — Vectorization

- Rolling statistics
- Vectorized financial operations
- Array slicing
- Cumulative operations
- Performance comparison
- Memory behavior
- Cache locality
- Numerical optimization

## Module 3 — Market Data

- OHLCV data
- Candles
- Tick data
- Bid / Ask
- Spread
- Data loading
- Data validation
- Return and volatility calculations

## Module 4 — Financial Indicators

Implement indicators from first principles:

- SMA
- EMA
- RSI
- Bollinger Bands
- ATR
- MACD

No dependence on indicator libraries.

## Module 5 — Backtesting

Build the foundations of a backtesting engine:

- Positions
- Long / Short
- Entries
- Exits
- Transaction costs
- Strategy evaluation
- Sharpe ratio
- Drawdown
- Win rate

## Module 6 — Portfolio Engine

- Position sizing
- Portfolio weights
- Risk allocation
- Diversification
- Rebalancing
- Portfolio valuation
- Portfolio performance

---

# Stage 2 — Trading Infrastructure

## Module 7 — Async Market Data

- asyncio
- WebSockets
- Streaming data
- JSON parsing
- Market-data pipelines

## Module 8 — Order Book

- Level 1 data
- Level 2 data
- Market depth
- Bid / Ask
- Spread
- Order matching
- Limit order book simulation

## Module 9 — Execution Engine

- Market orders
- Limit orders
- Slippage
- Commission
- Execution latency
- Execution simulation

## Module 10 — Risk Engine

- Position limits
- Exposure
- Drawdown
- Risk checks
- Stop conditions
- Trade rejection

## Module 11 — Paper Trading

Integrate:

    Market Data
         ↓
      Strategy
         ↓
     Risk Engine
         ↓
   Execution Engine
         ↓
      Portfolio

to produce a complete paper-trading environment.

---

# Stage 3 — Performance Engineering

## Module 12 — Performance

Study and apply:

- Profiling
- CPU performance
- Memory usage
- Cache locality
- Allocation costs
- Vectorization
- Benchmarking
- Async performance
- Algorithmic complexity

---

# Stage 4 — High-Performance C++

Performance-critical components will progressively be implemented in modern C++ within this same repository.

Potential components include:

- Numerical primitives
- Rolling statistics
- Market-data processing
- Order books
- Matching engines
- Execution systems
- Low-latency infrastructure

The development workflow will generally follow:

    Python prototype
           ↓
    Correctness tests
           ↓
        Benchmark
           ↓
    Identify bottleneck
           ↓
    C++ implementation
           ↓
        Benchmark again
           ↓
    Python integration

The repository will therefore evolve into a hybrid Python/C++ quantitative engineering system rather than becoming separate language-specific projects.

---

# Repository Structure

The repository evolves incrementally.

Current structure:

    quant-engine/
    │
    ├── src/
    │   └── quant_engine/
    │       ├── math/
    │       ├── statistics/
    │       └── finance/
    │
    ├── tests/
    ├── examples/
    ├── docs/
    ├── benchmarks/
    │
    ├── pyproject.toml
    ├── README.md
    ├── LICENSE
    └── .gitignore

Future structure may expand into:

    quant-engine/
    │
    ├── src/
    │   └── quant_engine/
    │       ├── math/
    │       ├── statistics/
    │       ├── finance/
    │       ├── optimization/
    │       ├── simulation/
    │       ├── timeseries/
    │       ├── data/
    │       ├── portfolio/
    │       ├── risk/
    │       └── execution/
    │
    ├── cpp/
    │   ├── include/
    │   ├── src/
    │   ├── tests/
    │   └── benchmarks/
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

---

# Development Philosophy

Every implementation should satisfy at least one of the following:

- Introduce a meaningful mathematical or statistical concept
- Build reusable computational infrastructure
- Support future quantitative finance components
- Demonstrate software engineering principles
- Provide a foundation for performance analysis
- Be suitable for production-style systems

The project emphasizes:

- Correctness
- Modularity
- Testability
- Documentation
- Reusability
- Performance awareness

Code should not exist merely as an isolated exercise.

Each component should have a clear relationship to the larger quantitative-engineering system.

---

# Testing

Tests are written using `pytest`.

Run:

    pytest

Numerical comparisons should use appropriate tolerance-based assertions where floating-point arithmetic is involved.

---

# Development Tools

The project currently uses:

- Python 3.12+
- NumPy
- pytest
- Ruff
- Black

Additional technologies will be introduced as required by later stages.

Planned technologies include:

- C++
- pandas
- SciPy
- Matplotlib
- Redis
- PostgreSQL
- WebSockets
- pybind11 / nanobind
- gRPC
- Kafka

---

# Installation

## Prerequisites

- Python 3.12+
- Git

Verify Python:

    python --version

---

## Clone

    git clone <repository-url>
    cd quant-engine

---

## Virtual Environment

### Windows

    python -m venv .venv
    .venv\Scripts\activate

### Linux / macOS

    python3 -m venv .venv
    source .venv/bin/activate

---

## Install

    python -m pip install --upgrade pip
    pip install -e ".[dev]"

---

## Verify

    pytest

---

## Formatting

    black .

---

## Linting

    ruff check .

---

# Current Progress

## Mathematical Foundations

- [x] Probability
- [x] Statistics
- [x] Linear Algebra
- [x] Calculus
- [x] Optimization
- [x] Time Series
- [x] Numerical Methods

## Numerical & Quantitative Computing

- [x] NumPy fundamentals
- [ ] Vectorization
- [ ] Market data
- [ ] Financial indicators
- [ ] Backtesting
- [ ] Portfolio engine

## Trading Infrastructure

- [ ] Async market data
- [ ] Order book
- [ ] Execution engine
- [ ] Risk engine
- [ ] Paper trading

## Performance

- [ ] Profiling
- [ ] Benchmarking
- [ ] C++ integration
- [ ] Low-latency components

---

# License

This project is licensed under the MIT License.