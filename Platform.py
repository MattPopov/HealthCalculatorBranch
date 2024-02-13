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


class Site:
    """Вводи и вывод данных пользователем """

    def __init__(self):
        self.controller: Health = Health(self)  # ресурсы легких

    def input(self):
        ...

    @staticmethod
    def output(value):
        plt.show()
        print(f'Сердце - {value}')


class Health:
    """Управление объектами """

    def __init__(self, _site: Site = None):
        self.site = _site  # Ссылка на родителя
        self.heart = Heart(self)  # ресурсы сердечно-сосудистой системы
        self.imt = IMT(self)  # индекс массы тела
        self.resp = Resp(self)  # ресурсы легких

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

    def __init__(self, _controller: Health = None):
        self.controller = _controller  # Ссылка на родителя

    def calc(self):
        self.controller.create_diagram()
        self.controller.site.output('хорошо')


if __name__ == '__main__':
    site = Site()  # Создаем объект
    site.controller.heart.calc()
