# Fonksiyon tanımlama

def calculate(x) :
    print( x * 2)


calculate(5)
# İki parametreli fonk tanımlama

def summer(arg1 , arg2) :
    print(arg1 + arg2)

summer(23,23)

###### DOCSTRİNG

def summer(arg1 , arg2):
    print(arg1 + arg2)

def summer(arg1, arg2):
    """
    sum of two numbers
    Args:
        arg1: int ,float
        arg2: int, float

    Returns:
        int,float
    """

    print(arg1 + arg2)

 summer(1,3)
###### FONKSİYONLARIN STATEMENT/BODY BÖLÜMÜ

    def say_hi() :
        print("Merhaba")
        print("Hi")
        print("Hello")

say_hi()


def multiplication(a, b):
        c = a * b
        print(c)
multiplication(9,10)



#Girilen değerleri bir liste içinde saklayacak fonksiyon

list_store = []

def add_element(a , b) :
    c = a * b
    list_store.append(c)
    print(list_store)

    add_element(1,8)

    add_element(18, 8)

    add_element(7, 90)


################################################################################3

##Ön Tanımlı Argümanlar

def divide(a , b=1):
    print( a / b)
divide(1)

    def say_hi(string="Merhaba") :
        print(string)
        print("Hi")
        print("Hello")

say_hi("mrb")


##########################################################################33
#DRY
 def calculate(varm,moisture,charge) :
     print((varm + moisture)/charge)

calculate(98,12,78)



#####################################
# RETURN : Fonksiyon Çıktılarını Girdi Olarak Kullanmak

 def calculate(varm,moisture,charge) :
    return ((varm + moisture)/charge)

calculate(98,12,78) * 10


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture)/charge

    return varm , moisture , charge ,output

type(calculate(98 , 12 , 78))


varm , moisture , charge ,output = calculate(98 , 12 , 78)


########################################################
####Fonksiyon İçerisinde Fonksiyon Çağırmak####

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)

calculate(90,12,12) * 10

def standardization(a, p) :
    return a * 10 / 100 * p * p

standardization(45, 1)


def all_calculation(varm, moisture, charge, p) :
    a = calculate(varm , moisture , charge)
    b = standardization(a , p)
    print(b * 10)

all_calculation(1 ,3 ,5 ,12)



def all_calculation(varm, moisture, charge, a, p) :
    print(calculate(varm , moisture , charge))
    b = standardization(a , p)
    print(b * 10)

all_calculation(1 ,3 ,5 ,19 ,12)
