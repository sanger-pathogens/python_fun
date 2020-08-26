from collections import defaultdict


def kmer_count(size, sequences):
    result = defaultdict(lambda: 0)
    for sequence in sequences:
        while len(sequence) >= size:
            result[sequence[:size]] += 1
            sequence = sequence[1:]
    return dict(result)


def sort_stats(stats):
    sort_by_count_reverse = sorted(stats.items(), key=lambda item: item[1], reverse=True)
    return sort_by_count_reverse


def compute_stats(size, sequences):
    return sort_stats(kmer_count(size, sequences))