import calc_bmi

print("bmiの計算")
w = int(input("体重: "))
h = int(input("身長: "))
bmi = calc_bmi.bmi_cal(h, w)
print(f"あなたのbmiは{bmi * 10000}です")
