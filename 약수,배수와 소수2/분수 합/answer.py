# 분수 클래스 정의
class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
 
    # 기약분수 형태로 출력
    def __str__(self):
        gcd = self.get_gcd(self.numerator, self.denominator)
        return str(self.numerator // gcd) + '/' + str(self.denominator // gcd)
 
    # 분자와 분모의 최대공약수 계산
    def get_gcd(self, a, b):
        if b == 0:
            return a
        return self.get_gcd(b, a % b)
 
# 분수 덧셈 함수 정의
def add_fraction(f1, f2):
    numerator = f1.numerator * f2.denominator + f2.numerator * f1.denominator
    denominator = f1.denominator * f2.denominator
    return Fraction(numerator, denominator)
 
# 두 분수 입력받기
a, b = map(int, input().split())
c, d = map(int, input().split())
 
# 분수 객체 생성
f1 = Fraction(a, b)
f2 = Fraction(c, d)
 
# 두 분수 더한 결과 출력
result = add_fraction(f1, f2)
print(result)
