import sys
import psutil

def read_lines(path_file):
    with open(path_file, 'r') as file:
        return file.readlines()

def main():
    if len(sys.argv) == 2:
        process = psutil.Process()
        file_lines = read_lines(sys.argv[1])
        for line in file_lines:
            pass
        pick_memory = process.memory_info().rss
        cpu_time = process.cpu_times().user + process.cpu_times().system
        print(f'Peak Memory Usage = {(pick_memory / 1024 ** 3):.3f} GB')
        print(f'User Mode Time + System Mode Time = {cpu_time:.2f}s')

if __name__ == "__main__":
    main()
