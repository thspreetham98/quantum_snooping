# Quantum Snooping

## Experiment - 1:
### Aim
1. Determine if crosstalk causes phase noise errors(Z-flips) or amplitude noise errors(X-flips).
2. Determine how snooping time window effects our ability to detect CNOTs
### Results
TODO: waiting for results

## Questions to be answered

- Is CNOT crosstalk causing X-flips or Z-flips?
- What if the CNOT happens in the middle of the snooping window?
- How small can I make my window size and detect a CNOT?
- Can I detect the start of a CNOT?
- How much does distance effect crosstalk?
- Can we make the window size very small and find the exact instance when the CNOT was started?
- Can we use the CNOT gate durations to determine what CNOTs were applied?
- Try windows smaller than 160dt?


## TODO:

1. Time windowed snooping with mid-circuit measurement to determine if there was a CNOT in that window.
2. Discuss - Shots vs Repeat experiment for more data points. Do 100k shots - split into 20k random samples = 5 repetitions? This might help us run more experiments per job.
3. config.channels??

## Future Experiment Ideas

- How much of the CNOT single do we need to see to detect it? How small can the snooping duration be?
    What factors does this depend on?
        1. Is every CNOT different
        2. Does distance to the qubits matter?
- Run on different backends
- Assign victim and attacker qubits randomly
- How much does distance matter?