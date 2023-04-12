import numpy as np

from qutip import *

def integrate(N, h, Jx, Jy, Jz, psi0, tlist):

    # construct the hamiltonian
    H0 = 0
    # energy splitting terms

    # interaction terms
    H1 = 0

    def H1_coeff(t, args):
        pass

    H = [H0, [H1, H1_coeff]]
    # evolve and calculate expectation values
    result = mesolve(H, psi0, tlist)
    return result.states


# For local test
if __name__ == "__main__":  
    N = 3            # number of spins
    h  = 1.0 * 2 * np.pi * np.ones(N) 
    Jz = 0.1 * 2 * np.pi * np.ones(N)
    Jx = 0.1 * 2 * np.pi * np.ones(N)
    Jy = 0.1 * 2 * np.pi * np.ones(N)

    # intial state, first spin in state |1>, the rest in state |0>
    psi_list = []
    psi_list.append(basis(2,1))
    for n in range(N-1):
        psi_list.append(basis(2,0))
    psi0 = tensor(psi_list)
    point = 5
    tlist = np.linspace(0, 2, point)
    sz_expt = integrate(N, h, Jx, Jy, Jz, psi0, tlist)
    print(sz_expt[point-1].full())

# For local test, your program should print

# [[ 0.        +0.j        ] 
#  [-0.49820154+0.1954353j ] 
#  [ 0.36553555+0.53850419j] 
#  [ 0.        +0.j        ] 
#  [ 0.5017984 +0.19543705j] 
#  [ 0.        +0.j        ] 
#  [ 0.        +0.j        ] 
#  [ 0.        +0.j        ]]



