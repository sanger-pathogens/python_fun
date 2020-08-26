from pkg_resources import get_distribution, DistributionNotFound

from fun_lib.counting import compute_stats
from fun_lib.fasta import read_sequence_file
from fun_lib.writer import write_stats


def count(input_file, output_file, size):
    sequences = read_sequence_file(input_file)
    stats = compute_stats(size, sequences)
    write_stats(stats, output_file)


def fun_version():
    try:
        return get_distribution("fun").version
    except DistributionNotFound:
        return '<Unknown>'

