"""
@author: lataf 
@file: Platform.py 
@time: 11.02.2024 13:49
Модуль отвечает за консолидацию модулей
UML схема модуля
Сценарий работы модуля:
Тест модуля находится в папке model/tests.
"""
import math

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

    # @staticmethod
    @staticmethod
    def create_diagram(par: list, res: list):
        """Показываем диаграмму"""
        params = par
        results = res

        theta = np.linspace(start=0, stop=2 * np.pi, num=len(results), endpoint=False)
        theta = np.concatenate((theta, [theta[0]]))
        results = np.append(results, results[0])
        fig, (a0, a1) = plt.subplots(1, 2, gridspec_kw={'width_ratios': [2, 1]},
                                     figsize=(10, 5), facecolor='#f3f3f3')
        a0.axes.get_xaxis().set_visible(False)  # Убираем надписи на осях
        a0.axes.get_yaxis().set_visible(False)
        a1.axes.get_xaxis().set_visible(False)
        a1.axes.get_yaxis().set_visible(False)
        ax = fig.add_subplot(121, projection='polar')
        ax.plot(theta, results, linewidth=2, color="red")
        ax.set_thetagrids(range(0, 360, int(360 / len(params))), params)
        plt.yticks(np.arange(0, 110, 10), fontsize=10)
        ax.set(facecolor='#f3f3f3')
        ax.set_theta_offset(np.pi / 2)
        pl = ax.yaxis.get_gridlines()
        for line in pl:
            line.get_path()._interpolation_steps = 5

        text_block = Health.text_block(params, results)

        plt.subplot(1, 2, 2)
        plt.text(0.05, 0.5, text_block, fontsize=14)  # Выводим сводный показатель и отдельные показатели
        plt.show()

    @staticmethod
    def text_block(par, res):
        health = int(round(math.prod(res) ** (1 / len(res)), 0))  # Обобщенный показатель Харрингтона
        header = f"Всего здоровье {health}%\n"  # Заголовок - обобщенный показатель Харрингтона
        parameters = ''  # Показатели здоровья
        for i in range(len(res) - 1):
            parameters += f'    {i + 1}.  {par[i]} {res[i]}%\n'  # Собираем все показатели в строку
        text_block = f'{header}{parameters}'
        return text_block


class Harrington:
    """Управление объектами """

    def __init__(self, _health: Health = None):
        """Ахназарова С.Л., Кафаров В.В.; Методы оптимизации эксперимента в химической технологии;1985, с.209"""
        # self.h_good = 0.755 # Хороший результат по Харрингтону b_0 + b_1 * y_good = h_good (Уравнение 1)
        self.h_good = -math.log(math.log(1 / 0.63))  # Хороший результат по Харрингтону b_0 + b_1*y_good = h_good (1)
        # self.h_bad = -0.326 # Плохой результат по Харрингтону b_0 + b_1 * y_bad = h_bad (Уравнение 2)
        self.h_bad = -math.log(math.log(1 / 0.20))  # Плохой результат по Харрингтону b_0 + b_1 * y_bad = h_bad (2)
        self.b_0: float = 0  # Первый коэффициент в уравнении Харрингтона
        self.b_1: float = 0  # Второй коэффициент в уравнении Харрингтона
        self.d: float = 0  # Частная функция желательности Харрингтона для параметра y
        self.health = _health  # Ссылка на родителя
        self.y_max = 25
        self.y_min = 18.5
        self.current_IMT = None
        self.param = 20.5
        self.d_param = 0.75
        self.y1 = None
        self.y = None
        self.n = None

    def calc(self, y_good: float, y_bad: float, y: float):
        """ Ахназарова с. 207   d = exp [—ехр(— у')]  у’ = bo + b1 * у' """
        self.b_1 = (self.h_good - self.h_bad) / (y_good - y_bad)  # Считаем b_1 из уравнений (1) и (2)
        self.b_0 = self.h_good - self.b_1 * y_good  # Считаем b_0 из уравнений (1) и (2)
        self.d = math.exp(-math.exp(-(self.b_0 + self.b_1 * y)))  # Считаем d по Ахназаровой с.207
        # print('h_good ', self.h_good)
        # print('h_bad ', self.h_bad)
        # print('b_1 ', self.b_1)
        # print('b_0', self.b_0)
        # print('d', self.d)
        return self.d

    def calc2(self, x: float):
        self.y1 = (2 * self.param - (self.y_max + self.y_min)) / (self.y_max - self.y_min)
        self.n = (math.log(math.log(1 / self.d_param))) / (math.log(math.fabs(self.y1)))
        self.y = (2 * x - (self.y_max + self.y_min)) / (self.y_max - self.y_min)
        self.d = math.exp(-(math.fabs(self.y) ** self.n))
        return self.d


