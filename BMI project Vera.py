#BMI Calculator
#Metric = weight/height**2
#imperial = weight/height**2*703
#w = weight
#h = height

unit = int(input("choose your preferred unit: \n1. metric(kilogram,meers) \n2. Imperial(pound,inches) \n"))

if(unit==1):
    met_w = int(input("input your weight (kg) "))
    met_h = float(input("input your height (m2) "))
    BMI = met_w/met_h**2
    print("your BMI is:" ,round(BMI,1 ))
             
elif(unit==2):
    imp_w = int(input("input your weight (lbs) "))
    imp_h = int(input("input your height (inches) "))
    BMI = (imp_weight*703)/imp_height**2
    print("your BMI is:" ,round(BMI,1 ))



if(BMI<18.5):
    print("you are underweight")

elif(BMI>=18.5 and BMI<25):
    print("you are perfectly in good shape")

elif(BMI>=25 and BMI<=29.9):
    print("you are overweight")

elif(BMI>30):
    print("you are obese please see a doctor")

