import math as m

t=int(input())
for _ in range(t):
    contains_ml, contains_mg, required_ml, required_mg= map(int, input().split())
    coconut_ml=m.ceil(required_ml/contains_ml)
    coconut_mg=m.ceil(required_mg/contains_mg)
    print(coconut_mg+coconut_ml)