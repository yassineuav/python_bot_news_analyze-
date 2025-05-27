#logical operators: and, or, not

hight_income = True
good_credit = True
student = False

print(f"Hight income: {"yes" if hight_income else "no"}")
print(f"Good credit: {"yes" if good_credit else "no"}")
print(f"Student: {"yes" if student else "no"}")


message = "Not Eligible"
if hight_income and good_credit and not student:
    message = "Eligible"

print(f"Aprove for loan: {message}")