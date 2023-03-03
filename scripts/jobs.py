import os
import gzip

# fastp: quality filtering
def quality_filtering_inFile(in_file, data_id, fastp_path):
    os.system('mkdir -p ./metathermo_intermediates/{qf_fq,qf_report,fna,faa}')
    try:
        os.system("{} -i {} -o ./metathermo_intermediates/qf_fq/{}.qf.fq -3 -h ./metathermo_intermediates/qf_report/{}.html -j ./metathermo_intermediates/qf_report/{}.json -n 1 -w 1 -x 1>/dev/null".format(fastp_path, in_file, data_id, data_id, data_id))
    except Exception as e:
        print(e)


# seqkit: fastq -> fna
def fq_to_fna_inFile(in_file, data_id, seqkit_path):
    os.system('mkdir -p ./metathermo_intermediates/{fna,faa}')
    try:
        os.system("{} fq2fa {} -o ./metathermo_intermediates/fna/{}.fna 1>/dev/null".format(seqkit_path, in_file, data_id))
    except Exception as e:
        print(e)
    
def fq_to_fna_dataID(data_id, seqkit_path):
    try:
        os.system("{} fq2fa ./metathermo_intermediates/qf_fq/{}.qf.fq -o ./metathermo_intermediates/fna/{}.fna 1>/dev/null".format(seqkit_path, data_id, data_id))
    except Exception as e:
        print(e)

# prodigal: gene prediction
def gene_prediction_inFile(in_file, data_id, prodigal_path):
    os.system('mkdir -p ./metathermo_intermediates/faa')
    try:
        if in_file.endswith('.gz'):
            os.system('gunzip -c {} | {} -a ./metathermo_intermediates/faa/{}.faa -p meta 1>/dev/null 2>&1'.format(in_file, prodigal_path, data_id))
            
        else:
            os.system('{} -i {} -a ./metathermo_intermediates/faa/{}.faa -p meta 1>/dev/null 2>&1'.format(prodigal_path, in_file, data_id))
    except Exception as e:
        print(e)

def gene_prediction_dataID(data_id, prodigal_path):
    try:
        os.system('{} -i ./metathermo_intermediates/fna/{}.fna -a ./metathermo_intermediates/faa/{}.faa -p meta 1>/dev/null 2>&1'.format(prodigal_path, data_id, data_id))
    except Exception as e:
        print(e)


# MPT_calculation.py
path_scripts = os.path.dirname(__file__)
def temperature_prediction_inFile(in_file):
    try:
        os.system('python3 {}/MPTcalculation.py {} MPT_output.csv AA_output.txt'.format(path_scripts, in_file))
    except Exception as e:
        print(e)

def temperature_prediction_dataID(data_id):
    try:
        os.system('python3 {}/MPTcalculation.py ./metathermo_intermediates/faa/{}.faa MPT_output.csv AA_output.txt'.format(path_scripts, data_id))
    except Exception as e:
        print(e)
