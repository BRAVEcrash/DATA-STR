from Tuesday02.ArrayStack import ArrayStack

def precedence(op):
    if op == '(' or op == ')':
        return 0
    elif op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    else:
        return -1

def Infix2Postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term == '(':
            s.push('(')

        elif term == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)

        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(s.pop())
                else:
                    break
            s.push(term)

        else:
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output

def evalPostfix(expr):
    s = ArrayStack(100)

    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if token == '+':
                s.push(val1 + val2)
            elif token == '-':
                s.push(val1 - val2)
            elif token == '*':
                s.push(val1 * val2)
            elif token == '/':
                s.push(val1 / val2)
        else:
            s.push(float(token))

    return s.pop()

if __name__ == "__main__":
    infix1 = ['8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
    infix2 = ['1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']

    postfix1 = Infix2Postfix(infix1)
    postfix2 = Infix2Postfix(infix2)

    result1 = evalPostfix(postfix1)
    result2 = evalPostfix(postfix2)

    print('중위표기: ', infix1)
    print('후위표기: ', postfix1)
    print('계산결과: ', result1, end='\n\n')

    print('중위표기: ', infix2)
    print('후위표기: ', postfix2)
    print('계산결과: ', result2)
