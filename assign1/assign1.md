# Assign 1

In this assignment, you will learn how to set up qiskit environment and need to implment a teleportation circuit with qiskit. You are required to 

- Simulate a n-qubit GHZ circuit and get the measurement result in Qiskit. 
- Get the unitary matrix of this circuit circuit.
- Implement a teleportation circuit in Qiskit

## n-qubit GHZ Circuit

A n-qubit Greenberger–Horne–Zeilinger state (GHZ state) is the quantum state
```math
|GHZ\rangle_n = \frac{|0\rangle^n + |1\rangle ^n}{\sqrt{2}}
```
You are required to write a program `ghz.py` that generates a Qiskit circuit which can transform the quantum state from $|0\rangle^n$ to $|GHZ\rangle_n$.

### Input

Your python program should take two command line arguements as input,
```shell
python your_program <n> <output_filename>.csv
```
'n' is the number of qubit. You can assume `n` is an integer and `n>3`.

### Output

Your program should generate a n-qubit Qiskit circuit which can generate the state $|GHZ\rangle_n$ from $|0\rangle^n$, and write its unitary matrix into a csv file "output_filename".


## Quantum Teleportation

You are required to implement a one-qubit teleportation process from Alice to Bob with Qiskit. In this assignment, we suppose Alice and Bob are at the same place and the physical "sending" process is omit. Recall that Alice and Bob needs an entangled qubit pair to transform a qubit, so your circuit should have three qubit $q_0,q_1,q_2$. We suppose qubit $q_0$ is the qubit to be transferred and it is initialized in a quantum state $|\phi\rangle$. Alice keeps qubit $q_0,q_1$ and Bob keeps qubit $q_2$, and qubits $q_0,q_1$ are initialized as $|0\rangle$. Your teleportation circuit should have three steps:

1. Create a Bell pair using qubit $q_1,q_2$
2. Alice applies some operations on qubit $q_0,q_1$. His operation should include measurement and store the result in Qiskit classical register.
3. Bob applies some operations one qubit $q_2$ based on the measurement result.

After these three steps, qubit $q_2$, the qubit Bob keeps, should have the state $|\phi\rangle$. Your program should be named as `teleportation.py`

## What to Submit

- `ghz.py`
- `teleporation.py`

You should put your code in a single directory (named `LastName-FirstName-assign1`), compress it to .tar.gz (`LastName-FirstName-assign0.tar.gz`) and upload that to gradescope.
