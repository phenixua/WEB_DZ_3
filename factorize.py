import time
import multiprocessing


def factorize(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize_parallel(numbers):
    with multiprocessing.Pool() as pool:
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

'''
Число 128: [1, 2, 4, 8, 16, 32, 64, 128]
Число 255: [1, 3, 5, 15, 17, 51, 85, 255]
Число 99999: [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
Число 10651060: [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
Час виконання синхронної версії: 1.4640026092529297 секунд
Число 128: [1, 2, 4, 8, 16, 32, 64, 128]
Число 255: [1, 3, 5, 15, 17, 51, 85, 255]
Число 99999: [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
Число 10651060: [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
Час виконання паралельної версії: 2.2489986419677734 секунд
'''
