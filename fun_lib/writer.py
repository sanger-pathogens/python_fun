
def write_stats(stats, output_file):
    with open(output_file, "w") as file:
        write_stats_to_stream(stats, file)


def write_stats_to_stream(stats, file):
    for k, v in stats:
        file.write("%s: %d\n" % (k, v))
