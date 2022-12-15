'''
 ПРОЦЕНТ НА ДЕПОЗИТ

 

'''
first = 0
while first != 'x':

    period_vklada = int(input('На какой строк делаем вклад в месяцах - '))
    summa_vklada = float(input('Сумма вклада (грн) - '))
    procent_godovih = float(input('% годовых - ')) / 100.00
    s = summa_vklada
    do = 0
    raznica = 0
    mesachnie_dev = (summa_vklada * procent_godovih)
    for k in range(period_vklada):
        print(round(s,2),'UAH',raznica,'%','  месяц-',k)
        do = s
        s += (s * procent_godovih) / 12
        raznica = round((s / do) * 100 - 100, 2)
    print(s,'UAH',raznica,'%','  месяц-',period_vklada)
    print('-' * 50, '\n', '-' * 50)
    print('заработал грн - ',s - summa_vklada,'   заработал в процентах - ',(s / summa_vklada)*100 - 100)
    snatie_depozita = summa_vklada + ((summa_vklada * procent_godovih) / 12)*period_vklada
    print('прирост без снятия девидендов(грн) - ',s - snatie_depozita ,'грн разници(если бы снимал)',
          ' в % - ',(s / snatie_depozita)* 100 - 100)
    print('==========если снимать ещемесячно=============')
    print('Заработок в год - ', mesachnie_dev)
    print('Заработок в месяц - ', mesachnie_dev / 12)


    first = input('to return press enter    to exit  x  ')
