import zipfile
import json
from qiskit.result import Result, marginal_counts
import os
import tempfile
import shutil


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