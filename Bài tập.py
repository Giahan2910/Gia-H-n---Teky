a = float(input("Nhập cân nặng(Kg): "))
b = float(input("Nhập chiều cao(m): "))
pt = input("Tính chỉ số BMI:")
BMI = a/(b*b)
if BMI < 0:
    print("Gầy cấp độ III")
if 16 <= BMI < 17:
    print("Gày cấp độ II")
if 17 <= BMI < 18.5:
     print("Gày cấp độ I")
if 18.5 <= BMI < 25:
    print("Bình thường")
if 25 <= BMI < 30:
    print("Béo phì cấp độ I")
if 35 <= BMI < 40:
    print("Béo phì cấp độ II")
else:
    print("Béo phì cấp độ III")
