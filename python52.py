<<<<<<< HEAD
#factorial of a number

num = int(input("Enter the number :"))

factorial =1

if(num <= 0):
    print("The factorial does not exits a negative number")
elif(num ==0):
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
       factorial=factorial*i
    print("The factorial number is",factorial)
=======
# Program to count the number of each vowels

# string of vowels
vowels = 'aeiou'

ip_str = 'Hello, have you tried our tutorial section yet?'

# make it suitable for caseless comparisions
ip_str = ip_str.casefold()

# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)

# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1

print(count)
>>>>>>> edef2af1860f35ac4ef4ba7f2ef4813a2f92c420
