import numpy as np
import matplotlib.pyplot as plt


class GADDS:


    def __init__ (self, unit_cell, crystal_structure):

        # specify crystal structure
        self.crystal_structure = crystal_structure

        # initialize unit cell and reciprocal space parameters        
        self.unit_cell = unit_cell
        
        if self.crystal_structure == 'orthorhombic':
            self.primitive_vectors = {
                'a1': np.array( [ unit_cell['a'], 0, 0 ] ),
                'a2': np.array( [ 0, unit_cell['b'], 0 ] ),
                'a3': np.array( [ 0, 0, unit_cell['c'] ] )
            }
        elif self.crystal_Structure == 'tetragonal':
            self.primitive_vectors = {
                'a1': np.array( [ unit_cell['a'], 0, 0 ] ),
                'a2': np.array( [ 0, unit_cell['a'], 0 ] ),
                'a3': np.array( [ 0, 0, unit_cell['c'] ] )
            }
        
        
        self.reciprocal_lattice = {
            'b1': 2*np.pi * np.cross(self.primitive_vectors['a2'], self.primitive_vectors['a3']) / (np.dot( self.primitive_vectors['a1'], np.cross(self.primitive_vectors['a2'], self.primitive_vectors['a3']) )),
            'b2': 2*np.pi * np.cross(self.primitive_vectors['a3'], self.primitive_vectors['a1']) / (np.dot( self.primitive_vectors['a2'], np.cross(self.primitive_vectors['a3'], self.primitive_vectors['a1']) )),
            'b3': 2*np.pi * np.cross(self.primitive_vectors['a1'], self.primitive_vectors['a2']) / (np.dot( self.primitive_vectors['a3'], np.cross(self.primitive_vectors['a1'], self.primitive_vectors['a2']) ))
        }




if __name__ == '__main__':

    unit_cell = {
        'a': 3e-10,
        'b': 4e-10,
        'c': 6e-10
    }

    crystal_structure = 'orthorhombic'

    UTe2 = GADDS ( unit_cell, crystal_structure)
    print(UTe2.reciprocal_lattice)
    