from models import Drivers

driver = Drivers.query.first()
print(f"""Имя: {driver.name}
Номер паспорта: {driver.pass_number}
Серия паспорта: {driver.pass_series}
Мето выдачи паспорта: {driver.place_issue}
Дата выдачи паспорта: {driver.date_issue}
Дата прибытия в Шахово: {driver.date_arrive}
""")