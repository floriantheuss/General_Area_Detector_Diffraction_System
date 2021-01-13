import numpy as np
import matplotlib.pyplot as plt



# give unit cell parameters >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
unit_cell = {
    'a': 3e-10,
    'b': 4e-10,
    'c': 6e-10
}

crystal_structure = 'orthorhombic'



if crystal_structure == 'orthorhombic':
    primitive_vectors = {
        'a1': np.array( [ unit_cell['a'], 0, 0 ] ),
        'a2': np.array( [ 0, unit_cell['b'], 0 ] ),
        'a3': np.array( [ 0, 0, unit_cell['c'] ] )
    }


print (primitive_vectors)