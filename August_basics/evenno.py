'''
numbers=[1,2,3,4,5,6,7,8]


sqno=map(lambda  x:x*2,numbers)
print(list(sqno))

even=filter(lambda x:x%2==0, numbers)
print(list(even))

# taking two inputs at a time
x, y = input("Enter two values: ").split()
print("Number of boys: ", x)
print("Number of girls: ", y)

# taking three inputs at a time
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)
'''
# Taking input as string
color = input("What color is rose?: ")
print(color)

n=input("how many roses?: ")
print(n)