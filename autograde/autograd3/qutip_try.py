import numpy as np

from qutip import *

def sigma_i(N, i, sig):
    tmp = [qeye(2) for m in range(N)]
    tmp[i]=sig
    return tensor(tmp)

def integrate2(N, h, Jx, Jy, Jz, psi0, tlist):

    si = qeye(2)
    sx = sigmax()
    sy = sigmay()
    sz = sigmaz()

    sx_list = []
    sy_list = []
    sz_list = []

    for n in range(N):
        op_list = []
        for m in range(N):
            op_list.append(si)

        op_list[n] = sx
        sx_list.append(tensor(op_list))

        op_list[n] = sy
        sy_list.append(tensor(op_list))

        op_list[n] = sz
        sz_list.append(tensor(op_list))

    # construct the hamiltonian
    H = 0

    # energy splitting terms
    for n in range(N):
        H += - 0.5 * h[n] * sz_list[n]

    # interaction terms
    H1 = 0
    def H1_coeff(t, args):
        return np.exp(-(t / 5.) ** 2)
    
    for n in range(N-1):
        H1 += - 0.5 * Jx[n] * sx_list[n] * sx_list[n+1]
        H1 += - 0.5 * Jy[n] * sy_list[n] * sy_list[n+1]
        H1 += - 0.5 * Jz[n] * sz_list[n] * sz_list[n+1]

    # evolve and calculate expectation values
    result = mesolve([H, [H1, H1_coeff]], psi0, tlist)


    return result.states
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
    sz_expt = integrate2(N, h, Jx, Jy, Jz, psi0, tlist)
    print(sz_expt[point-1].full())


