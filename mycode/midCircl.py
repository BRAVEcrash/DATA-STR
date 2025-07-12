# (실기) 원형 큐를 이용하여
# 피보나치 수열 출력하는 프로그램을 작성하시오.
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [0] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, data):
        if self.count == self.size:
            # 원형 큐이므로 앞에서 제거하고 넣기
            self.dequeue()
        self.queue[self.rear] = data
        self.rear = (self.rear + 1) % self.size
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError("큐가 비어 있습니다.")
        data = self.queue[self.front]
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return data

    def get_items(self):
        items = []
        idx = self.front
        for _ in range(self.count):
            items.append(self.queue[idx])
            idx = (idx + 1) % self.size
        return items

# 피보나치 수열 출력
def fibonacci_with_circular_queue(n):
    if n <= 0:
        return []

    cq = CircularQueue(2)  # 피보나치는 바로 전 두 수만 기억하면 됨
    result = []

    # 초기값
    cq.enqueue(0)
    result.append(0)

    if n == 1:
        return result

    cq.enqueue(1)
    result.append(1)

    for _ in range(n - 2):
        items = cq.get_items()
        next_fib = sum(items)
        result.append(next_fib)
        cq.enqueue(next_fib)

    return result

print(fibonacci_with_circular_queue(10))
# 출력: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# ✏️ 핵심 설명
# 원형 큐는 고정된 크기로 순환하면서 데이터를 저장
# 피보나치는 직전 두 항의 합으로 이루어져 있으므로, 큐 크기를 2로 설정
# 새 값을 넣기 전, 큐가 꽉 찼다면 앞의 값을 dequeue해서 제거
# 이 구조는 메모리 효율적으로 오직 필요한 두 항만 유지