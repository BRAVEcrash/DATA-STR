# 순환문을 이용해 나눗셈의 몫과 나머지를
# 구하는 알고리즘을 손코딩하기
def divide(a, b):
    if b == 0:
        raise ValueError("0으로 나눌 수 없습니다.")

    quotient = 0  # 몫 초기화
    remainder = a  # 나머지는 처음엔 a로 시작

    # b를 계속 빼면서 몫을 증가
    while remainder >= b:
        remainder = remainder - b
        quotient = quotient + 1

    return (quotient, remainder)
print(divide(17, 5))  # 결과: (3, 2)
print(divide(10, 3))  # 결과: (3, 1)
print(divide(20, 4))  # 결과: (5, 0)
# ✏️ 손코딩 포인트 요약
# while문을 사용해서 remainder가 b보다 작아질 때까지 반복
# 한 번 반복할 때마다 b만큼 빼고 quotient 1 증가
# 반복이 끝나면 quotient는 몫, remainder는 나머지