# Quantum Snooping

## Experiment - 1
### Aim
1. Determine if crosstalk causes phase noise errors(Z-flips) or amplitude noise errors(X-flips).
2. Determine how snooping time window effects our ability to detect CNOTs

Note: acquire_alignment = 16 for IBM Lagos. Hence the delay durations are multiples of 16.

### Results
- Crosstalk causes significantly more phase noise errors than amplitude noise errors.
- To observe these we need to fist perform a H-gate on the attack qubits and listen for CNOTs. Then, apply H-again before measuring to get the phase noise.
- We also see that the time window cannot be too small. We can see significant noise starting from snooping durations 25% the size of the CNOT.

## Experiment - 2
### Aim
Can we detect how many CNOTs are being applied in the same time window?


## Questions to be answered

- [x] Is CNOT crosstalk causing X-flips or Z-flips?
- [x] How small can I make my window size and detect a CNOT?
- [ ] Can I detect the start of a CNOT?
- [ ] What if the CNOT happens in the middle of the snooping window?
- [ ] How much does distance effect crosstalk?
- [ ] Can we make the window size very small and find the exact instance when the CNOT was started?
- [ ] Can we use the CNOT gate durations to determine what CNOTs were applied?
- [ ] Try windows smaller than 160dt?
<!-- - Can we use [pulse gates](https://qiskit.org/documentation/tutorials/circuits_advanced/05_pulse_gates.html) to be more sensitve or disrupt other user's computation. -->


## TODO:

1. Time windowed snooping with mid-circuit measurement to determine if there was a CNOT in that window.
2. Discuss - Shots vs Repeat experiment for more data points. Do 100k shots - split into 20k random samples = 5 repetitions? This might help us run more experiments per job.
3. config.channels??
4. what is config.meas_levels?

## Future Experiment Ideas

- How much of the CNOT single do we need to see to detect it? How small can the snooping duration be?
    What factors does this depend on?
        1. Is every CNOT different
        2. Does distance to the qubits matter?
- Run on different backends
- Assign victim and attacker qubits randomly
- How much does distance matter?