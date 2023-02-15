# Assign 1
<!-- 
In this assignment, you will learn how to set up qiskit environment and need to implment a teleportation circuit with qiskit. You are required to 

- Simulate a n-qubit GHZ circuit and get the measurement result in Qiskit. 
- Get the unitary matrix of this circuit circuit.
- Implement a teleportation circuit in Qiskit -->

## n-qubit GHZ Circuit

A n-qubit Greenberger–Horne–Zeilinger state (GHZ state) is the quantum state
```math
|GHZ\rangle_n = \frac{|0\rangle^n + |1\rangle ^n}{\sqrt{2}}
```
You are required to write a program `ghz.py` that generates a Qiskit circuit which can transform the quantum state from $|0\rangle^n$ to $|GHZ\rangle_n$. You are provided with [starter code](ghz.py) to handle input-output data. Your job is to finish the function `GHZ`. If you want to use a language other than Qiskit, please follow the input-output criteria below.

### Input

Your python program should take two command line arguements as input,

```shell
python your_program <n> <output_filename>
```

'n' is the number of qubit. You can assume `n` is an integer and `n>3`.

### Output

Your program should generate a n-qubit circuit which can generate the state $|GHZ\rangle_n$ from $|0\rangle^n$, and write its unitary matrix into a csv file "output_filename". Plese keep the decimal limit for each entry in the output matrix as 3. [Here](ghz3.csv) is an example output for `n=3`. You can use the python statement below to dump a NumPy array `matrix` into a csv file.

```python
numpy.savetxt(output_filename, matrix, delimiter=",", fmt = "%0.3f")
```


## Quantum Teleportation

You are required to implement a one-qubit teleportation process from Alice to Bob with Qiskit. In this assignment, we suppose Alice and Bob are at the same place and the physical "sending" process is omitted. Recall that Alice and Bob need an entangled qubit pair to transform a qubit, so your circuit should have three qubits $q_0,q_1,q_2$. We suppose qubit $q_0$ is the qubit to be transferred and it is initialized in a quantum state $|\phi\rangle$. Alice keeps qubit $q_0,q_1$ and Bob keeps qubit $q_2$, and qubits $q_0,q_1$ are initialized as $|0\rangle$. Your teleportation circuit should have three steps:

1. Create a Bell pair using qubit $q_1,q_2$
2. Alice applies some operations on qubit $q_0,q_1$. His operation should include measurement and store the result in Qiskit classical register.
3. Bob applies some operations one qubit $q_2$ based on the measurement result.

After these three steps, qubit $q_2$, the qubit Bob keeps, should have the state $|\phi\rangle$. Your program should be named as `teleportation.py`. You are provided with [starter code](teleportation.py). Your job is to finish the function `teleportation`.

## What to Submit

- `ghz.py`
- `teleporation.py`

Submit your two programs respectively to the Gradescope. Gradescope will test your submission automatically. You can resubmit until the due date (Mar 09, 2023 at 11:00:00 PM EST). But the auto-test works only once per 12 hours. We will manually grade the last version of your submissions if you do not get the full point from the auto-grader.

## Academic Integrity

Your submissions will be checked manually. The following are examples of academic integrity violations:

- Hardcoding of results in an assignment. Hardcoding refers to attempting to make a program appear as if it works correctly (e.g., printing expected results for a test).
- Hiring any online service to complete an assignment for you.
- Sharing your code or your tests with any student.
