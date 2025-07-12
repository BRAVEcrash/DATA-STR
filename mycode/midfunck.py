def divide(a, b):
    # 나눌 수가 0이면 오류
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")

    # 종료 조건: a가 b보다 작으면 몫은 0, 나머지는 a
    if a < b:
        return (0, a)

    # 재귀적으로 b를 계속 빼며 몫을 1씩 누적
    quotient, remainder = divide(a - b, b)
    return (quotient + 1, remainder)

print(divide(17, 0))  # 결과: (3, 2)
print(divide(20, 4))  # 결과: (5, 0)

# 덧셈(+)이나 뺄셈(-) 연산자와 재귀 함수만을 사용해서,
# 나눗셈의 몫과 나머지를 구하는 파이썬 함수 예제를 아래에 작성해봤어.
# 이 함수는 divmod(a, b)처럼 (몫, 나머지)를 반환해.
#
# 🧮 함수 설명
# a는 나눠지는 수 (피제수)
# b는 나누는 수 (제수)
# 덧셈/뺄셈만 사용
# 음수는 처리하지 않고, 양의 정수만 처리하는 기본 버전 (확장 가능)

# (필기) 나눗셈의 몫과 나머지를 구하는 함수를 나눗셈과 나머지
# 연산자가 아닌 덧셈이나 뺄셈 연산자, 재귀 함수 기법을 사 용하여
# 구현하시오.

def divide(a,b):
  if b == 0:
    raise ValueError("cant divide to 0")
  q = 0
  r = a
  while r >= b:
    r -= b
    q += 1
  return (q,r)
print(divide(17,5))

#묷과 나머지지
def divide(a, b):
    if b == 0:
        raise ValueError("cant divide to 0")
    q = 0
    r = a
    while r >= b:
        r -= b
        q += 1
    return (q, r)


print(divide(17, 5))


# 묷과 나머지지

def div_rec(a, b):
    if b == 0:
        raise ValueError("Cannot divide by 0")
    if a < b:
        return (0, a)
    q, r = div_rec(a - b, b)
    return (q + 1, r)


print(div_rec(17, 5))