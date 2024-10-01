
from threading import Thread
from datetime import datetime
from time import sleep

time_start = datetime.now()


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='UTF-8') as file:
        for word in range(1, word_count + 1):
            file.write(f"Какое-то слово № {word} \n")
            sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")
    pass


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_and = datetime.now()
time_result = time_and - time_start
print(f'Работа функции write_words {time_result}')

time_start = datetime.now()

write_words_1 = Thread(target=write_words, args=(10, 'example5.txt'))
write_words_2 = Thread(target=write_words, args=(30, 'example6.txt'))
write_words_3 = Thread(target=write_words, args=(200, 'example7.txt'))
write_words_4 = Thread(target=write_words, args=(100, 'example8.txt'))

write_words_1.start()
write_words_2.start()
write_words_3.start()
write_words_4.start()

write_words_1.join()
write_words_2.join()
write_words_3.join()
write_words_4.join()

time_and = datetime.now()
time_result = time_and - time_start
print(f'Работа потоков {time_result}')
