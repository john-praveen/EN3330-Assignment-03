# EN3330 Assignment 03 - Lagrangian Duality

**Name:** PRAVEEN V.V.J.
**Index No:** 220491B
**Module:** EN3330 Introduction to Engineering Optimization

## What this code does

This Python script draws all the graphs used in my Assignment 03 report.

The problem used in the assignment is:

```
minimize    x^2
subject to  x >= 1
```

The Lagrangian is `L(mu, x) = x^2 + mu(1 - x)` with `mu >= 0`.

The script makes these graphs:

| File | Question | What it shows |
|------|----------|---------------|
| `q1a_lagrangian.pdf` | Q1(a) | `L(mu, x)` against `x` for `mu = 0, 1, 2, 3`, with the minimum point of each curve |
| `q1b_dual.pdf` | Q1(b) | The dual function `d(mu) = mu - mu^2/4`, with the maximum at `mu* = 2` |
| `q1c_primal.pdf` | Q1(c) | The primal function `g(x)`, which is `x^2` when `x >= 1` and infinity when `x < 1` |
| `q2a_saddle_slices.pdf` | Q2(a) | `L(mu, x*)` against `mu`, and `L(mu*, x)` against `x` |
| `q3b_envelope.pdf` | Q3(b) | The lines `L(mu, x)` for `x = 0, 1, 2` and their lower envelope |

It also prints the values of `d(mu)` for `mu = 0, 1, 2, 3`, which are used in Q3(a).

## How to run

1. Install Python 3.
2. Install the required libraries:

   ```
   pip install numpy matplotlib
   ```

3. Run the script:

   ```
   python en3330_a03_lagrangian_duality.py
   ```

The graphs are saved as PDF files in the `images` folder, next to the script.
The `images` folder in this repository already has all the graphs.

## Expected output

```
saved q1a_lagrangian.pdf
saved q1b_dual.pdf
saved q1c_primal.pdf
saved q2a_saddle_slices.pdf
saved q3b_envelope.pdf
d(0..3) = [0.0, 0.75, 1.0, 0.75]
L(2,1) = 1  L(mu,1) = [1, 1, 1, 1, 1]
```
