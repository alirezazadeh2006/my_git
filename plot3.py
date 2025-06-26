# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 13:39:19 2025

@author: AsusAliR
"""

import numpy as np
import matplotlib.pyplot as plt

# تعریف بردار x
x = np.linspace(-5, 5, 500)
y = x ** 3

# رسم ناحیه آبی کم‌رنگ از x = -5 تا 0 (بخش نزولی)
plt.axvspan(-5, 0, facecolor='white', alpha=0.3)

# رسم ناحیه آبی کم‌رنگ از x = 0 تا 5 (بخش صعودی)
plt.axvspan(0, 5, facecolor='white', alpha=0.3)

# رسم تابع x^3 با خط‌چین آبی
plt.plot(x, y, 'b--', label='x^3')

plt.fill_between(x, y, color='skyblue', alpha = 0.4)

# عنوان و برچسب‌ها
plt.title('Plot of x  3')
plt.xlabel('x')
plt.ylabel('y')

plt.grid(True)
plt.legend()

# نمایش نمودار
plt.show()
