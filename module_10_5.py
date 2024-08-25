import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    # Возврат списка не требуется по условиям задачи
    # return all_data

if __name__ == '__main__':
    # Список файлов для чтения скачан из архива подготовка
    filenames = [f'./file_{number}.txt' for number in range(1, 5)]  # Список файлов от file 1.txt до file 4.txt

    # Линейный вызов
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f"Линейный вызов занял: {linear_time} секунд")

    # Многопроцессный вызов
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_time = time.time() - start_time
    print(f"Многопроцессный вызов занял: {parallel_time} секунд")
