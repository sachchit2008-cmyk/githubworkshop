# find the smallest of 3 time instants, T1, T2, T3,
# where each is a floating point number

T1=float(input("time 1? "))
T2=float(input("time 2? "))
T3=float(input("time 3? "))
minT = T1
if(minT > T2):
    minT = T2
if(minT >T3):
    minT = T3
print('T1 =', T1, 'T2 =', T2, 'T3 =', T3, 'minimum T =' , minT)