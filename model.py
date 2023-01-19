import pint

from modsim import *

contact_time = 3 # there is a contact between individuals once every three days
recovery_time = 4

beta = 1 / contact_time
gamma = 1 / recovery_time

def model(beta, gamma):
    initial_state = State(S=89, I=1, R=0)
    initial_state /= sum(initial_state)
    
    t_0 = 0
    t_end = 7 * 14 # duration, in days, of a semester
    
    return System(init=initial_state, t_0=t_0, t_end=t_end, beta=beta, gamma=gamma)

def update_model(state, t, system):
    s, i, r = state
    
    infected = system.beta * i * s
    recovered = system.gamma * i
    
    s -= infected
    i += infected - recovered
    r += recovered
    
    return State(S=s, I=i, R=r)

def simulate(system, update_func):
    S = TimeSeries()
    I = TimeSeries()
    R = TimeSeries()
    
    state = system.init
    t_0 = system.t_0
    S[t_0], I[t_0], R[t_0] = state
    
    for t in linrange(system.t_0, system.t_end):
        state = update_func(state, t, system)
        S[t+1], I[t+1], R[t+1] = state
        
    return S, I, R

def plot_results(S, I, R):
    plot(S, '--', label='Susceptible')
    plot(I, '-', label='Infected')
    plot(R, ':', label='Resistant')
    decorate(xlabel='Time (days)', ylabel='Fraction of population')

my_model = model(beta, gamma)
S, I, R = simulate(my_model, update_model)

plot_results(S, I, R)
