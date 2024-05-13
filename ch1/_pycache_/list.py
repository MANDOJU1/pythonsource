# %%
# 숫자, 문자열

# 데이터 모임 표현 : list(== 자바의 ArrayList(배열)), dict(== 자바의 Map), set(== 자바의 HashSet)
# 동일한 타입만을 담지 않음

# %%
# 리스트 생성
list1 = []
list2 = [1, 2, 3, 4, 5, 6]
list3 = [1, "a", 3, "b", 5, 6]
list4 = [1, 2, 3, 4, 5.5, 6.5]
list5 = [1, 2, 3, 4, ["Life", "is", "short"]]
list6 = list([3, 4, 5])

# %%
# 출력
print(list2)  # [1, 2, 3, 4, 5, 6]

# %%
# 리스트 인덱싱 / 슬라이싱
print(list2[2])  # 3
print(list3[-2])  # 5
print(list4[-1])  # 6.5
print(list5[-1])  # ['Life', 'is', 'short']
print(list5[4])  # ['Life', 'is', 'short']
print(list5[4][0])  # Life
print(list5[4][2])  # short
print(list5[-1][-1])  # short

# %%
list7 = [1, 2, 3, 4, ["a", "b", ["Life", "is"]]]
# is 출력
print(list7[4][2][1])  # is
print(list7[-1][2][1])  # is
print(list7[-1][2][-1])  # is
print(list7[-1][-1][-1])  # is

# %%
print(list2)  # [1, 2, 3, 4, 5, 6]
print(list2[2:4])  # [3, 4]
print(list2[:4])  # [1, 2, 3, 4]
print(list2[:-1])  # [1, 2, 3, 4, 5]

# %%
print(list5)  # [1, 2, 3, 4, ['Life', 'is', 'short']]
print(list5[4:])  # [['Life', 'is', 'short']]
print(list5[4][:2])  # ['Life', 'is']

# %%
# 연산자
# + : 연결
print(list2 + list3)  # [1, 2, 3, 4, 5, 6, 1, 'a', 3, 'b', 5, 6]
print(list5 + list6)  # [1, 2, 3, 4, ['Life', 'is', 'short'], 3, 4, 5]

# 요소와 요소를 인덱싱 한 경우 산술 + 의 개념이 됨
print(list2[1] + list3[0])  # 3

# %%
# * : 반복
print(list2 * 2)  # [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]

# %%
# len() : 길이
len(list2)  # 6

# %%
# 리스트 수정 / 삭제
# 특정 요소 삭제
list2[0] = 7
print(list2)  # [7, 2, 3, 4, 5, 6]

list2[1] = [10, 11, 12]
print(list2)  # [7, [10, 11, 12]]

# 리스트 삭제
del list2[1]
print(list2)  # [7, 3, 4, 5, 6]

del list2[2:]
print(list2)  # [7, 4]

# %%

for i in list3:
    print(i, end="\t")


# %%
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]
# 100 이상의 요소만 출력
for i in numbers:
    if i >= 100:
        print(i, end=" ")

# %%
# 홀수, 짝수 구분하여 출력
for i in numbers:
    if i % 2 == 0:
        print("짝수", i)
    else:
        print("홀수", i)

# %%
# 숫자의 자릿수 출력
for i in numbers:
    # print(len(str(i)))
    print("{} : {}".format(i, len(str(i))))

# %%
# 함수
# 1) append() : 리스트에 요소 추가
list3.append(["c", "d", "e"])
print(list3)  # [1, 'a', 3, 'b', 5, 6, ['c', 'd', 'e']]
list3.append(5)
print(list3)  # [1, 'a', 3, 'b', 5, 6, ['c', 'd', 'e'], ['c', 'd', 'e'], 5]

# %%
# 1 ~ 100 까지 숫자 중에서 짝수만 리스트로 생성
even = []

for i in range(2, 101, 2):
    even.append(i)
print(even)

# %%
# 2) sort() : 오름차순 정렬
a = [1, 4, 3, 2]
a.sort()
print(a)  # [1, 2, 3, 4]

a = ["a", "e", "g", "b", "c"]
a.sort()
print(a)  # ['a', 'b', 'c', 'e', 'g']

a = ["ㅎ", "ㄱ", "ㅈ", "ㅁ", "ㅋ"]
a.sort()
print(a)  # ['ㄱ', 'ㅁ', 'ㅈ', 'ㅋ', 'ㅎ']

# %%
# 3) reverse() : 리스트 뒤집기
print(list4)  # [1, 2, 3, 4, 5.5, 6.5]
list4.reverse()
print(list4)  # [6.5, 5.5, 4, 3, 2, 1]

# %%
# 4) index() : 인덱스 값 리턴 (위치)

list4.index(3)  # 3
list4.index(6)  # ValueError : 6 is not in list

# %%
# 5) remove() == del 요소지정
# 처음 만나는 요소 제거

# list4  # [6.5, 5.5, 4, 3, 2, 1]
# list4.remove(4)
print(list4)  # [6.5, 5.5, 3, 2, 1]
list4.append(5.5)
print(list4)  # [6.5, 5.5, 3, 2, 1, 5.5, 5.5]

list4.remove(5.5)
# 처음 만나는 요소 제거
print(list4)  # [6.5, 3, 2, 1, 5.5, 5.5]

# %%
# 6) pop() : 맨 마지막 리스트 요소 꺼내기
list4.pop()
list4  # [6.5, 3, 2, 1, 5.5]

# %%
# pop(인덱스) : 인덱스 요소 꺼내기 (==제거)
list4.pop(1)
list4  # [6.5, 2, 1, 5.5]

# %%
# 7) count(찾을 요소) : 찾을 요소 개수 리턴
list4 = [12, 13, 14, 15, 14]
list4.count(14)  # 2

# %%
# 8) extend() : + 같은 역할
list4.extend([16, 17, 18])
list4  # [12, 13, 14, 15, 14, 16, 17, 18]

# %%
# 9) clear() : 리스트 요소 모두 삭제
list4.clear()
list4

# %%
numbers  # [273, 103, 5, 32, 65, 9, 72, 800, 99]

# %%
numbers.sort(reverse=True)
print(numbers)  # [800, 273, 103, 99, 72, 65, 32, 9, 5]

# %%
# 거짓에 해당 : "", [], (), {}, 0

city = ""
list8 = []

if city:
    print("비어 있지 않음")
else:
    print("비어 있음")


if list8:
    print("비어 있지 않음")
else:
    print("비어 있음")

# %%
fruits = ["딸기", "바나나", "사과", "배"]

# in == SQL in 연산자와 동일 개념
if "딸기" in fruits:
    print("딸기 요소가 포함됨")

print("메론" not in fruits)  # True

# %%
a_class = [70, 60, 55, 75, 92, 80, 85, 100, 87, 65]

# a_class 평균과 총합을 구하시오
total = 0
for num in a_class:
    total += num

print(f"총합 : {total}, 평균 : {total/len(a_class)}")

# %%
# sum
print(f"총합 : {sum(a_class)}, 평균 : {sum(a_class)/len(a_class)}")
