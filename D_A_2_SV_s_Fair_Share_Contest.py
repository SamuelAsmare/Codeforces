n , ans = int (input()) , 0
students = list(map(int, input().split()))
largest= max(students)
for i in students:
    ans += (largest - i)
print(ans)