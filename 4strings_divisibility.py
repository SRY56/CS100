# Shailesh Yannam
# cs 100 2023S section 012
# HW 04, march 09, 2023

#Excercise 1a and 1b
def hasFinalletter(strList, letters):
    result = []
    for l in strList:
        if l[-1] in letters:
            result.append(l)
    return result
list1 = ["Soccer", "Football", "Taekwondo", "Basketball", "Tennis", "Sumo", "Kabaddi"]
list2 = ["john", "Ben", "kenny", "Jamie", "Benjamin"]
list3 = ["Crazy", "Happy", "relived", "sad"]
l1 = hasFinalletter(list1, "aeiou")
l2 = hasFinalletter(list2, "aeiou")
l3 = hasFinalletter(list3, "aeiou")
print("Result 1: ", l1)
print("Result 2: ", l2)
print("result 3: ", l3)

print()

#Excercise 2a and 2b
def isDivisible(maxInt, twoInts):
    result = []
    for m in range(1, maxInt):
        if m % twoInts[0] == 0 and m % twoInts[1] == 0:
            result.append(m)
    return result

twoInt1 = (2,5)
maxInt1 = 60
print(isDivisible(maxInt1, twoInt1))

twoInt2 = (12, 30)
maxInt2 = 0
print(isDivisible(maxInt2, twoInt2))

twoInt3 = (9,3)
maxInt3 = 100
print(isDivisible(maxInt3, twoInt3))