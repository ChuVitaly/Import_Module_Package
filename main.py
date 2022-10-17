from application import salary
from application.db import people
from datetime import datetime
import numpy as np
import matplotlib as ml
import matplotlib.pyplot as plt

from dirty_main import *

# Tasks 1,2,3
person_salary = salary.calculate_salary
persons_in_firm = people.get_employees
today_time = datetime.now()

# Tasks 4
ver_matlib = ml._get_version()

# Запись версии библиотеки Matplotlib
# ---------------------------------------
# with open("requirements.txt", "a") as f:
#   f.write(f"Версия Matplotlib: {ver_matlib}")


# Программка с использованием Matplotlib
def salary_by_month():
    """
  Зарплата в течение года на графике
  return: graphic
  """
    plt.figure('Зарплата в течение года на графике')
    x = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    y = np.array([56000, 58400, 61300, 57500, 65000, 71000, 23000, 60000, 75000, 80000, 65300, 89500])
    lines = plt.plot(x, y, 'r--o')
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    person_salary("Mike", "10000")
    persons_in_firm("Coca-cola", "2000")
    print(today_time)
    salary_by_month()
