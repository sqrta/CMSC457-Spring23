from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Unroller

def diffusion(qc,flip):
    qc.h(flip)
    qc.x(flip)
    qc.h(flip[8])
    qc.mct(flip[0:8], flip[8])
    qc.h(flip[8])
    qc.x(flip)
    qc.h(flip)

# Subroutine for oracle
# Calculate what the light state in `tile` will be after pressing each solution candidate in `flip`. 
def flip_tile(qc,flip,tile):
    pass

def light_out_grover(lights, N):
    tile = QuantumRegister(9)
    flip = QuantumRegister(9)
    oracle_output = QuantumRegister(1)
    result = ClassicalRegister(9)
    qc = QuantumCircuit(tile, flip, oracle_output,  result)
    # -----------------------------------------------------
    # Do not modify the code of this function above


    # Initialization

    # Grover Iteration
    for i in range(N):
        # Apply the oracle 
        
        # diffusion
        
        pass
    # Remember to do some uncomputation


    # Do not modify the code below
    # ------------------------------------------------------
    # Measuremnt
    qc.measure(flip,result)

    # Make the Out put order the same as the input.
    qc = qc.reverse_bits() 

    from qiskit import execute, Aer
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend, shots=8000, seed_simulator=12345, backend_options={"fusion_enable":True})
    result = job.result()
    count = result.get_counts()

    score_sorted = sorted(count.items(), key=lambda x:x[1], reverse=True)
    final_score = score_sorted[0:40]
    solution = final_score[0][0]
    return solution


# For local test, your program should print 110010101
lights = [0, 1, 1, 1, 0, 0, 1, 1, 1]
print(light_out_grover(lights,17))
