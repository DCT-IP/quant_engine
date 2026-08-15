# Rolling Windows

## What are Rolling Windows?
A rolling window is a fixed-size subset of $W$ consecutive observations that moves through a dataset one observation at a time. It calculates localized statistics over subsets of data rather than across an entire global dataset.

---

## Why Use Rolling Windows?
- **Local Dynamics:** Tracks how properties (mean, volatility, min/max) change over time.
- **Time-Series Analysis:** Captures local trends, regime shifts, and signal dispersion.
- **Feature Engineering:** Produces dynamically updating input features for predictive models without using future data.

---

## Window Calculation & Mechanics
For a dataset of size $N$ and a window size of $W$:

$$\text{Number of Windows} = N - W + 1$$

### Numerical Example
Given $x = [10, 20, 30, 40, 50]$ and $W = 3$:
- **Extracted Windows:** $[10, 20, 30]$, $[20, 30, 40]$, $[30, 40, 50]$
- **Rolling Mean Output:** $[20, 30, 40]$

---

## Core Rolling Statistics
- **Rolling Mean (Moving Average):**

  $$\text{RollingMean}_t = \frac{1}{W} \sum_{i=t-W+1}^{t} x_i$$

- **Rolling Variance:**

  $$s^2_t = \frac{1}{W - 1} \sum_{i=t-W+1}^{t} (x_i - \bar{x})^2$$

- **Rolling Standard Deviation (Volatility):**

  $$\text{RollingStd}_t = \sqrt{s^2_t}$$

- **Rolling Extrema (Min/Max):** Identifies the localized extreme values within each frame.

---

## Financial Applications

| Indicator / Metric | Description | Formula / Concept |
| :--- | :--- | :--- |
| **Simple Moving Average (SMA)** | Smooths price action to identify trends | $\text{SMA}_t = \text{RollingMean}_t(P)$ |
| **Rolling Volatility** | Measures changing market risk | $\sigma_t = \text{RollingStd}_t(\text{returns})$ |
| **Bollinger Bands** | Volatility-adjusted price envelopes | $\text{SMA}_t \pm k \cdot \sigma_t$ |
| **Risk Metrics** | Dynamic risk assessment | Rolling Sharpe Ratio, Rolling Beta, ATR |

---

## Implementation: Naive vs. Vectorized

### Naive Implementation (Python Loop)
Extremely slow for large financial datasets due to Python loop overhead:
```python
rolling_mean = []
for i in range(len(data) - W + 1):
    window = data[i:i + W]
    rolling_mean.append(sum(window) / W)
```

---