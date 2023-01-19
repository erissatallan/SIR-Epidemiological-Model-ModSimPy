# SIR-Epidemiological-Model-ModSimPy
An epidemiological model for the spread of an infection in a small, closed or about-closed system.


## Model description 

This is a compartmental model for the spread of an infection in a closed or about-closed (relative to the population size, the fraction of individuals joining and/ or leaving the population is very small) community. S, I, and R represent the susceptible, infected, and recovered compartments, respectively.

If we let s, i, and r represent the fraction of the total population in the respective comparments above, then the following differential equations apply to the system:

$$
\begin{align} 
\frac{ds}{dt} &= -\beta si \\
\frac{di}{dt} &= \beta si - \gamma i \\
\frac{di}{dt} &= \gamma i \\
\end{align}
$$

where $t$ is the time variable, 

## Assumptions
The fraction of individuals joining and/ or leaving the population is 0 or very small.
Time is a continuous variable.
There are no deaths nor births.
Permanent immunity is developed upon recovery.
