def calculation(a,b,c):
    a=float(a)
    b=float(b)
    if c=='+':
        return a+b 
    elif c=='-':
        return a-b 
    elif c=='*':
        return a*b
    elif c=='/':
        return a/b
    
def bodmas(equation):
    equation = equation.split()
    # print(equation)
    if len(equation)<3:
        return equation[0]
    priority = {'+':1,'-':1,'*':2 , '/':2}
    ans = 0;
    stack = []
    operator = []
    q = 0
    stack.append(equation[0])
    operator.append(equation[1])
    stack.append(equation[2])
    i=3
    while(i<len(equation) and len(operator)>0  ):
        # print(equation[i],stack,operator)
        if equation[i] in priority and priority[operator[-1]]>=priority[equation[i]]:
            # print(stack,operator)
            oper =operator.pop()
            b = stack.pop()
            a = stack.pop()
            c = calculation(a,b,oper)
            stack.append(c)
            operator.append(equation[i])
            i+=1
            # print(stack,operator)
            # print()
        elif equation[i] in priority : 
            operator.append(equation[i])
            i+=1
        else :
            stack.append(equation[i])
            i+=1
     
    while(len(operator)>0):
        oper = operator.pop()
        b = stack.pop()
        a = stack.pop()
        c= calculation(a,b,oper)
        stack.append(c)
    return stack[-1]
    
    

operator_sym = ['+','-','*','/','=']
operator_words = ['plus','substract','multiple','division','equals']

numbers_sym  =['1','2','3','4','5','6','7','8','9','0']
numbers_words = ['one','two','three','four','five','six','seven','eight','nine','zero']

file = open('input.txt')
# t = int(input())
t = int(file.readline())
while(t>0):
    t-=1

    # equation = list(map(str, input("elements of array:-").strip().split()))
    # equation=" ".join(equation)
    equation = file.readline()
    # print(equation)
    for i in range(len(operator_words)):
        equation = equation.replace(operator_words[i],operator_sym[i])
        
    for i in range(len(numbers_sym)):
        equation = equation.replace(numbers_words[i],numbers_sym[i])
        
    final = equation.split('=')
    lhs = final[0]
    rhs = final[1]
    lhs = bodmas(lhs)
    # print(lhs,rhs)
    with open('output.txt','a') as f:
        if float(lhs) == float(rhs):
            f.write(f'true\n')
            # f.write(f'true {float(lhs)},{float(rhs)}\n')
        else:
            f.write(f'false\n') 
            # f.write(f'false {float(lhs)},{float(rhs)}\n') 


