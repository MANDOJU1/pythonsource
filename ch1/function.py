# 함수
# def 함수명(매개변수):
#     수행할 문장1
#     수행할 문장2


# %%
# 매개변수 X
def hello():
    print("Hello!!")


hello()


# %%
# 매개변수 O
def add(a, b):
    return a + b


add(5, 3)
# add(5) : TypeError


# %%
# 기본값 부여 : 값이 안넘어오는 경우 사용
def sub(a, b=3):
    return a - b


print(sub(9, 5))  # 4
print(sub(9))  # 6


# %%
# 가변 : 입력값이 몇 개가 될지 모르는 경우 사용
#        입력값을 모아서 튜플로 만들어 줌
def add_many(*args):
    print(args)
    # (1, 2, 3)
    # (1, 2, 3, 4, 5, 6, 7)
    # ('35', '24', '65', '98')
    # ({'dessert': 'macaroon', 'wine': 'marlot'},)


add_many(1, 2, 3)
add_many(1, 2, 3, 4, 5, 6, 7)
add_many("35", "24", "65", "98")
add_many({"dessert": "macaroon", "wine": "marlot"})


# %%
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result


print(add_many(1, 2, 3))  # 6
print(add_many(1, 2, 3, 4, 5, 6, 7))  # 28


# %%
# 순서
# 가변파라메터와 일반 파라메터가 섞일 때 가변파라메터를 맨 뒤에 선언
def add_many(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result


print(add_many("add", 1, 2, 3))  # 6
print(add_many("mul", 1, 2, 3, 4, 5, 6, 7))  # 5040


# %%
# 키워드 파라메터 : kwargs
# 입력값을 모아서 dict(딕셔너리)로 만들어줌
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(name="foo", age=3)  # {'name': 'foo', 'age': 3}
print_kwargs(
    name="foo", age=3, addr="seoul"
)  # {'name': 'foo', 'age': 3, 'addr': 'seoul'}


# %%
# 일반, 가변, 키워드, 파라메터 섞이는 경우
def print_kwargs(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, *args, **kwargs)


print_kwargs(10, 20)
print_kwargs(10, 20, "park", "kim")
print_kwargs(10, 20, "park", "kim", age=25, name="choi")


# %%
# 리턴값에 여러 개를 작성할 수 있는데 내부적으로는 튜플 하나로 리턴이 되는 것
def add_and_mul(a, b):
    return a + b, a * b


hap, mul = add_and_mul(5, 6)
print(hap, mul)  # 11 30
print(add_and_mul(3, 4))  # (7, 12)


# %%
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    # 튜플로 리턴(기본)
    return y1, y2, y3


print(func_mul(100))  # (10000, 20000, 30000)


def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    # 리스트로 리턴 받고 싶을 때
    return [y1, y2, y3]


print(func_mul(100))  # [10000, 20000, 30000]


# %%
def say_nick(nick):
    if nick == "바보":
        return
    print(f"나의 별명은 {nick} 입니다")


say_nick("바보")
say_nick("야호")

# %%
# 두 개의 숫자와 연산자를 입력받아 사칙연산 함수 작성


def four_rules(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2


num1 = int(input("Input Num1 : "))
num2 = int(input("Input Num1 : "))
op = input("(+,-,*,/) 중 하나를 입력하세요")

print(f"{num1} {op} {num2} = {four_rules(num1,num2,op)}")

# %%
# 1번 방법
a = 1


def vartest(a):
    a = a + 1
    return a


a = vartest(a)
print(a)  # 2

# %%
# 2번 방법 (추천 X)
a = 1


def vartest():
    global a
    a = a + 1
    return a


vartest()
print(a)  # 2

# %%
# 1 ~ 100 숫자 중에서 소수에 해당하는 숫자를 찾아서 리스트에 담기
# 소수 : 1과 자기 자신으로 나누어 떨어지는 숫자
#        2, 3, 5, 7, ... 97

primes = []


def isPrime(x):
    # x 가 소수이면 primes 에 추가
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    if cnt == 2:
        primes.append(x)


for j in range(1, 101):
    # isPrime() 호출
    isPrime(j)

print(primes)  # [2,3,5, ..., 97]
