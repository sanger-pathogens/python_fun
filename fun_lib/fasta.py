
def read_sequences(stream):
    reads = []
    for line in stream:
        data = line.strip("\n")
        if len(data) == 0:
            continue
        if data.startswith('>'):
            reads.append("")
        else:
            reads[-1] += data
    return reads


def read_sequence_file(filename):
    with open(filename, 'r') as sequence_file:
        return read_sequences(sequence_file)