class IMT:
    """Управление объектами """

    def __init__(self, _health: Health = None):
        self.health = _health  # Ссылка на родителя
        self.current_height = None
        self.current_weight = None
        self.current_IMT = None
        self.d_IMT = None

    def imt(self, height: float, weight: float):
        self.current_height = height
        self.current_weight = weight
        self.current_IMT = round(self.current_weight/(self.current_height ** 2), 2)
        self.d_IMT = round(self.health.harrington.calc2(self.current_IMT) * 100)
        return self.d_IMT


class Resp:
    """Управление объектами """

    def __init__(self, _health: Health = None):
        self.health = _health
        self.good_time = None
        self.bad_time = None
        self.current_time = None
        self.d_time = None
        xls_file = pd.ExcelFile(r'resp.xlsx')
        self.df = xls_file.parse('Лист1')

    def time(self, gender, time):
        df = self.df
        self.good_time = int(df.loc[(df['gender'] == gender)]['good_time'].iloc[0])
        self.bad_time = int(df.loc[(df['gender'] == gender)]['bad_time'].iloc[0])
        self.current_time = time
        self.d_time = round(self.health.harrington.calc(self.good_time, self.bad_time, self.current_time) * 100)
        return self.d_time
        # print(f'gender\t{gender},\ttime\t{time},\td_time\t{self.d_time}%')


class Heart:
    """Загрузка данных и расчет показателя пульса по Харрингтону """

    def __init__(self, _health: Health = None):
        self.health = _health  # Ссылка на родителя
        self.good_pulse = None  # Хороший пульс
        self.bad_pulse = None  # Плохой пульс
        self.current_pulse = None  # Текущий пульс
        self.d_pulse = None  # Показатель Харрингтона
        xls_file = pd.ExcelFile(r'heart.xlsx')  # Импорт excel файла
        self.df = xls_file.parse('Лист1')  # Создание DataFrame

    def pulse(self, gender, age, pulse):
        df = self.df
        self.good_pulse = int(df.loc[(df['gender'] == gender) & (df['age'] >= age)]['good_pulse'].iloc[0])
        # Фильтруем по полу, возрасту и выводим первый [0] элемент серии значений как целое число
        self.bad_pulse = int(df.loc[(df['gender'] == gender) & (df['age'] >= age)]['bad_pulse'].iloc[0])
        self.current_pulse = pulse
        self.d_pulse = round(self.health.harrington.calc(self.good_pulse, self.bad_pulse, self.current_pulse) * 100)
        return self.d_pulse
        # print(f'gender\t{gender},\tage\t{age},\tpulse\t{pulse},\td_pulse\t{self.d_pulse}%')

        # self.health.create_diagram()
        # self.health.user.output('хорошо')


if __name__ == '__main__':
    user_1 = User()  # Создаем объект Пользователь
    # print(user_1.health.heart.df)
    # user_1.health.heart.pulse('women', 26, 79)
    user_2 = User()  # Создаем объект Пользователь
    # user_2.health.heart.pulse('man', 36, 50)

    print('Показатели Харрингтона и диаграмма здоровья отрисованы')
    user_1.health.create_diagram(['ИМТ', 'Сердце', 'Легкие'], [user_1.health.imt.imt(1.98, 101),
                                                               user_1.health.heart.pulse('women', 66, 42),
                                                               user_1.health.resp.time('women', 59)])

    user_2.health.create_diagram(['ИМТ', 'Сердце', 'Легкие'], [user_2.health.imt.imt(1.98, 101),
                                                               user_2.health.heart.pulse('man', 25, 70),
                                                               user_2.health.resp.time('man', 29)])

    # print('user_1')
    # print('y = 430, d = ', round(user_1.health.harrington.calc(430, 320, 430), 3))
    # print('y = 320, d = ', round(user_1.health.harrington.calc(430, 320, 320), 3))
    # print('y = 520, d = ', round(user_1.health.harrington.calc(430, 320, 520), 3))
    # print('y = 270, d = ', round(user_1.health.harrington.calc(430, 320, 270), 3))
    #
    # print('user_2')
    # print('y = 200, d = ', round(user_2.health.harrington.calc(200, 100, 200), 3))
    # print('y = 100, d = ', round(user_2.health.harrington.calc(200, 100, 100), 3))
    # print('y = 300, d = ', round(user_2.health.harrington.calc(200, 100, 300), 3))
    # print('y = 70, d = ', round(user_2.health.harrington.calc(200, 100, 70), 3))
    # print('y = 1000, d = ', round(user_2.health.harrington.calc(200, 100, 1000), 3))
    # print('y = 10, d = ', round(user_2.health.harrington.calc(200, 100, 0), 3))

    # print('b_1 = ', round(user_1.health.harrington.b_1, 4))
    # print('b_0 = ', round(user_.health.harrington.b_0, 4))
    # print('ln (ln 1/0.63) = ', round(-math.log(math.log(1 / 0.63)), 3))
    # print('ln (ln 1/0.20) = ', round(-math.log(math.log(1 / 0.20)), 3))
    # print('ln (e) = ', math.log(math.e))
    # print(round(1/math.e, 3))
