class Poly:

    def __init__(self, capatity = 10):
        self.capatity = capatity
        self.degree = 0
        self.coef = [None] * capatity

    def readPoly(self):
        self.degree = int(input("다항식의 찰수를 입력: "))
        for i in range(self.degree, -1, -1):
            coef = int(input("%d차 항의 계수: " %i))
            self.coef[i] = coef

    def printPoly(self):
        for i in range(self.degree, 0, -1):
            print("%dx^%d + "% (self.coef[i], i), end=" ")
        print(self.coef[0])

    def addPoly(self, other):
        max_degree = max(self.degree, other.degree)
        result = Poly(capatity=max_degree + 1)
        result.degree = max_degree

        for i in range(max_degree + 1):
            a = self.coef[i] if i <= self.degree and self.coef[i] is not None else 0
            b = other.coef[i] if i <= other.degree and other.coef[i] is not None else 0
            result.coef[i] = a + b

        return result


    def evaluate(self, x):
        result = 0
        for i in range(self.degree + 1):
            if self.coef[i] is not None:
                result += self.coef[i] * (x ** i)
        return result
# test
p1 = Poly()
print("첫 번째 다항식을 입력하세요:")
p1.readPoly()

p2 = Poly()
print("두 번째 다항식을 입력하세요:")
p2.readPoly()

print("첫 번째 다항식:")
p1.printPoly()

print("두 번째 다항식:")
p2.printPoly()

sum_poly = p1.addPoly(p2)
print("두 다항식의 합:")
sum_poly.printPoly()

x_value = int(input("미지수 x의 값을 입력하세요: "))
print("1 다항식의 계산값:", p1.evaluate(x_value))
print("2 다항식의 계산값:", p2.evaluate(x_value))
print("합 다항식의 계산값:", sum_poly.evaluate(x_value))


