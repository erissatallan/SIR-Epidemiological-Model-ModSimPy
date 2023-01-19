# SIR-Epidemiological-Model
An epidemiological model for the spread of an infection in a small, closed or about-closed system.


## Model description 

This is a compartmental model for the spread of an infection in a closed or about-closed (relative to the population size, the fraction of individuals joining and/ or leaving the population is very small) community. S, I, and R represent the susceptible, infected, and recovered compartments, respectively.

If we let s, i, and r represent the fraction of the total population in the respective comparments above, then the following differential equations apply to the system:

$$
\begin{align*} 
\frac{ds}{dt} &= -\beta si \\
\frac{di}{dt} &= \beta si - \gamma i \\
\frac{di}{dt} &= \gamma i \\
\end{align*}
$$

where $t$ is the time variable.
The first of these equations suggests that the rate at which individuals move from comparment S to I (contract the infection) is directly proportional to the populations in these compartments, with a proportionality constant $\beta$. The second, that infected individuals recover at a rate proportional to their number and a constant $\gamma$. The second and third equations dictate that their respective compartments experience growth in populations resulting from the movement of individuals from the previous comparment.

## Assumptions
The fraction of individuals joining and/ or leaving the population is 0 or very small. <br/>
Time is a continuous variable. <br/>
There are no deaths nor births. <br/>
Permanent immunity is developed upon recovery. <br/>
Infected individuals immeditely become infectious.
