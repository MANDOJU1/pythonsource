# 딕셔너리 == Map
# list 와 같이 많이 쓰이는 자료형
# key, value
# {}

# %%
# 생성
dict = {}
dict1 = {"": "addr"}
dict2 = {"name": "Song", "age": 12}
dict3 = {0: "Hello Python", 1: "Hello Coding"}
dict4 = {"arr": [1, 2, 3, 4, 5]}

# %%
print(dict2)  # {'name': 'Song', 'age': 12}
print(dict3)  # {0: 'Hello Python', 1: 'Hello Coding'}
print(dict4)  # {'arr': [1, 2, 3, 4, 5]}

# %%
# 특정 키의 요소 출력
print(dict2["name"])  # Song
print(dict3[0])  # Hello Python
print(dict4["arr"])  # [1, 2, 3, 4, 5]

# %%
dict1["addr"]  # KeyError: 'addr'

# %%
dict1.get("addr")

# %%
