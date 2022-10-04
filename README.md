MetaThermo : Metagenomic Thermometer
====================================================

Metagenomic Thermometer is the tool for predicting the environmental temperature of metagenomic samples from metagenomic sequences.

Installation
---------------

### Requirements
MetaThermo requires python packages listed below to function correctly.

 * python>=3.6.5
 * numpy>=1.19.0

MetaThermo also requires several executables listed below.

 * fastp
 * seqkit
 * prodigal

### Install

```bash
git clone https://github.com/kuroppy/meta-thermo.git
cd meta-thermo
pip install .
```

Usage
-----

### Basic usage
```bash
python ../metathermo.py -f [input_file] -t [file_type]
```

### Input files
The following files can be used as input files, and file type must be declared after the -t (--type) option.
 * fastq [-t fastq]
 * quality filtered fastq [-t fastq_qf]
 * nucleotide fasta [-t fna]
 * amino acid fasta [-t faa]

Gzip compressed files also can be used with the --gz option.

### Specify absolute paths for executable programs
If the required executables do not exist in the directory through which the path passes, an absolute path must be provided.
```bash
python ../metathermo.py -f [input_file] -t [file_type] --gz --fastp [path_to_fastp] --seqkit [path_to_seqkit] --prodigal [path_to_prodigal]
```

## Example and output
Here is an example of analysis using `test.fastq` in the `test_data` directory. 
```bash
cd meta-thermo/test_data/
python ../metathermo.py -f test.fastq -t fastq
```
The following directories or files will be output to the current directory.
 * qf_fq/test.qf.fq
 * qf_report/test.html test.json
 * fna/test.fna
 * faa/test.faa
 * AA_output.txt (input filename and amino acid counts)
 * MPT_output.csv (input filename and Metagenomic Predicted Temperature)

```bash
cat AA_output.txt
./faa/test.faa{'*': 20, 'A': 1490, 'C': 168, 'D': 661, 'E': 853, 'F': 520, 'G': 1104, 'H': 313, 'I': 700, 'K': 530, 'L': 1411, 'M': 282, 'N': 455, 'P': 748, 'Q': 544, 'R': 1011, 'S': 743, 'T': 729, 'V': 1091, 'W': 201, 'X': 11, 'Y': 351}

cat MPT_output.csv
./faa/test.faa,43.57
```

MetaThermo web application
------------
MetaThermo processing can be performed online at http://metathermo.jp/.
You can also check the MetaThermo workflow at MetaThermo web page.

Publications
------------
 * Masaomi Kurokawa, Koichi Higashi, Keisuke Yoshida, Tomohiko Sato, Shigenori Maruyama, Hiroshi Mori, Ken Kurokawa (2022) Metagenomic Thermometer. bioRxiv https://doi.org/10.1101/2022.07.14.499854
