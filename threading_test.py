import multiprocessing
import math

def math_function(input):
    """Math function to calculate potential_threads and max_threads"""
    potential_threads = math.floor(input / 4)
    max_threads = min(potential_threads, num_cores - 1)
    return potential_threads, max_threads

def worker(process_id):
    """Function to be executed by each process"""
    print(f"Hello World from process {process_id}!")

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Number of CPU cores available: {num_cores}")

    input_value = 20  # Set your desired input value here

    potential_threads, max_threads = math_function(input_value)
    print(f"Potential threads: {potential_threads}")
    print(f"Max threads: {max_threads}")

    processes = []
    for i in range(max_threads):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)

    # Start the processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
