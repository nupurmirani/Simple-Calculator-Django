from django.shortcuts import render

def calculator(request):
    result = None
    
    if request.method == 'POST':
        try:
            num1 = request.POST.get('num1')
            num2 = request.POST.get('num2')
            operation = request.POST.get('opr')
            
            if num1 is not None and num2 is not None and operation is not None:
                num1 = float(num1)
                num2 = float(num2)
                
                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        result = "Division by zero is not allowed."
                    else:
                        result = num1 / num2
                else:
                    result = "Invalid operator."
            else:
                result = "Missing input data."
        
        except ValueError:
            result = "Invalid numeric input."
    print(result)
    context = {'result': result}
    return render(request, "calc.html", context)
