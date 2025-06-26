# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 13:37:53 2025

@author: AsusAliR
"""

import numpy as np
import matplotlib.pyplot as plt

# بردار x با ۵۰۰ نقطه در بازه [-5, 5]
x = np.linspace(-5, 5, 500)

# توابع ریاضی
y_cos = np.cos(1.2 * x)
y_exp = np.exp(-x ** 2)

# ترسیم نمودار
plt.plot(x, y_cos, 'g--', label='cos(1.2x)')       # خط‌چین سبز
plt.plot(x, y_exp, 'r', label='exp(-x^2)')         # خط قرمز

# عنوان و برچسب‌ها
plt.title('Plot of Mathematical Functions')
plt.xlabel('x')
plt.ylabel('y')

# و نمایش
plt.grid(True)
plt.legend()
plt.show()
