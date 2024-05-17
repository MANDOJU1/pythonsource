# 변수
# 변수 : 타입 없음(값을 담고 난 다음에 결정) / 키워드 없음(let, const X)

num = 1
num = "10"
print(num) # 10

a = b = 3
print(a, b) # 3 3

a, b = 10, 15
print(a, b) # 10 15

# 두 개의 변수에 있는 값 서로 변경
a, b = b, a
print("a = %d, b = %d" % (a, b)) # a = 15, b = 10

str1 = "500"
# 파이썬 : int값과 str 값을 연결해주지 않음 (타입을 변경해야 함) JAVA : + 는 연결의 의미
# num1 = str1 + 500 # TypeError: can only concatenate str (not "int") to str
# print(str1 + 500)

# 타입변환 : str(), int(), float(), bool()
# type() : 타입확인
print(type(str1))
print(type(10))
print(type(10.5))
print(type(False))

print(int(str1))
print(type(int(str1))) # <class 'int'>

print(int(str1) + 500) # 1000

f = 3.5
print(type(f))
print(type(str(f)))

print(int(True)) # 1
print(int(False)) # 0
print(int(3.6)) # 3
print(int("3")) # 3
# 소수점 혹은 지수를 포함하는 문자열은 int로 변경 못함
# print(int("3.6")) # ValueError: invalid literal for int() with base 10: '3.6'

print(float(True)) # 1.0
print(float(False)) # 0.0
print(float(3.6)) # 3.6
print(float("3")) # 3.0
print(float("3.6")) # 3.6
print(float("3.06e4")) # 30600.0

print()
# 0이 아닌 숫자는 모두 True임
print(bool(1)) # True
print(bool(0)) # False
print(bool(99)) # True
print(bool("99")) # True