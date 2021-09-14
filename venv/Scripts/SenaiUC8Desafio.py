from _datetime import datetime as dt
def converter(old):
    return dt.strptime(dt.strptime(old, '%Y/%m/%d'), '%d/%m/%Y')
DataEvento = input('Informe a data do evento [DD-MM-AAAA]: ')
DataAtual = dt.dt.date.today()
print(DataAtual, DataEvento)
