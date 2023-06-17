import cirq

bell = cirq.Circuit()
q = cirq.LineQubit.range(2)
bell.append(cirq.H(q[0]))
bell.append(cirq.CNOT(q[0], q[1]))
bell.append(cirq.measure(q[0], q[1]))


