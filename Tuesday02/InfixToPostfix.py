from Tuesday02.ArrayStack import ArrayStack

def precedence(op):
    if op == '(' or op == ')': return 0
    elif op == '+'or op == '-': return 1
    elif op == '*' or op == '/': return 2
    else: return -1
def infixToPostfix( expr ):
    S = ArrayStack(100)
    output = []

    for term in expr:
        if term == '(':
            S.push('(')
        elif term in ')':
            while not S.isEmpty():
                op = S.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif term in "+-*/":
            while not S.isEmpty():
                op = S.peek()
                if ( precedence(term) <= precedence(op)):
                    output.append(op)
                    S.pop()
                else: break
            S.push(term)
        else:
            output.append(term)

    while not S.isEmpty():
        output.append(S.pop())

    return output

if __name__ == '__main__':
    infix = input("Enter a expression: ")
    expr = infix.split()
    postfix = infixToPostfix(expr)

    print(postfix)

# Enter a expression: ( 8 / 2 ) - ( 3 - 3 * 2 )
# ['8', '2', '/', '3', '3', '2', '*', '-', '-']

    