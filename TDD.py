# name: neoray hagag id:208090738,name:tal sinay id: 316261353
def testdigit(weight,height):
    if str(weight).replace('.',"").isdigit()and str(height).replace('.',"").isdigit():
        return True
    return False


def wahtIstheBMI():
    while True:
        weight, height = input("Enter weight:\n"), input("Enter height:\n")
        if testdigit(weight,height):
            BMI = float(weight)/float(height)**2
            if 18<=BMI<=25:
                return "normal"
            elif BMI>25:
                return"Overweight"
            return "Underweight"
        print("Enter only real numbers\n")




print("The results are:"+wahtIstheBMI())