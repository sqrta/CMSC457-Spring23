# Do the necessary imports
import numpy as np
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer
from qiskit.extensions import Initialize
import json

from qiskit.quantum_info import random_statevector, Statevector,partial_trace

def trace01(out_vector):
    return Statevector([sum([out_vector[i] for i in range(0,4)]), sum([out_vector[i] for i in range(4,8)])])

def create_bell_pair(qc, a, b):
    """Creates a bell pair in qc using qubits a & b"""
    qc.h(a) # Put qubit a into state |+>
    qc.cx(a,b) # CNOT with a as control and b as target
    ## SETUP

def alice_gates(qc, psi, a):
    qc.cx(psi, a)
    qc.h(psi)

def measure_and_send(qc, a, b):
    """Measures qubits a & b and 'sends' the results to Bob"""
    qc.barrier()
    qc.measure(a,0)
    qc.measure(b,1)

# This function takes a QuantumCircuit (qc), integer (qubit)
# and ClassicalRegisters (crz & crx) to decide which gates to apply
def bob_gates(qc, qubit, crz, crx):
    # Here we use c_if to control our gates with a classical
    # bit instead of a qubit
    qc.x(qubit).c_if(crx, 1) # Apply gates if the registers 
    qc.z(qubit).c_if(crz, 1) # are in the state '1'

def teleportation():
    # Create random 1-qubit state
    # f = open("submission_metadata.json")
    # data = json.load(f)
    # print(data)
    # previous = data['previous_submissions'][0]
    # print(previous)

    psi = random_statevector(2)
    print(psi)

    init_gate = Initialize(psi)
    init_gate.label = "init"

    ## SETUP
    qr = QuantumRegister(3, name="q")   # Protocol uses 3 qubits
    crz = ClassicalRegister(1, name="crz") # and 2 classical registers
    crx = ClassicalRegister(1, name="crx")
    qc = QuantumCircuit(qr, crz, crx)

    ## STEP 0
    # First, let's initialize Alice's q0
    qc.append(init_gate, [0])
    qc.barrier()

    ## STEP 1
    # Now begins the teleportation protocol
    create_bell_pair(qc, 1, 2)
    qc.barrier()

    ## STEP 2
    # Send q1 to Alice and q2 to Bob
    alice_gates(qc, 0, 1)

    ## STEP 3
    # Alice then sends her classical bits to Bob
    measure_and_send(qc, 0, 1)

    ## STEP 4
    # Bob decodes qubits
    bob_gates(qc, 2, crz, crx)


    sim = Aer.get_backend('aer_simulator')
    qc.save_statevector()
    out_vector = sim.run(qc).result().get_statevector()
    result = trace01(out_vector)
    return psi, result

