from search import *

class WaterJugProblem(Problem):
    def __init__(self, initial, goal, capacities):
        super().__init__(initial, goal)
        self.capacities = capacities

# acoes possiveis
    def actions(self, state):
        actions = []
        recipiente_x, recipiente_y = state
        # Se o recipiente X tiver menos que sua capacidade, enche X.
        if recipiente_x < self.capacities[0]: actions.append('Enche recipiente X')
        # Se o recipiente Y tiver menos que sua capacidade, enche Y.
        if recipiente_y < self.capacities[1]: actions.append('Enche recipiente Y')
        # Se recipiente X não estiver vazio, esvazia X
        if recipiente_x > 0: actions.append('Esvazia recipiente X')
        # Se recipiente Y não estiver vazio, esvazia Y
        if recipiente_y > 0: actions.append('Esvazia recipiente Y')
        # Se recipiente X não estiver vazio e recipiente Y não estiver cheio, transfere do recipente X para o recipiente Y
        if recipiente_x > 0 and recipiente_y < self.capacities[1]: 
            actions.append('Transfere do recipiente X para o recipiente Y')
        # Se recipiente Y não estiver vazio e recipiente X não estiver cheio, transfere do recipente Y para o recipiente X
        if recipiente_y > 0 and recipiente_x < self.capacities[0]: 
            actions.append('Transfere do recipiente Y para o recipiente X')
        return actions

# resultados
    def result(self, state, action):
        recipiente_x, recipiente_y = state
        if action == 'Enche recipiente X': 
            return (self.capacities[0], recipiente_y)
        if action == 'Enche recipiente Y': 
            return (recipiente_x, self.capacities[1])
        if action == 'Esvazia recipiente X': 
            return (0, recipiente_y)
        if action == 'Esvazia recipiente Y': 
            return (recipiente_x, 0)
        if action == 'Transfere do recipiente X para o recipiente Y':
            return (recipiente_x - (self.capacities[1] - recipiente_y), self.capacities[1]) if recipiente_x > self.capacities[1] - recipiente_y else (0, recipiente_x + recipiente_y)
        if action == 'Transfere do recipiente Y para o recipiente X':
            return (self.capacities[0], recipiente_y - (self.capacities[0] - recipiente_x)) if recipiente_y > self.capacities[0] - recipiente_x else (recipiente_x + recipiente_y, 0)

# checagem se chegou no objetivo final
    def goal_test(self, state):
        return state == self.goal

# custo de caminho de cada acao
    def path_cost(self, c, state1, action, state2):
        return c + 1