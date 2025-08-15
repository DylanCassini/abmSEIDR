import random
import numpy as np

class SEIDR:
    def __init__(self, beta=0.02, gamma=0.1, delta=0.2, mu=0.01, N=1000):
        self.beta = beta
        self.gamma = gamma
        self.delta = delta
        self.mu = mu
        self.N = N
        self.population = [{'state': 'S'} for _ in range(N)]

    def run(self, days=160, E0=1, I0=0, D0=0, R0=0):
        # Set initial conditions
        for i in range(E0):
            self.population[i]['state'] = 'E'
        for i in range(E0, E0 + I0):
            self.population[i]['state'] = 'I'

        history = {'S': [], 'E': [], 'I': [], 'D': [], 'R': []}

        for day in range(days):
            counts = {'S': 0, 'E': 0, 'I': 0, 'D': 0, 'R': 0}
            for agent in self.population:
                counts[agent['state']] += 1

            num_infected = counts['I']

            history['S'].append(counts['S'])
            history['E'].append(counts['E'])
            history['I'].append(counts['I'])
            history['D'].append(counts['D'])
            history['R'].append(counts['R'])

            new_population = []
            for agent in self.population:
                new_agent = agent.copy()
                if agent['state'] == 'S':
                    if random.random() < self.beta * num_infected / self.N:
                        new_agent['state'] = 'E'
                elif agent['state'] == 'E':
                    if random.random() < self.delta:
                        new_agent['state'] = 'I'
                elif agent['state'] == 'I':
                    if random.random() < self.gamma:
                        new_agent['state'] = 'R'
                    elif random.random() < self.mu:
                        new_agent['state'] = 'D'
                new_population.append(new_agent)
            self.population = new_population

        t = np.linspace(0, days, days)
        S = np.array(history['S'])
        E = np.array(history['E'])
        I = np.array(history['I'])
        D = np.array(history['D'])
        R = np.array(history['R'])

        return t, (S, E, I, D, R)