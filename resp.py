best = 'отлично'
good = 'хорошо'
udovl = 'удовлетворительно'
bad = 'плохо'
def respiratory():
    gender = input('Введите ваш пол: ')
    def proba(gender):
        time=int(input('Введите время задержки воздуха на вдохе в секундах: '))
        if gender=='Мужской' or gender=='мужской':
            if time<35:
                rproba=bad
            elif time>=35 and time<=45:
                rproba=udovl
            elif time>45 and time<=60:
                rproba=good
            else:
                rproba=best
        elif gender=='Женский' or gender=='женский':
            if time<29:
                rproba=bad
            elif time>=29 and time<=40:
                rproba=udovl
            elif time>40 and time<=55:
                rproba=good
            else:
                rproba=best
        print('Ваш результат:',rproba)
    proba(gender)
print('Cделайте 2-3 глубоких вдоха и выдоха, а затем, сделав полный вдох, задержите дыхание')
print('По окончании времени, нажмите на любую кнопку')
input()
respiratory()