import math
import concurrent.futures
import multiprocessing
import time
import logging


def integrate(f, a, b, *, n_jobs=1, n_iter=100000):
    step = (b - a) / n_iter
    total_steps = range(n_iter)

    def integrate_step(i):
        return f(a + i * step) * step

    if n_jobs == 1:
        return sum(integrate_step(i) for i in total_steps)
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=n_jobs) as executor:
            results = list(executor.map(integrate_step, total_steps))
        return sum(results)


def measure_time_and_log(executor_type, n_jobs, f, a, b):
    start_time = time.time()
    if executor_type == "thread":
        result = integrate(f, a, b, n_jobs=n_jobs)
    elif executor_type == "process":
        result = integrate(f, a, b, n_jobs=n_jobs)
    end_time = time.time()

    logging.info(f"Executor: {executor_type}, n_jobs: {n_jobs}, Result: {result}, Time: {end_time - start_time}")
    return end_time - start_time


def main():
    logging.basicConfig(filename='artifacts/integration_log.txt', level=logging.INFO,
                        format='%(asctime)s: %(message)s')

    n_jobs_range = range(1, 8)
    results = []

    for n_jobs in n_jobs_range:
        time_thread = measure_time_and_log("thread", n_jobs, math.cos, 0, math.pi / 2)
        time_process = measure_time_and_log("process", n_jobs, math.cos, 0, math.pi / 2)
        results.append((n_jobs, time_thread, time_process))

    with open('artifacts/2_timing_results.txt', 'w') as f:
        for n_jobs, time_thread, time_process in results:
            f.write(f'n_jobs: {n_jobs}, Thread Time: {time_thread}, Process Time: {time_process}\n')


if __name__ == "__main__":
    main()
