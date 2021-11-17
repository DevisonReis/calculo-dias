from datetime import date

ano = int(input('Ano do seu nascimento: '))
mes = int(input('Mês do seu nascimento: '))
dia = int(input('Dia do seu nascimento: '))

print('-' * 40)

dias = date.today( ) - date(ano, mes, dia)

print(f'Hoje faz {dias.days} desde que você nasceu')