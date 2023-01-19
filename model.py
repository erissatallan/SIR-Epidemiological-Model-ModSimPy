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
    state = system.init
    
    for t in linrange(system.t_0, system.t_end):
        state = update_func(state, t, system)
        
    return state

my_model = model(beta, gamma)
final_state = simulate(my_model, update_model)
final_state
