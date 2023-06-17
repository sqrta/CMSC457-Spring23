from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Unroller

def map_board(lights, qc, qr):
    j = 0
    for i in lights:
        if i==1:
            qc.x(qr[j])
            j+=1
        else:
            j+=1

def diffusion(qc,flip):
    qc.h(flip)
    qc.x(flip)
    qc.h(flip[8])
    qc.mct(flip[0:8], flip[8])
    qc.h(flip[8])
    qc.x(flip)
    qc.h(flip)

# Subroutine for oracle
# Calculate what the light state will be after pressing each solution candidate. 
def flip_tile(qc,flip,tile):
    qc.cx(flip[0], tile[0])
    qc.cx(flip[0], tile[1])
    qc.cx(flip[0], tile[3])
    qc.cx(flip[1], tile[0])
    qc.cx(flip[1], tile[1])
    qc.cx(flip[1], tile[2])
    qc.cx(flip[1], tile[4])
    qc.cx(flip[2], tile[1])
    qc.cx(flip[2], tile[2])
    qc.cx(flip[2], tile[5])
    qc.cx(flip[3], tile[0])
    qc.cx(flip[3], tile[3])
    qc.cx(flip[3], tile[4])
    qc.cx(flip[3], tile[6])
    qc.cx(flip[4], tile[1])
    qc.cx(flip[4], tile[3])
    qc.cx(flip[4], tile[4])
    qc.cx(flip[4], tile[5])
    qc.cx(flip[4], tile[7])
    qc.cx(flip[5], tile[2])
    qc.cx(flip[5], tile[4])
    qc.cx(flip[5], tile[5])
    qc.cx(flip[5], tile[8])
    qc.cx(flip[6], tile[3])
    qc.cx(flip[6], tile[6])
    qc.cx(flip[6], tile[7])
    qc.cx(flip[7], tile[4])
    qc.cx(flip[7], tile[6])
    qc.cx(flip[7], tile[7])
    qc.cx(flip[7], tile[8])
    qc.cx(flip[8], tile[5])
    qc.cx(flip[8], tile[7])
    qc.cx(flip[8], tile[8])

def light_out_grover(lights,N):
    tile = QuantumRegister(9)
    flip = QuantumRegister(9)
    oracle_output = QuantumRegister(1)
    result = ClassicalRegister(9)
    #26 qubit
    qc = QuantumCircuit(tile, flip, oracle_output,  result)
    map_board(lights, qc, tile)

    qc.h(flip[0:10])
    qc.x(oracle_output[0])
    qc.h(oracle_output[0])

    for i in range(N):
        # oracle
        flip_tile(qc,flip,tile)
        
        qc.x(tile[0:9])
        qc.mct(tile[0:9], oracle_output[0])
        qc.x(tile[0:9])
        
        flip_tile(qc,flip,tile)
        
        # diffusion
        diffusion(qc,flip)
    # Uncompute
    qc.h(oracle_output[0])
    qc.x(oracle_output[0])
    # Measuremnt
    qc.measure(flip,result)

    # Make the Out put order the same as the input.
    qc = qc.reverse_bits() 

    from qiskit import execute, Aer
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend=backend, shots=50, seed_simulator=12345, backend_options={"fusion_enable":True})
    result = job.result()
    count = result.get_counts()

    score_sorted = sorted(count.items(), key=lambda x:x[1], reverse=True)
    final_score = score_sorted[0:40]
    return final_score[0][0]

test=[[0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 1, 1, 0],
        [0, 1, 1, 0, 1, 1, 0, 1, 1]
        ]
solutions=[]
for i in test:
    solutions.append(light_out_grover(i,17))
print(solutions)