def read_and_write():
    with (open("ds.csv", "r") as file_input):
        with open("ds.tsv", "w") as file_output:
            file_output.write(file_input.read().replace('","', '"\t"')
                              .replace('false,', 'false\t')
                              .replace('true,', 'true\t')
                              .replace('",', '\t'))

if __name__ == "__main__":
    read_and_write()
