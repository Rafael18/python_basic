import datetime

agora = datetime.datetime.now()

date_hoje = datetime.date.today()

futuro = date_hoje + datetime.timedelta(days=10)

passado = date_hoje - datetime.timedelta(days=13)

hora_agora = agora.time()

print(hora_agora)
