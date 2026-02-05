num1 =int(input("numero 1:"))
num2 =int(input("numero 2:"))
operacion = input("ingrese la operacion (+, -, *, /): ")

match operacion:
    case "+":
        res = num1+num2
    case "-":
        res = num1-num2
    case "*":
        res = num1*num2
    case "/":
        res = num1/num2
   
print("el resultado es:", res)
