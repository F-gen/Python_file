# BIM=weight(kg)/ height**
weight = float(input("input you weight (kg)"))
height = float(input("input you height (m) "))
bim = round(weight / height ** 2)
if bim < 18.5:
    print(f"you bim is {bim},you are underweight")
elif bim < 25:
    print(f"you bim is {bim},you are normal weight")
elif bim < 30:
    print(f"you bim is {bim},you are overweight")
elif bim < 35: 
    print(f"you bim is {bim},you are obese")

else:
    print(f"you bim is {bim},you are clinically obese")
