##-------------------------------------------------------------##
## DATA, HORARIO E RELACIONAR DATAS DIFERENTES
##-------------------------------------------------------------##

from datetime import date, time, datetime, timedelta

def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(type(data_atual))
    print(data_atual_str)

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario)
    print(horario_str)

def trabalhando_com_datetime():
    data_atual_d = datetime.now()
    print(data_atual_d)
    print(data_atual_d.strftime('%d/%m/%Y %H:%M:%S'))
    print(data_atual_d.strftime('%c'))

    print(data_atual_d.day)
    print(data_atual_d.year)
    print(data_atual_d.minute)
    print(data_atual_d.weekday())

    tupla = ('seg', 'ter', 'qua', 'qui', 'sex', 'sab', 'dom')
    print(tupla[data_atual_d.weekday()])

    #criar data
    data_criada = datetime(2018, 6, 21, 11, 23)
    print(data_criada)
    print(data_criada.strftime('%c'))

    #converter data
    data_string = '01/01/2019'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y')
    print(type(data_convertida))
    print(data_convertida.day)

    #subtrair datas
    nova_data = data_convertida - timedelta(days=365)
    print(nova_data)

if __name__ == '__main__':
    #trabalhando_com_date()
    #trabalhando_com_time()
    trabalhando_com_datetime()