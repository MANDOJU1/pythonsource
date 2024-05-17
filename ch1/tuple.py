# 튜플 : ()
# 튜플은 요소값을 바꿀 수 없다(sort, remvoe, insert, pop 같은 함수 없음)
# 리스트와 유사

# %%
# 생성
t1 = ()
t2 = (1,)  # 1개의 요소만을 가질 때 요소 뒤에 쉼표 반드시 필요함
t3 = (1, 2, 3)
t4 = 1, 2, 3  # 소괄호 생략 가능 (보통 사용함)
t5 = ("a", "b", ("ab", "cd"))

# %%
print(t2)  # (1,)
print(t3)  # (1, 2, 3)
print(t4)  # (1, 2, 3)
print(t5)  # ('a', 'b', ('ab', 'cd'))

# %%
del t3[0]  # TypeError : 'tuple' object doesn't support item deletion

# %%
t3[0] = 6  # TypeError: 'tuple' object does not support item assignment

# %%
t3[1:]  # (2, 3)

# %%
t6 = t1 + t2
t6  # (1,)

# %%
t6 = t3 * 3
t6  # (1, 2, 3, 1, 2, 3, 1, 2, 3)

# %%
len(t6)  # 9
