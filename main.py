
from application import salary
from application.db import people
from datetime import datetime
import matplotlib as ml

ver_matlib = ml._get_version()


# Запись версии библиотеки Matplotlib
# with open("requirements.txt", "a") as f:
#   f.write(f"Версия Matplotlib: {ver_matlib}")







person_salary = salary.calculate_salary
persons_in_firm = people.get_employees
today_time = datetime.now()




if __name__ == '__main__':
  person_salary("Mike", "10000")
  persons_in_firm("Coca-cola", "2000")
  print(today_time)