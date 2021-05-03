#Write a program that asks the user how many Fibonacci numbers to generate and 
#then generates them. Take this opportunity to think about how you can use 
#functions. Make sure to ask the user to enter the number of numbers in the 
#sequence to generate.(Hint: The Fibonacci seqence is a sequence of numbers
#where the next number in the sequence is the sum of the previous two numbers in
#the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …) 

def fibo_generator(num):
  res = [1]
  j=1
  for i in range(1,num):
    res.append(j)
    j += res[i-1]
  return res

x = int(input("Enter no of terms to generate: "))
print(fibo_generator(x))