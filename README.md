# Monte Carlo Estimation of π — Stage I

I started this project because I wanted to understand the physics 
behind nuclear reactors. That led me to Monte Carlo methods, the idea 
that you can throw millions of random samples at a problem and extract 
something precise and real from what looks like pure chaos and garble.

## Why π?

Estimating π through random sampling sounded simple, but it forced me 
to think about probability differently. More like a measured variable, 
something that's concrete like mass or velocity. When you watch millions of 
random points converge onto a single value, probability stops being 
abstract and starts being physical.

The most surprising thing was seeing the rate of error actually fall 
as sample size increased. There's something genuinely amazing about 
watching that happen. Millions of invisible operations, none of which 
individually mean anything, collectively building toward a precise 
answer. I couldn't even see it happening, but I could with mathematics.

## What I found

- Error scales as 1/√N, so to halve the error you need four times the 
  samples and four times the computation time
- Execution time scales linearly with N
- The convergence is slow but exact, and the 1/√N behaviour isn't 
  specific to π at all. It reappears in Stage II neutron transport 
  without any modification because it's a property of random sampling 
  itself, not of the geometry

## Why this connects to nuclear engineering

Nuclear reactors involve billions of neutron interactions happening in 
fractions of a second. Monte Carlo codes like OpenMC replicate this 
statistically, where each simulated neutron history is one random 
sample and the reactor's behaviour emerges from running enough of them. 
The fact that a computer can approximate that process, and that the 
mathematics describes it exactly, is what made me want to go further.

This project is where that started. Mathematics as a looking glass, 
a way to analyse processes that are completely invisible to the eye 
but completely real in the math :)

## Files

- `pi_simulation.py` — main simulation
- `graph_plotting.py` — plotting scripts  
- `pi estimate vs sample size.png` — convergence of the estimate
- `error vs sample size.png` — 1/√N error scaling on log-log axes
- `time vs sample size.png` — linear computational cost
- `Monte_Carlo_Estimation_of_π_and_Analysis_of_Convergence_Behavior.pdf` 
  — full research paper

## Part of a larger project

- **Stage I** (this repo) — Monte Carlo estimation of π
- **Stage II** — Neutron transport simulation, Beer-Lambert attenuation 
  law verified from first principles
- **Stage III** — Full reactor criticality simulation using OpenMC 
  (in progress)
