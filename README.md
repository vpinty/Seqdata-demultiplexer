# seqdata_demultiplexer
Creates a simplified sequencing data demultiplexer. The tool receives a list of DNA sequences ([ACTG]*) which are split into groups based on prefix/postfix sequences defined in a simple configuration.

The tool receives the following input data:
 - path to the sequencing data file: text file, contains one sequence per line,
 - path to the configuration file: text file, each line contains the group name, sequence prefix and postfix separated by ws,
 - path prefix to the output files which serves as a base to generate output filenames for each group.

If a sequence has matching prefix and postfix it goes into the corresponding group. Sequences not matching any group go into the 'unmatched' group.

Example data:

sample.seq:
ACTCACGACCACTAACTAGCAATCAGTACAGTAACGATCG
CAGTAAGCGATCAGACAGTACAGATCAGTACAGTACGTACA
ACTCACGACCACTAACTGGCAATCAGTACAGTAACGATCG
AGACAACATCAGATCGCAAGACGACAGATACGATCAGACA

sample.conf:
group1 ACTCACG ACGATCG
group2 CAGTAAG ACGTACA

Expected output:

group1.seq:
ACTCACGACCACTAACTAGCAATCAGTACAGTAACGATCG
ACTCACGACCACTAACTGGCAATCAGTACAGTAACGATCG

group2.seq:
CAGTAAGCGATCAGACAGTACAGATCAGTACAGTACGTACA

unmatched.seq:
AGACAACATCAGATCGCAAGACGACAGATACGATCAGACA
