import sum1

print(sum1.sum1(50, 60))  # 110
# print(sum1.sum1(50, "60")) # TypeError
print(sum1.safe_sum(50, "60"))  # 더할 수 없습니다. (에러는 나지 않음)
