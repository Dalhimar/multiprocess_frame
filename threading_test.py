import multiprocessing

def worker(process_id):
    """Function to be executed by each process"""
    print(f"Hello World from process {process_id}!")

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    print(f"Number of CPU cores available: {num_cores}")

    processes = []
    for i in range(num_cores-1):
        process = multiprocessing.Process(target=worker, args=(i,))
        processes.append(process)

    # Start the processes
    for process in processes:
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()

