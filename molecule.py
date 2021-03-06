from particle import Particle
import numpy as np
class Molecule:
    def __init__(self, pos1, pos2, mass1, mass2, k, L0): 
        '''Initializes a diatomic molecule from 2 particles. Takes in 2 particles'''
        '''a spring constant, and the equilibrium distance the 2 particles should be apart for no force to act on them'''
        self.k = k
        self.L0 = L0
        self.p1 = Particle(pos1, mass1)
        self.p2 = Particle(pos2, mass2)

    def get_displ1(self): 
        '''Returns a displacement vector corresponding to the displacement of the 2 positions'''
        return np.array([self.p1.pos[0] - self.p2.pos[0],self.p1.pos[1] - self.p2.pos[1]])
    def get_force(self): 
        '''Returns a force vector corresponding to the spring force '''
        mag = np.linalg.norm(self.get_displ1())
        unit = self.get_displ1()/mag
        return (unit*self.k*(mag-self.L0)**2)
