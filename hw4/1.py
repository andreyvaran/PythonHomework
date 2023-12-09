import threading
import multiprocessing
import time


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        print(n)
        return fibonacci(n - 1) + fibonacci(n - 2)


def run_fibonacci(n: int) -> float:
    start_time = time.time()
    fibonacci(n)
    return time.time() - start_time


def measure_time(method: str, n: int, runs: int) -> list[float]:
    times = []
    for _ in range(runs):
        if method == "process":
            process = multiprocessing.Process(target=run_fibonacci, args=(n,))
            process.start()
            start_time = time.time()
            process.join()
            times.append(time.time() - start_time)
        elif method == "thread":
            thread = threading.Thread(target=run_fibonacci, args=(n,))
            thread.start()
            start_time = time.time()
            thread.join()
            times.append(time.time() - start_time)
        else:
            times.append(run_fibonacci(n))
    return times


def main() -> None:
    n = 40
    runs = 1

    single_times = measure_time("single", n, runs)

    thread_times = measure_time("thread", n, runs)

    process_times = measure_time("process", n, runs)

    with open("artifacts/timing_results.txt", "w") as file:
        file.write("Single-threaded execution times:\n")
        file.write("\n".join(map(str, single_times)) + "\n")
        file.write("Multi-threaded execution times:\n")
        file.write("\n".join(map(str, thread_times)) + "\n")
        file.write("Multi-process execution times:\n")
        file.write("\n".join(map(str, process_times)) + "\n")


if __name__ == "__main__":
    main()
