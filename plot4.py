# -*- coding: utf-8 -*-
"""
Created on Thu Jun 26 15:14:43 2025

@author: AsusAliR
"""

import numpy as np
import matplotlib.pyplot as plt

def pilot_normal_dist(n, mean=0, std=1):
    # ایجاد داده تصادفی با توزیع نرمال
    data = np.random.normal(loc=mean, scale=std, size=n)

    # رسم هیستوگرام با 100 بین
    plt.hist(data, bins=100, color='skyblue', edgecolor='black')

    # تنظیمات نمودار
    plt.title(f'Normal Distribution (n={n}, mean={mean}, std={std})')
    plt.xlabel('')
    plt.ylabel('')

    # محدودیت y به شکل دینامیک بر اساس n
    plt.ylim(0, 3500 if n > 1000 else None)

    # نمایش
    plt.grid(True)
    plt.show()
pilot_normal_dist(10)
pilot_normal_dist(1000)
pilot_normal_dist(100000)
