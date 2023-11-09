from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit.circuit import Parameter
import matplotlib.pyplot as plt

def attack_circ_amplitude_flips(
        qregs: QuantumRegister,
        cregs: ClassicalRegister,
        snooping_duration_param: Parameter,
        reps: int = 1
    ):
    '''
    qregs: Attack QuantumRegisters
    cregs: Attack ClassicalRegister
    snooping_duration_param: Snooping duration in dt
    reps: number of repetitions. Default is 1 which means we measure once.
    '''
    assert reps >= 1, "reps should be greater than equal to 1"
    qc = QuantumCircuit(qregs, cregs, name="Attack Circ Amp Flips")
    for i in range(reps):
        qc.delay(snooping_duration_param)
        cregs_start_index = i * len(qregs)
        cregs_end_index = cregs_start_index + len(qregs)
        select_cregs = cregs[cregs_start_index: cregs_end_index]
        if i != reps - 1:
            measure_and_conditional_reset(qc, qregs, select_cregs)        
        else:
            qc.measure(qregs, select_cregs)
    return qc

def attack_circ_phase_flips(
        qregs: QuantumRegister,
        cregs: ClassicalRegister,
        snooping_duration_param: Parameter,
        reps: int = 1
    ):
    '''
    qregs: Attack QuantumRegisters
    cregs: Attack ClassicalRegister
    snooping_duration_param: Snooping duration in dt
    reps: number of repetitions. Default is 1 which means we measure once.
    '''
    assert reps >= 1, "reps should be greater than equal to 1"
    qc = QuantumCircuit(qregs, cregs, name="Attack Circ Phase Flips")
    for i in range(reps):
        qc.h(qregs)
        qc.delay(snooping_duration_param)
        qc.h(qregs)
        cregs_start_index = i * len(qregs)
        cregs_end_index = cregs_start_index + len(qregs)
        select_cregs = cregs[cregs_start_index: cregs_end_index]
        if i != reps - 1:
            measure_and_conditional_reset(qc, qregs, select_cregs)        
        else:
            qc.measure(qregs, select_cregs)
    return qc

def measure_and_conditional_reset(qc: QuantumCircuit, qregs: QuantumRegister, cregs: ClassicalRegister):
    qc.barrier()
    qc.measure(qregs, cregs)
    for i, creg in enumerate(cregs):
        with qc.if_test((creg, 1)):
            qc.x(qregs[i])
    qc.barrier()
    return qc