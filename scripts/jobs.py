import os

# fastp: quality filtering
def quality_filtering_inFile(in_file, fastp_path):
    data_id = os.path.splitext(in_file)[0]
    os.system('mkdir -p ./qf_fq')
    os.system('mkdir -p ./qf_report')
    try:
        os.system("{} -i {} -o ./qf_fq/{}.qf.fq -3 -h ./qf_report/{}.html -j ./qf_report/{}.json -n 1 -w 1 -x 1>/dev/null".format(fastp_path, in_file, data_id, data_id, data_id))
    except Exception as e:
        print(e)


# seqkit: fastq -> fna
def fq_to_fna_inFile(in_file, seqkit_path):
    data_id = os.path.splitext(in_file)[0]
    os.system('mkdir -p ./fna')
    try:
        os.system("{} fq2fa {} -o ./fna/{}.fna 1>/dev/null".format(seqkit_path, in_file, data_id))
    except Exception as e:
        print(e)
    
def fq_to_fna_dataID(data_id, seqkit_path):
    os.system('mkdir -p ./fna')
    try:
        os.system("{} fq2fa ./qf_fq/{}.qf.fq -o ./fna/{}.fna 1>/dev/null".format(seqkit_path, data_id, data_id))
    except Exception as e:
        print(e)

# prodigal: gene prediction
def gene_prediction_inFile(in_file, prodigal_path):
    data_id = os.path.splitext(in_file)[0]
    os.system('mkdir -p ./faa')
    os.system('{} -i {} -a ./faa/{}.faa -p meta 1>/dev/null 2>&1'.format(prodigal_path, in_file, data_id))

def gene_prediction_dataID(data_id, prodigal_path):
    os.system('mkdir -p ./faa')
    os.system('{} -i ./fna/{}.fna -a ./faa/{}.faa -p meta 1>/dev/null 2>&1'.format(prodigal_path, data_id, data_id))


# MPT_calculation.py
path_scripts = os.path.dirname(__file__)
def temperature_prediction_inFile(in_file):
    os.system('python3 {}/MPTcalculation.py {} MPT_output.txt AA_output.txt'.format(path_scripts, in_file))

def temperature_prediction_dataID(data_id):
    os.system('python3 {}/MPTcalculation.py ./faa/{}.faa MPT_output.txt AA_output.txt'.format(path_scripts, data_id))
