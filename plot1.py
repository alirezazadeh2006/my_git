# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 16:13:32 2025

@author: AsusAliR
"""

import numpy as np
import matplotlib.pyplot as plt

# ایجاد بردار x با ۵۰۰ نقطه در بازه [-5, 5]
x = np.linspace(-5, 5, 500)

# توابع مورد نظر
y3 = x ** 3
y2 = x ** 2

# ترسیم نمودار
plt.plot(x, y3, 'g--', label='y = x^3')   # خط چین سبز
plt.plot(x, y2, 'r', label='y = x^2')     # خط معمولی قرمز

# تنظیمات نمودار
plt.title('Plot of x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()

# ذخیره نمودار به صورت تصویر
plt.savefig('chart_output.png')

# نمایش نمودار
plt.show()

# اجرای تابع
#plot_custom_chart()