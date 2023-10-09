import time
import multiprocessing

def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize_parallel(numbers):
    num_cores = multiprocessing.cpu_count()  # Отримуємо кількість доступних ядер
    with multiprocessing.Pool(processes=num_cores) as pool:
        return pool.map(factorize, numbers)

if __name__ == "__main__":
    test_numbers = [128, 255, 99999, 10651060]

    # Вимірюємо час для синхронної версії
    start_time = time.time()
    results_sync = [factorize(num) for num in test_numbers]
    end_time = time.time()
    execution_time_sync = end_time - start_time

    # Виводимо результати та час для синхронної версії
    for i, num in enumerate(test_numbers):
        print(f"Число {num}: {results_sync[i]}")
    print(f"Час виконання синхронної версії: {execution_time_sync} секунд")

    # Вимірюємо час для паралельної версії
    start_time = time.time()
    results_parallel = factorize_parallel(test_numbers)
    end_time = time.time()
    execution_time_parallel = end_time - start_time

    # Виводимо результати та час для паралельної версії
    for i, num in enumerate(test_numbers):
        print(f"Число {num}: {results_parallel[i]}")
    print(f"Час виконання паралельної версії: {execution_time_parallel} секунд")
