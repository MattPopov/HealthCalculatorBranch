athlete='соотвествует результату тренированного атлета'
excellent='отличный результат'
good='хороший результат' 
abov_av='результат выше среднего'
aver='результат в пределах нормы'
belo_av='результат ниже среднего'
poor='плохой результат'
very_poor='очень плохой результат'
def heart_st():
    age=int(input('Введите Ваш возраст: '))
    gender=input('Введите Ваш пол: ')
    def rhr(age, gender):
        hrate=int(input('Введите Ваш пульс в состоянии покоя: '))
        if gender=='Мужской' or gender=='мужской':
            if age>17 and age<26:
                if hrate>48 and hrate<56:
                    rhr_=athlete
                elif hrate>55 and hrate<62:
                    rhr_=excellent
                elif hrate>61 and hrate<66:
                    rhr_=good
                elif hrate>65 and hrate<70:
                    rhr_=abov_av
                elif hrate>69 and hrate<74:
                    rhr_=aver
                elif hrate>73 and hrate<82:
                    rhr_=belo_av
                elif hrate>81:
                    rhr_=poor
            elif age>25 and age<36:
                if hrate>48 and hrate<55:
                    rhr_=athlete
                elif hrate>54 and hrate<62:
                    rhr_=excellent
                elif hrate>61 and hrate<66:
                    rhr_=good
                elif hrate>65 and hrate<71:
                    rhr_=abov_av
                elif hrate>70 and hrate<75:
                    rhr_=aver
                elif hrate>74 and hrate<82:
                    rhr_=belo_av
                elif hrate>81:
                    rhr_=poor
            elif age>35 and age<46:
                if hrate>49 and hrate<57:
                    rhr_=athlete
                elif hrate>56 and hrate<63:
                    rhr_=excellent
                elif hrate>62 and hrate<67:
                    rhr_=good
                elif hrate>66 and hrate<71:
                    rhr_=abov_av
                elif hrate>70 and hrate<76:
                    rhr_=aver
                elif hrate>75 and hrate<83:
                    rhr_=belo_av
                elif hrate>82:
                    rhr_=poor
            elif age>45 and age<56:
                if hrate>49 and hrate<58:
                    rhr_=athlete
                elif hrate>57 and hrate<64:
                    rhr_=excellent
                elif hrate>63 and hrate<68:
                    rhr_=good
                elif hrate>67 and hrate<72:
                    rhr_=abov_av
                elif hrate>71 and hrate<77:
                    rhr_=aver
                elif hrate>76 and hrate<84:
                    rhr_=belo_av
                elif hrate>83:
                    rhr_=poor
            elif age>55 and age<66:
                if hrate>50 and hrate<57:
                    rhr_=athlete
                elif hrate>56 and hrate<62:
                    rhr_=excellent
                elif hrate>61 and hrate<68:
                    rhr_=good
                elif hrate>67 and hrate<72:
                    rhr_=abov_av
                elif hrate>71 and hrate<76:
                    rhr_=aver
                elif hrate>75 and hrate<82:
                    rhr_=belo_av
                elif hrate>81:
                    rhr_=poor
            elif age>65:
                if hrate>49 and hrate<56:
                    rhr_=athlete
                elif hrate>55 and hrate<62:
                    rhr_=excellent
                elif hrate>61 and hrate<66:
                    rhr_=good
                elif hrate>65 and hrate<70:
                    rhr_=abov_av
                elif hrate>69 and hrate<74:
                    rhr_=aver
                elif hrate>73 and hrate<80:
                    rhr_=belo_av
                elif hrate>79:
                    rhr_=poor
        elif gender=='Женский' or gender=='женский':
            if age>17 and age<26:
                if hrate>53 and hrate<61:
                    rhr_=athlete
                elif hrate>60 and hrate<66:
                    rhr_=excellent
                elif hrate>65 and hrate<70:
                    rhr_=good
                elif hrate>69 and hrate>74:
                    rhr_=abov_av
                elif hrate>73 and hrate<79:
                    rhr_=aver
                elif hrate>78 and hrate<85:
                    rhr_=belo_av
                elif hrate>84:
                    rhr_=poor
            elif age>25 and age<36:
                if hrate>53 and hrate<60:
                    rhr_=athlete
                elif hrate>59 and hrate<65:
                    rhr_=excellent
                elif hrate>64 and hrate<69:
                    rhr_=good
                elif hrate>68 and hrate<73:
                    rhr_=abov_av
                elif hrate>72 and hrate<77:
                    rhr_=aver
                elif hrate>76 and hrate<83:
                    rhr_=belo_av
                elif hrate>82:
                    rhr_=poor
            elif age>35 and age<46:
                if hrate>53 and hrate<60:
                    rhr_=athlete
                elif hrate>59 and hrate<65:
                    rhr_=excellent
                elif hrate>64 and hrate<70:
                    rhr_=good
                elif hrate>69 and hrate<74:
                    rhr_=abov_av
                elif hrate>73 and hrate<79:
                    rhr_=aver
                elif hrate>78 and hrate<85:
                    rhr_=belo_av
                elif hrate>84:
                    rhr_=poor
            elif age>45 and age<56:
                if hrate>53 and hrate<61:
                    rhr_=athlete
                elif hrate>60 and hrate<66:
                    rhr_=excellent
                elif hrate>65 and hrate<70:
                    rhr_=good
                elif hrate>69 and hrate<74:
                    rhr_=abov_av
                elif hrate>73 and hrate<78:
                    rhr_=aver
                elif hrate>77 and hrate<84:
                    rhr_=belo_av
                elif hrate>83:
                    rhr_=poor
            elif age>55 and age<66:
                if hrate>53 and hrate<60:
                    rhr_=athlete
                elif hrate>59 and hrate<65:
                    rhr_=excellent
                elif hrate>64 and hrate<69:
                    rhr_=good
                elif hrate>68 and hrate<74:
                    rhr_=abov_av
                elif hrate>73 and hrate<78:
                    rhr_=aver
                elif hrate>77 and hrate<84:
                    rhr_=belo_av
                elif hrate>83:
                    rhr_=poor
            elif age>65:
                if hrate>53 and hrate<60:
                    rhr_=athlete
                elif hrate>59 and hrate<65:
                    rhr_=excellent
                elif hrate>64 and hrate<69:
                    rhr_=good
                elif hrate>68 and hrate<73:
                    rhr_=abov_av
                elif hrate>72 and hrate<77:
                    rhr_=aver
                elif hrate>76 and hrate<85:
                    rhr_=belo_av
                elif hrate>83:
                    rhr_=poor
        print(f'Ваш пульс в состоянии покоя: {rhr_}')
    rhr(age, gender)
    input()
    print('Cтеп-тест представляет собой разновидность сердечного стресс-теста для выявления и диагностики сердечно-сосудистых заболеваний.\n' +
          'Это также хороший показатель физической подготовки и способности человека восстанавливаться после интенсивных упражнений путем\n' +
          'проверки скорости восстановления.')
    
    def step_test(age, gender):
        cont=input("Введите 'Да', если хотите пройти степ-тест: ")
        while cont=='Да' or cont=='да':
            print()
            print('Перед началом теста разомнитесь в течение нескольких минут\n' +
              'Попросите помощника установить метроном на темп 24 шага в минуту\n' +
              "Попросите помощника дать команду 'вперёд' и запустить секундомер\n" +
              'Поднимайтесь на скамью или ступеньку высотой 30 см и спускайтесь по одной ноге за раз в течение 3 минут с частотой 24 шага в минуту\n' +
              'По окончании степ-теста запишите измерьте и запишите частоту сердечных сокращений, ударов в минуту')
            input()
            hrate_1=int(input('Введите Ваш пульс: '))
            if gender=='Мужской' or gender== 'мужской':
                if age>17 and age<26:
                    if hrate_1<79:
                        steptest=excellent
                    elif hrate_1>78 and hrate_1<90:
                        steptest=good
                    elif hrate_1>89 and hrate_1<100:
                        steptest=abov_av
                    elif hrate_1>99 and hrate_1<106:
                        steptest=aver
                    elif hrate_1>105 and hrate_1<117:
                        steptest=belo_av
                    elif hrate_1>116 and hrate_1<129:
                        steptest=poor
                    elif hrate_1>128:
                        steptest=very_poor
                elif age>25 and age<36:
                    if hrate_1<81:
                        steptest=excellent
                    elif hrate_1>80 and hrate_1<90:
                        steptest=good
                    elif hrate_1>89 and hrate_1<100:
                        steptest=abov_av
                    elif hrate_1>99 and hrate_1<108:
                        steptest=aver
                    elif hrate_1>107 and hrate_1<118:
                        steptest=belo_av
                    elif hrate_1>117 and hrate_1<129:
                        steptest=poor
                    elif hrate_1>128:
                        steptest=very_poor
                elif age>35 and age<46:
                    if hrate_1<83:
                         steptest=excellent
                    elif hrate_1>82 and hrate_1<97:
                         steptest=good
                    elif hrate_1>96 and hrate_1<104:
                        steptest=abov_av
                    elif hrate_1>103 and hrate_1<113:
                        steptest=aver
                    elif hrate_1>112 and hrate_1<120:
                        steptest=belo_av
                    elif hrate_1>119 and hrate_1<131:
                        steptest=poor
                    elif hrate_1>130:
                        steptest=very_poor
                elif age>45 and age<56:
                    if hrate_1<87:
                        steptest=excellent
                    elif hrate_1>86 and hrate_1<98:
                         steptest=good
                    elif hrate_1>97 and hrate_1<106:
                        steptest=abov_av
                    elif hrate_1>105 and hrate_1<117:
                        steptest=aver
                    elif hrate_1>116 and hrate_1<123:
                        steptest=belo_av
                    elif hrate_1>122 and hrate_1<133:
                        steptest=poor
                    elif hrate_1>132:
                        steptest=very_poor
                elif age>55 and age<66:
                    if hrate_1<86:
                        steptest=excellent
                    elif hrate_1>85 and hrate_1<98:
                         steptest=good
                    elif hrate_1>97 and hrate_1<104:
                        steptest=abov_av
                    elif hrate_1>103 and hrate_1<113:
                        steptest=aver
                    elif hrate_1>112 and hrate_1<121:
                        steptest=belo_av
                    elif hrate_1>120 and hrate_1<130:
                        steptest=poor
                    elif hrate_1>129:
                        steptest=very_poor
                elif age>65:
                    if hrate_1<88:
                        steptest=excellent
                    elif hrate_1>87 and hrate_1<97:
                         steptest=good
                    elif hrate_1>96 and hrate_1<104:
                        steptest=abov_av
                    elif hrate_1>103 and hrate_1<114:
                        steptest=aver
                    elif hrate_1>113 and hrate_1<121:
                        steptest=belo_av
                    elif hrate_1>120 and hrate_1<131:
                        steptest=poor
                    elif hrate_1>130:
                        steptest=very_poor
            elif gender=='Женский' or gender=='женский':
                if age>17 and age<26:
                    if hrate_1<85:
                        steptest=excellent
                    elif hrate_1>84 and hrate_1<99:
                        steptest=good
                    elif hrate_1>98 and hrate_1<109:
                        steptest=abov_av
                    elif hrate_1>108 and hrate_1<118:
                        steptest=aver
                    elif hrate_1>117 and hrate_1<127:
                        steptest=belo_av
                    elif hrate_1>126 and hrate_1<141:
                        steptest=poor
                    elif hrate_1>140:
                        steptest=very_poor
                elif age>25 and age<36:
                    if hrate_1<88:
                        steptest=excellent
                    elif hrate_1>87 and hrate_1<100:
                        steptest=good
                    elif hrate_1>99 and hrate_1<112:
                        steptest=abov_av
                    elif hrate_1>111 and hrate_1<120:
                        steptest=aver
                    elif hrate_1>119 and hrate_1<127:
                        steptest=belo_av
                    elif hrate_1>126 and hrate_1<139:
                        steptest=poor
                    elif hrate_1>138:
                        steptest=very_poor
                elif age>35 and age<46:
                    if hrate_1<90:
                         steptest=excellent
                    elif hrate_1>89 and hrate_1<103:
                         steptest=good
                    elif hrate_1>102 and hrate_1<111:
                        steptest=abov_av
                    elif hrate_1>110 and hrate_1<119:
                        steptest=aver
                    elif hrate_1>118 and hrate_1<129:
                        steptest=belo_av
                    elif hrate_1>128 and hrate_1<141:
                        steptest=poor
                    elif hrate_1>140:
                        steptest=very_poor
                elif age>45 and age<56:
                    if hrate_1<94:
                        steptest=excellent
                    elif hrate_1>93 and hrate_1<105:
                         steptest=good
                    elif hrate_1>104 and hrate_1<116:
                        steptest=abov_av
                    elif hrate_1>115 and hrate_1<121:
                        steptest=aver
                    elif hrate_1>120 and hrate_1<130:
                        steptest=belo_av
                    elif hrate_1>129 and hrate_1<136:
                        steptest=poor
                    elif hrate_1>135:
                        steptest=very_poor
                elif age>55 and age<66:
                    if hrate_1<95:
                        steptest=excellent
                    elif hrate_1>94 and hrate_1<105:
                         steptest=good
                    elif hrate_1>104 and hrate_1<113:
                        steptest=abov_av
                    elif hrate_1>112 and hrate_1<119:
                        steptest=aver
                    elif hrate_1>118 and hrate_1<129:
                        steptest=belo_av
                    elif hrate_1>128 and hrate_1<140:
                        steptest=poor
                    elif hrate_1>139:
                        steptest=very_poor
                elif age>65:
                    if hrate_1<90:
                        steptest=excellent
                    elif hrate_1>89 and hrate_1<103:
                         steptest=good
                    elif hrate_1>102 and hrate_1<116:
                        steptest=abov_av
                    elif hrate_1>115 and hrate_1<123:
                        steptest=aver
                    elif hrate_1>122 and hrate_1<129:
                        steptest=belo_av
                    elif hrate_1>128 and hrate_1<135:
                        steptest=poor
                    elif hrate_1>134:
                        steptest=very_poor
            print(f'Ваш результат степ-теста: {steptest}')
            cont=input('Хотите ли Вы пройти степ-тест ещё раз ?: ')
    step_test(age, gender)
    
if __name__=='__main__':
    heart_st()
