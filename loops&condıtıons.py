###########
# KOŞULLLAR (CONDITIONS)
###########

if 1 == 1:
    print("something")


def number_check(number):
    if number == 10:
        print("number is 10")
    else:
        print("noo")


number_check(10)
number_check(12)


#############################
# elif

def number_check(number):
    if number == 10:
        print("number is 10")
    elif number < 10:
        print("noo")
    elif number > 10:
        print("yesss")


number_check(12)
number_check(4)

####################################################################
#### DÖNGÜLER ####
####################################################################

## for loop

students = ["John", "Mark", "Venessa", "Mariam"]
students[0]
students[3]

for student in students:
    print(student)

for student in students:
    print(student.upper())

salaries = [1000, 2000, 3000, 4000, 5000]

for salary in salaries:
    print(salary)

for salary in salaries:
    print(int(salary + salary * 2 / 10))


def new_salary(salary, rate):
    return int(salary * rate / 100 + salary)


new_salary(1500, 10)

salaries2 = [24000, 23421, 32323, 32445]

for salary in salaries2:
    print(new_salary(salary, 14))

for salary in salaries:
    if salary >= 3000:
        print(new_salary(salary, 10))
    else:
        print(new_salary(salary, 20))


############################################################################################################
######## UYGULAMA : MÜLAKAT SORUSU
############################################################################################################

# AMAÇ : Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.

# before :"hi my name is john and i am learning python"
# after : "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def alternating(string):
    new_string = ""
    for string_index in range(len(string)):
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        else:
            new_string += string[string_index].lower()


     print(new_string)

alternating("miuul")


############################################################################3
######### ENUMERATE : Otomatik Counter ile for loop #############

students = ["John", "Mark", "Venessa", "Mariam"]

for student in students:
    print(student)

for index ,student in enumerate(students) :
    print(index,student)

students = ["John", "Mark", "Venessa", "Mariam"]

A = []
B = []

for index, student in enumerate(students):
    if index % 2 == 0:
        A.append(student)
    else:
        B.append(student)

A[0]
A[1]


#######################################
############# ZİP #####################

students = ["John", "Mark", "Venessa", "Mariam"]

departmans = ["mat" , "fen" ,"sos" ,"türkçe"]

ages = [12 , 34 , 23, 55]

list(zip(students,departmans,ages))

##########################################################################
# LAMBDA , MAP , FİLTER ,REDUCE
##########################################################################
#lambda

new_sum = lambda a,b : a + b

new_sum(4,5)

#map

salaries = [1000 ,2000 ,3000, 4000 , 5000]

def new_salary(x):
    return x * 20 / 100 + x

new_salary(5000)

for salary in salaries:
    print(new_salary(salary))

list(map(new_salary,salaries))

list(map(lambda x: x * 20 / 100 + x , salaries))
#del new_sum

list(map(lambda x: x ** 2 , salaries))


# FILTER

list_store = {1 , 2, 3, 4, 5, 6, 7, 8, 9, 10}
list(filter(lambda x :x % 2 == 0 , list_store))

#REDUCE

from functools import reduce
list_store = [1 , 2, 3 ,4]
reduce(lambda a , b: a+b ,list_store)