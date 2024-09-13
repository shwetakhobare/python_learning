#The numbers divisible by another number

my_list = [22,24,13,65,78,95,100,241,888]

result = list(filter(lambda x : (x%13 == 0),my_list))
print("Numbers divisible by 13 are",result)