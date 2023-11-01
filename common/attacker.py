from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter

def measure_and_conditional_reset(qc: QuantumCircuit, qregs: QuantumRegister, cregs: ClassicalRegister):
    qc.measure(qregs, cregs)
    for i, creg in enumerate(cregs):
        with qc.if_test((creg, 1)):
            qc.x(qregs[i])
    return qc    

# def measure_all_and_conditional_reset(num_of_qubits: int):
#     qregs = QuantumRegister(num_of_qubits)
#     cregs = ClassicalRegister(num_of_qubits)
#     qc = QuantumCircuit(qregs, cregs, name='meas all and reset')
#     qc.measure(qregs, cregs)
#     for i, creg in enumerate(cregs):
#         with qc.if_test((creg, 1)):
#             qc.x(qregs[i])
#     return qc

# def single_snooping_window(num_of_qubits: int) -> QuantumCircuit:
#     assert num_of_qubits > 0
#     qregs = QuantumRegister(num_of_qubits)
#     cregs = ClassicalRegister(num_of_qubits)
#     delay_dt = Parameter('snooping duration')
#     qc = QuantumCircuit(qregs, cregs)
#     qc.h(qregs)
#     qc.delay(delay_dt, qregs)
#     qc.h(qregs)
#     qc.measure(qregs, cregs)
#     return qc

# def conditional_reset(num_of_qubits: int):
#     qregs = QuantumRegister(num_of_qubits)
#     cregs = ClassicalRegister(num_of_qubits)
#     qc = QuantumCircuit(qregs, cregs, name="Conditional Reset")
#     for i in range(num_of_qubits):
#         with qc.if_test((cregs[i], 1)):
#             qc.x(qregs[i])
#     return qc

# def create_snooping_circuit(num_of_qubits: int, reps: int = 0) -> QuantumCircuit:
#     assert num_of_qubits > 0
#     assert reps > 0
#     qregs = QuantumRegister(num_of_qubits)
#     cregs_array = [ClassicalRegister(num_of_qubits)]
#     for _ in range(reps):
#         cregs_array.append(ClassicalRegister(num_of_qubits))
#     qc = QuantumCircuit(qregs, *cregs_array)
#     single_snooping_window_qc = single_snooping_window(num_of_qubits)
#     conditional_reset_qc = conditional_reset(num_of_qubits)
#     for i in range(reps):
#         qc = qc.compose(single_snooping_window_qc, qregs, cregs_array[0])
#         if i < reps - 1:
#             qc.append(conditional_reset_qc, qregs, cregs_array[i])
#             qc.barrier()
#     return qc