from datetime import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            all_data.append(line)
            if not line:
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# линейный вызов (0:00:05.094283)
start = datetime.now()
for file in filenames:
    read_info(file)
end = datetime.now()
print(f'{end - start} - линейный')

# мультипроцессорный вызов (0:00:03.514228)
if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'{end - start} - многопроцессорный')
