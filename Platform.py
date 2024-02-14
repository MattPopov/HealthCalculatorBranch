"""
@author: lataf 
@file: Platform.py 
@time: 11.02.2024 13:49
Модуль отвечает за консолидацию модулей
UML схема модуля
Сценарий работы модуля:
Тест модуля находится в папке model/tests.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class User:
    """Вводи и вывод данных пользователем """

    def __init__(self):
        self.health: Health = Health(self)  # ресурсы легких

    def input(self):
        ...

    @staticmethod
    def output(value):
        plt.show()
        print(f'Сердце - {value}')


class Health:
    """Управление объектами """

    def __init__(self, _user: User = None):
        self.user = _user  # Ссылка на родителя
        self.heart = Heart(self)  # ресурсы сердечно-сосудистой системы
        self.imt = IMT(self)  # индекс массы тела
        self.resp = Resp(self)  # ресурсы легких
        self.harrington = Harrington(self)  # перевод параметра в безразмерную величину

    @staticmethod
    def create_diagram():
        """Показываем диаграмму"""
        params = ['imt', 'heart', 'resp']
        results = [0.5, 0.8, 0.9, ]

        theta = np.linspace(start=0, stop=2 * np.pi, num=len(results), endpoint=False)
        theta = np.concatenate((theta, [theta[0]]))
        results = np.append(results, results[0])

        fig = plt.figure(figsize=(5, 5), facecolor='#f3f3f3')
        ax = fig.add_subplot(111, projection='polar')
        ax.plot(theta, results, linewidth=2, color="red")
        ax.set_thetagrids(range(0, 360, int(360 / len(params))), params)
        plt.yticks(np.arange(0, 1.1, 0.1), fontsize=8)
        ax.set(facecolor='#f3f3f3')
        ax.set_theta_offset(np.pi / 2)

        pl = ax.yaxis.get_gridlines()
        for line in pl:
            line.get_path()._interpolation_steps = 5
        # plt.show()


class Harrington:
    """Управление объектами """

    def __init__(self, _health: Health = None):
        self.h_bad = 0.20  # С
        self.h_good = 0.63  # С

    @staticmethod
    def calc(bad: float, good: float):
        print(bad, good)
        return bad, good


class IMT:
    """Управление объектами """

    def __init__(self, _health: Health = None):
        self.health = _health  # Ссылка на родителя


class Resp:
    """Управление объектами """

    def __init__(self, contr: Health = None):
        self.controller = contr  # Ссылка на родителя


class Heart:
    """Управление объектами """

    def __init__(self, _health: Health = None):
        self.health = _health  # Ссылка на родителя
        self.bad_pulse = None
        self.good_pulse = None

    def pulse(self, gender: str = 'women', age: int = 26):
        xls_file = pd.ExcelFile(r'heart.xlsx')  # Импорт excel файла
        df = xls_file.parse('Лист1')  # Создание DataFrame
        print(df)
        self.good_pulse = int(df.loc[(df['gender'] == gender) & (df['age'] >= age)]['good_pulse'].iloc[0])
        # Фильтруем по полу, возрасту и выводим первый [0] элемент серии значений как целое число
        self.bad_pulse = int(df.loc[(df['gender'] == gender) & (df['age'] >= age)]['bad_pulse'].iloc[0])
        print(f'good_pulse = {self.good_pulse}')
        print(f'bad_pulse = {self.bad_pulse}')

        # self.health.create_diagram()
        # self.health.user.output('хорошо')


if __name__ == '__main__':
    user_1 = User()  # Создаем объект
    user_1.health.heart.pulse()
    # user_1.health.harrington.calc(320, 430)
