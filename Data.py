#Basic Float Example
# x = 3
# y = float(3)
# print(x,y)
#what this code does is assign a value to "x" and "y"
# when you put float in front of a number in parenthesis it makes it a decimal
#then it prints x and prints y.

# the output would be: 3 3.0
#_______________________

#lists
# values = [1,2.23,5,7,2,30,15]
# print(values)
# for i in values:
#     print(i)

# print(values[0])
# print(values[6])

# print(values[7]) -This wouldnt work since there is no value "7" 
#python starts counting at 0 

# "test"
# ["t","e","s","t"]

# x = "this is a thing"
# y = x.split()
# z = y[0]
# print(y)
# print(z)

#_____________________
#Challenge


# # creates an input called sentance
# sentance = input("write any sentance")
# # now creates words which is sentanc split
# words = sentance.split()
# # prints the length of words
# print(len(words))



# day_of_week = input("what day is it?")
# if day_of_week == "Friday":
#     print("Yay it's Friday!")
# else:
#     print("Aw man")


#F strings

# x = "test"
# print(f"hello {x}")



# temp = 75
# if temp > 68:
#     print('warm')
# elif temp == 68:
#     print('perfect')

# else:
#     print('cold')


#______________________________________
#challenge

# n = int(input('please input a number')) 
# x = n 
# if x % 2 ==0:
#     print('even')
# else:
#     print('odd')

#_____________________________________
#challenge

food_cost = int(input('How much did your foood cost?'))
service = input("How was the service? bad, okay, good or great?")
x = food_cost

if service == 'bad':
    print(food_cost * 0)
elif service == 'okay':
    print(food_cost * 0.15)
elif service == 'good': 
    print(food_cost * 0.20)
elif service == 'great':
    print(food_cost * 0.25)