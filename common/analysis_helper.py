import zipfile
import json
from qiskit.result import Result, marginal_counts
import os
import tempfile
import shutil
import matplotlib.pyplot as plt
import numpy as np


def get_results_from_zip(folder_path, job_id) -> Result:
    zipfile_path = os.path.join(folder_path, 'job-{}.zip'.format(job_id))
    result_fname = '{}-result.txt'.format(job_id)
    temp_dir = tempfile.mkdtemp()
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)
    with open(os.path.join(temp_dir, result_fname)) as f:
        data = json.load(f)
    result = Result.from_dict(data)
    shutil.rmtree(temp_dir)
    return result

def get_1_mcounts_per_qubit(atk_qbt_index, counts):
    m_counts = [marginal_counts(count, indices=[atk_qbt_index]).get('1', 0) for count in counts]
    return m_counts

def exp_1_diff_heatmap(attack_qubit_indices, delays, diff_percent_xs, diff_percent_zs, cnots):
    # # Sample data - replace this with your actual data
    qubits = ['Qubit {}'.format(i) for i in attack_qubit_indices]
    experiments = ['Delay {} dt'.format(i) for i in delays]

    # Generate random data for each experiment
    data1 = np.array(diff_percent_xs)
    data2 = np.array(diff_percent_zs)

    # Calculate the common data range for both heatmaps
    data_min = min(data1.min(), data2.min())
    data_max = max(data1.max(), data2.max())

    # Create a figure with 1 row and 2 columns
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))  # 1 row, 2 columns
    fig.suptitle('IBM Lagos CNOT {}: Different snooping durations and basis'.format(cnots))

    # Determine a common scale for both heatmaps
    common_vmin = min(data_min, data2.min())
    common_vmax = max(data_max, data2.max())

    # Plot the first heatmap on the left subplot (ax[0])
    heatmap1 = ax[0].imshow(data1, cmap='viridis', aspect='auto', vmin=common_vmin, vmax=common_vmax)
    ax[0].set_title('Phase Flips')
    ax[0].set_xticks(np.arange(len(experiments)))
    ax[0].set_yticks(np.arange(len(qubits)))
    ax[0].set_xticklabels(experiments, rotation=45, ha='right')
    ax[0].set_yticklabels(qubits)

    # Display percentage values inside the boxes
    for i in range(len(qubits)):
        for j in range(len(experiments)):
            ax[0].text(j, i, f'{data1[i, j]:.2f}%', ha='center', va='center', color='w')

    # Plot the second heatmap on the right subplot (ax[1])
    heatmap2 = ax[1].imshow(data2, cmap='viridis', aspect='auto', vmin=common_vmin, vmax=common_vmax)
    ax[1].set_title('Amplitude Flips')
    ax[1].set_xticks(np.arange(len(experiments)))
    ax[1].set_yticks(np.arange(len(qubits)))
    ax[1].set_xticklabels(experiments, rotation=45, ha='right')
    ax[1].set_yticklabels(qubits)

    # Display percentage values inside the boxes
    for i in range(len(qubits)):
        for j in range(len(experiments)):
            ax[1].text(j, i, f'{data2[i, j]:.2f}%', ha='center', va='center', color='w')

    # Add colorbars to both heatmaps
    cbar1 = fig.colorbar(heatmap1, ax=ax[0])
    cbar2 = fig.colorbar(heatmap2, ax=ax[1])

    # Set labels for the colorbars
    cbar1.set_label('Percentage Difference in 1 counts')
    cbar2.set_label('Percentage Difference in 1 counts')

    # Adjust the layout to prevent clipping of the labels
    plt.tight_layout()

    return fig, ax

