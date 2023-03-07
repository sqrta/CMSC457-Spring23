# Do the necessary imports
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer
from qiskit.extensions import Initialize

from qiskit.quantum_info import random_statevector, Statevector,partial_trace

def trace01(out_vector):
    return Statevector([sum([out_vector[i] for i in range(0,4)]), sum([out_vector[i] for i in range(4,8)])])

def teleportation():
    # Create random 1-qubit state
    psi = random_statevector(2)
    print(psi)

    init_gate = Initialize(psi)
    init_gate.label = "init"

    ## SETUP
    qr = QuantumRegister(3, name="q")   # Protocol uses 3 qubits
    crz = ClassicalRegister(1, name="crz") # and 2 classical registers
    crx = ClassicalRegister(1, name="crx")
    qc = QuantumCircuit(qr, crz, crx)
    qc.initialize(psi, qr[0])
    # Don't modify the code above
    ## Put your code below
    # ----------------------------



    # ----------------------------
    # Don't modify the code below

    sim = Aer.get_backend('aer_simulator')
    qc.save_statevector()
    out_vector = sim.run(qc).result().get_statevector()
    result = trace01(out_vector)
    return psi, result

