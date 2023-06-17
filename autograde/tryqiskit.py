from qiskit import IBMQ, QuantumCircuit, execute

# IBMQ.save_account(TOKEN)
IBMQ.load_account() # Load account from disk
IBMQ.providers()    # List all available providers

provider = IBMQ.get_provider(hub='ibm-q')  
# List all available real quantum device
provider.backends(simulator=False, operational=True) 

# Or, only those backends that are real devices, have more than 10 qubits,
provider.backends(filters=lambda x: x.configuration().n_qubits >= 10
                                    and not x.configuration().simulator
                                    and x.status().operational==True)

backend = provider.get_backend('ibmq_vigo')

circ = QuantumCircuit(3) # build a circuit
job = execute(circ, backend)

result = job.result()
counts = result.get_counts()
print(counts)