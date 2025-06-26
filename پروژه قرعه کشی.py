# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 13:16:26 2025

@author: AsusAliR
"""
import random

# نمایش پیام خوشامدگویی
print("\n🎉 خوش آمدید به سیستم قرعه‌کشی هوشمند! 🎉")
print("--------------------------------------------------")

# دریافت تعداد شرکت‌کنندگان
num_participants = int(input("🔹 تعداد شرکت‌کنندگان را وارد کنید: "))
num_winners = int(input("🔹 تعداد برندگان را وارد کنید: "))

# بررسی تعداد برندگان نباید بیشتر از شرکت‌کنندگان باشد
if num_winners > num_participants:
    print("❌ تعداد برندگان نمی‌تواند بیشتر از شرکت‌کنندگان باشد!")
else:
    # ایجاد لیست شرکت‌کنندگان با شماره ویژه
    participants = {}

    print("\n✅ لطفاً نام شرکت‌کنندگان را وارد کنید:")
    for i in range(1, num_participants + 1):
        name = input(f"🔹 نام شرکت‌کننده {i}: ")
        unique_number = random.randint(0, 9999)  # شماره ویژه تصادفی
        participants[name] = unique_number

    # تبدیل دیکشنری به لیست برای قرعه‌کشی
    participants_list = list(participants.keys())

    # انتخاب تصادفی برندگان
    winners = random.sample(participants_list, num_winners)

    # نمایش اطلاعات برندگان
    print("\n🏆 **نتیجه قرعه‌کشی:**")
    print("--------------------------------------------------")
    for winner in winners:
        print(f"🎉 {winner} (شماره ویژه: {participants[winner]})")

    print("\n✨ تبریک به برندگان! امیدواریم که خوش‌شانس باشید! ✨")
