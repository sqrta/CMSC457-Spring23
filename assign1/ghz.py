from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute
from qiskit import Aer

def GHZ(n):
    if n<=0:
        return None
    circ = QuantumCircuit(n)
    circ.h(0)
    for i in range(1,n):
        circ.cx(i-1,i)

    return circ

print(GHZ(4))