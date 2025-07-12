# def EvalPostfix(expr):
#     S = ArrayStack()
#
#     for term in expr:
#         if term in '+-*/':
#             val2 = S.pop()
#             val1 = S.pop()
#
#             if term == '+':
#                 S.push(val1 + val2)
#             elif term == '-':
#                 S.push(val1 - val2)
#             elif term == '*':
#                 S.push(val1 * val2)
#             elif term == '/':
#                 S.push(val1 / val2)
#         else:
#             S.push(float(term))
#
#     return S.pop()
# if __name__ == '__main__':
#     expr = ['2', '3', '+', '4', '*']  # (2 + 3) * 4 = 20
#     result = EvalPostfix(expr)
#     print(result)  # Output: 20.0


from Tuesday02.ArrayStack import ArrayStack

def evalPostfix(expr):
    s = ArrayStack(100)

    for token in expr:
        if token in "+-*/":
            val2 = s.pop()  # 피연산자2 (Second operand)
            val1 = s.pop()  # 피연산자1 (First operand)

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
    expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
    expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']

    print(expr1, '-->', evalPostfix(expr1))
    print(expr2, '-->', evalPostfix(expr2))
# ['8', '2', '/', '3', '-', '3', '2', '*', '+'] --> 7.0
# ['1', '2', '/', '4', '*', '1', '4', '/', '*'] --> 0.5
