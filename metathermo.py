#!usr/bin/env python
#-*- coding: utf-8 -*-
import os
import argparse
import numpy as np
import scripts.jobs as jobs

# setting arguments
p = argparse.ArgumentParser()
p.add_argument('-f', '--file', required=True, help='Input file path.')
p.add_argument('-t', '--type', choices=['fastq', 'fastq_qf', 'fna', 'faa'], help='input file type', required=True)
p.add_argument('--gz', help='This argument is required when input file is gzipped file.', action='store_true')
p.add_argument('--fastp', default='fastp', help='Absolute path for fastp')
p.add_argument('--seqkit', default='seqkit', help='Absolute path for seqkit')
p.add_argument('--prodigal', default='prodigal', help='Absolute path for prodigal')
args = p.parse_args()

in_file = args.file
fastp_path = args.fastp
seqkit_path = args.seqkit
prodigal_path = args.prodigal


# call job scripts
def run_job_fastq(in_file):
    jobs.quality_filtering_inFile(in_file, fastp_path)
    jobs.fq_to_fna_dataID(data_id, seqkit_path)
    jobs.gene_prediction_dataID(data_id, prodigal_path)
    jobs.temperature_prediction_dataID(data_id)

def run_job_fastq_qf(in_file):
    jobs.fq_to_fna_inFile(in_file, seqkit_path)
    jobs.gene_prediction_dataID(data_id, prodigal_path)
    jobs.temperature_prediction_dataID(data_id)

def run_job_fna(in_file):
    jobs.gene_prediction_inFile(in_file, prodigal_path)
    jobs.temperature_prediction_dataID(data_id)

def run_job_faa(in_file):
    jobs.temperature_prediction_inFile(in_file)


# unzip in case of --gz option
if args.gz == True:
	os.system('gunzip {in_file}'.format(in_file = args.file))
	data_id = os.path.basename(in_file).split(".", 1)[0]
	in_file = os.path.splitext(in_file)[0]
else:
	data_id = os.path.splitext(in_file)[0]


# Determination of processing according to extensions
if args.type == 'fastq':
	run_job_fastq(in_file)
elif args.type == 'fastq_qf':
	run_job_fastq(in_file)
elif args.type == 'fna':
	run_job_fastq(in_file)
elif args.type == 'faa':
	run_job_fastq(in_file)
else:
	print('Submission failed. Inappropriate file.')