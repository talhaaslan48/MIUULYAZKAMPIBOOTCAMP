### List Comprehension


salaries = [1000, 2000, 3000, 4000, 5000]


def new_salary(x):
    return x * 20 / 100 + x


null_list = []

for salary in salaries:
    null_list.append(new_salary(salary))

[new_salary(salary*2) if salary < 3000 else new_salary(salary) for salary in salaries]

[salary * 2 for salary in salaries]

[salary * 2 for salary in salaries if salary <3000]

[salary * 2 if salary < 3000 else salary * 0  for salary in salaries ]

[new_salary(salary * 2) if salary < 3000 else new_salary(salary * 0.2) for salary in salaries ]


students = ["John" , "Mark" ,"Venessa" ,"Mariam"]

students_no = ["John" , "Venessa"]

[student.lower() if student in students_no else student.upper() for student in students]

########### Dict Comprehensions  #################

dictionary = {'a': 1,
              'b': 2,
              'c': 3,
              'd': 4}

   dictionary.keys()
   dictionary.values()
   dictionary.items()

{k: v ** 2 for (k,v) in dictionary.items()}

{k.upper() : v for (k,v) in dictionary.items()}

# Amaç : Çift sayıların karesi alınarak bir sözlüğe eklenecektir.
# Key'ler orj değerler value'ler ise değiştirilmiş değerler olacak

numbers = range(10)
new_dict = {}

for n in numbers :
    if n % 2 == 0:
        new_dict[n] = n ** 2

print(new_dict)

{n: n ** 2 for n in  numbers if n % 2 == 0}