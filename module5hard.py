import time
import hashlib


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        hash_password = hashlib.sha256(password.encode('utf-8')).digest()
        for user in self.users:
            if nickname == user.nickname and hash_password == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int):
        hash_password = hashlib.sha256(password.encode('utf-8')).digest()
        new_user = User(nickname, hash_password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.log_out()
            self.log_in(nickname, password)
        else:
            print(f"Пользователь {nickname} уже существует")

    def log_out(self):
        self.current_user = None

    def get_titels_videos(self):
        list_titels = []
        for video in self.videos:
            list_titels.append(video.title)
        return list_titels

    def add(self, *args):
        for movie in args:
            if movie.title not in self.get_titels_videos():
                self.videos.append(movie)

    def get_videos(self, text: str):
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie: str):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if movie == video.title:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for i in range(video.time_now+1, video.duration):
                            print(i, end=' ')
                            time.sleep(1)
                        print('Конец видео')

    def __str__(self):
        return f"{self.videos}"


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"{self.title}"


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)


if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
