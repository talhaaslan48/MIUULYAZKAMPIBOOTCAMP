###### PANDAS  #########

# Pandas Series #

import  pandas as pd

s = pd.Series([10 ,77 ,12 ,4 ,5])
type(s)
s.index
s.dtype
s.size
s.ndim
s.values
type(s.values)
s.head((3))
s.tail((3))

#### Veriye Hızlı Bakış #####

import pandas as pd
import seaborn as sns


df = sns.load_dataset("titanic")
df.head()
df.info
df.columns
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df["sex"].head()
df["sex"].value_counts()

#### Pandas'ta Seçim İşlemleri ####

df.index
df[0:13]
df.drop(0 ,axis=0).head()

delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes,axis=0).head(10)

### Değişkeni İndexe Çevirmek

df["age"].head()

df.index = df["age"]
df.drop("age" , axis=1).head()

df.drop("age" , axis=1 , inplace=True)
df.head()


### İndexi Değişkene Çevirmek

df.index

df["age"] = df.index

df.head()
df.drop("age" , axis=1 , inplace=True)

#### Değişkenler Üzerinde İşlemler

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns" , None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())

df[["age"]].head()
type(df[["age"]].head())

df[["age" , "alive"]]

col_names = ["age" , "adult_male" ,"alive"]
df[col_names]

df["age2"] = df["age"] ** 2

df["age3"] = df["age"] / df["age2"]
df["age3"]

df.drop("age3" , axis=1).head()

df.drop(col_names , axis=1).head()

df.loc[:, df.columns.str.contains("age")].head()

df.loc[:, ~df.columns.str.contains("age")].head()


###  iloc & loc  ###

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns" , None)
df = sns.load_dataset("titanic")
df.head()

#iloc : integer based selection

df.iloc[0:3]

#loc : label based selection

df.loc[0:3]

df.iloc[0:3 , 0:3]

df.loc[0:3 , "age"]

col_names = ["age" , "adult_male" ,"alive"]
df.loc[0:3 ,col_names]



### Koşullu Seçim  -(Conditional Selection) ###


import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns" , None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50 , ["age" , "class"]].head()

df["embark_town"].value_counts()

 df_new = df.loc[(df["age"] > 50 )
       & (df["sex"] == "male")
       &  ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age" , "class" ,"embark_town"]].head()

df_new["embark_town"].value_counts()


### Toplulaştırma ve Gruplama ###

#-count()
#-first()
#-last()
#-mean()
#-median()
#-min()
#-max()
#-std()
#-var()
#-sum()
#-pivot table

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns" , None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age" : "mean"})

df.groupby("sex").agg({"age" : ["mean" , "sum"]})

df.groupby("sex").agg({"age" : ["mean" , "sum"],
                     "embark_town" :"count"})

df.groupby(["sex" ,"embark_town"]).agg({"age" : ["mean" , "sum"],
                       "survived" :"mean"})

df.groupby(["sex" ,"embark_town","class"]).agg({"age" : ["mean" , "sum"],
                       "survived" :"mean"})

df.groupby(["sex" ,"embark_town","class"]).agg({"age" : ["mean" , "sum"],
                       "survived" :"mean",
                      "sex" : "count"})

### Pivot Table ###

import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns" , None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived" ,"sex" ,"embarked")

df.pivot_table("survived" ,"sex" ,"embarked" ,aggfunc="std")

df.pivot_table("survived" ,"sex" ,["embarked" ,"class"])

df["new_age"] = pd.cut(df["age"] , [0 , 10 ,18 , 25 ,40,90])
df.head()

df.pivot_table("survived" , "sex" , "new_age")

df.pivot_table("survived" , "sex" , ["new_age" ,"class"])

pd.set_option("display.width" ,500)

##### Apply & Lambda ####


import pandas as pd
import seaborn as sns

pd.set_option("display.max_columns" , None)
pd.set_option("display.width" ,500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

df[["age" ,"age2" ,"age3"]].apply(lambda x: x/10).head()

 # df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

 # df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()
# Ortalamadan çıkarıp standart sapmaya bölecek



### Birleştirme İşlemleri ###

import numpy as np
import pandas as pd
m= np.random.randint(1,30, size=(5,3))
df1 = pd.DataFrame(m,columns=["var1" , "var2" ,"var3"])
df2 = df1 + 99

pd.concat([df1 , df2])

pd.concat([df1 , df2] , ignore_index=True)

### VERİ GÖRSELLEŞTİRME : MATPLOTLIB & SEABORN

###  Matplotlib ###
# Kategorik değişken : Sütun Grafik - countplot bar
#Sayısal Değişken : Hist , Boxplot

# Kategorik Değişken Görselleştirme

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns" , None)
pd.set_option("display.width" ,500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].value_counts().plot(kind = "bar")
plt.show()

df["class"].value_counts().plot(kind = "bar")
plt.show()

##Sayısal Değişken Görselleştirme ##

plt.hist(df["age"])
plt.show()

 ### Matplotlib ' in Özellikleri

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_columns" , None)
pd.set_option("display.width" ,500)

# 1-plot

x = np.array([1,8])
y = np.array([0,150])

plt.plot(x ,y)
plt.show()

plt.plot(x ,y,"o")
plt.show()


x = np.array([2,4,6,8,10])
y = np.array([1,3,5,7,9])


plt.plot(x ,y ,"o")
plt.show()


# 2-marker

y = np.array([13,28,11,100])
plt.plot(y , marker="o")
plt.show()

plt.plot(y , marker="H")
plt.show()

# 3-Line


y = np.array([13,28,11,100])
plt.plot(y , linestyle = "dotted")
plt.show()

y = np.array([13,28,11,100])
plt.plot(y , linestyle = "dashdot", color ="r")
plt.show()

# 4-Multiple Lines


x = np.array([23,18,31,10])
y = np.array([13,28,11,100])

plt.plot(x)
plt.plot(y)
plt.show()

# 5-Labels

x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.plot(x,y)
plt.title("Burası Başlık")
plt.xlabel("x kısmı")
plt.ylabel("y kısmı")
plt.grid()
plt.show()

#6-Subplots


x = np.array([80,85,90,95,100,105,110,115,120,125])
y = np.array([240,250,260,270,280,290,300,310,320,330])
plt.subplot(1 , 3, 1)
plt.title("1")
plt.plot(x,y)

x = np.array([8,8,9,9,10,15,11,15,12,15])
y = np.array([24,20,26,27,280,29,30,30,30,30])
plt.subplot(1 , 3, 2)
plt.title("2")
plt.plot(x,y)

x = np.array([8,8,9,9,10,15,11,15,12,15])
y = np.array([24,20,26,27,280,29,30,30,30,30])
plt.subplot(1 , 3, 3)
plt.title("3")
plt.plot(x,y)

# Seaborn ile Veri Görselleştirme

import pandas as pd
import seaborn as sns
from  matplotlib import  pyplot as plt
df= sns.load_dataset("tips")
df.head()

df["sex"].value_counts()
sns.countplot(x = df["sex"],data = df)
plt.show()

df["sex"].value_counts().plot(kind = "bar")

# Sayısal Değişkenleri Görselleştirme

sns.boxplot(x = df["total_bill"])
plt.show()

df["total_bill"].hist()
plt.show()




 #############################################################333
 ### GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ
 # 1 - Genel Resim
 # 2 - Kategorik Değişken Analizi
 # 3 - Sayısal Değişken Analizi
 # 4 - Hedef Değişken Analizi
 # 5 - Korelasyon Analizi


# 1 - Genel Resim

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns" , None)
pd.set_option("display.width" ,500)
df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()

def check_df(dataframe , head= 5):
    print("##############SHAPE###################")
    print(dataframe.shape)
    print("##############TYPES###################")
    print(dataframe.dtypes)
    print("##############HEAD###################")
    print(dataframe.head(head))
    print("##############TAİL###################")
    print(dataframe.tail(head))
    print("############## NA ###################")
    print(dataframe.isnull().sum())
    print("############## QUANTİLES ###################")
    print(dataframe.describe([0 , 0.05 , 0.50 , 0.95 , 0.99 , 1]).T)

check_df(df)



df = sns.load_dataset("tips")
check_df(df)

# 2 - Kategorik Değişken Analizi

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns" , None)
pd.set_option("display.width" ,500)
df = sns.load_dataset("titanic")
df.head()

df["embarked"].value_counts()
df["sex"].unique()
df["class"].value_counts()

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category" , "object" , "bool"]]

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64" , "float64"]]

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category" , "object"]]

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]

df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols]


df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)
def cat_summary(dataframe , col_name):
    print(pd.DataFrame({col_name : dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("########################################################################################")

cat_summary(df , "sex")

    for col in  cat_cols:
        cat_summary(df ,col)
# Burası Gibi Kullanıcaz Asıl Yerimiz Bu
def cat_summary(dataframe , col_name ,plot =False):
    print(pd.DataFrame({col_name : dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("########################################################################################")

    if plot :
        sns.countplot(x = dataframe[col_name] , data = dataframe)
        plt.show(block = True)

    cat_summary(df, "sex" ,plot=True)

    for col in cat_cols:
        if df[col].dtypes == "bool":
            print(col)
        else :
        cat_summary(df,col,plot=True)


df["adult_male"].astype(int)

for col in cat_cols:
    if df[col].dtypes == "bool":
       df[col] =  df[col].astype(int)
       cat_summary(df, col, plot=True)

    else:
        cat_summary(df, col, plot=True)



def cat_summary(dataframe , col_name ,plot =False):
    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)

    print(pd.DataFrame({col_name : dataframe[col_name].value_counts(),
                        "Ratio" : 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("########################################################################################")

    if plot :
        sns.countplot(x = dataframe[col_name] , data = dataframe)
        plt.show(block = True)

    else :
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("########################################################################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

cat_summary(df,"adult_male" ,plot=True)


 # 3- Sayısal Değişken Analizi

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns" , None)
pd.set_option("display.width" ,500)
df = sns.load_dataset("titanic")
df.head()

df[["age","fare"]].describe().T

num_cols = [col for col in df.columns if df[col].dtypes in ["int64" , "float64"]]
num_cols = [col for col in num_cols if col not in cat_cols]

def num_summary(dataframe , numerical_col):
    quantiles = [0.05 ,0.10 ,0.15, 0.20 ,0.25 , 0.30, 0.35, 0.40 ,0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75 ,0.80, 0.85 ,0.90 ,0.95, 0.99]

    print(dataframe[numerical_col].describe(quantiles).T)

num_summary(df , "age")

for col in num_cols :
    num_summary(df,col)

def num_summary(dataframe , numerical_col , plot=False):
    quantiles = [0.05 ,0.10 ,0.15, 0.20 ,0.25 , 0.30, 0.35, 0.40 ,0.45, 0.50, 0.55, 0.60, 0.65, 0.70, 0.75 ,0.80, 0.85 ,0.90 ,0.95, 0.99]

    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

for col in num_cols :
    num_summary(df,col,plot=True)

 # 4- Değişkenlerin Yakalanması ve İşlemlerin Genelleştirilmesi


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns" , None)
pd.set_option("display.width" ,500)
df = sns.load_dataset("titanic")
df.head()
df.info()

#docstring
def grab_col_names(dataframe , cat_th = 10 , car_th=20):
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat

    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int64" , "float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observation : {dataframe.shape[0]}")
    print(f"Variables : {dataframe.shape[1]}")
    print(f"cat_cols : {len(cat_cols)}")
    print(f"num_cols : {len(num_cols)}")
    print(f"cat_but_car : {len(cat_but_car)}")
    print(f"num_but_car : {len(num_but_cat)}")

    return cat_cols , num_cols , cat_but_car

cat_cols , num_cols , cat_but_car = grab_col_names(df)

# BONUS

df = sns.load_dataset("titanic")    ,
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)


cat_cols , num_cols , cat_but_car = grab_col_names(df)

# 5 - Hedef Değişken Analizi

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns" , None)
pd.set_option("display.width" ,500)
df = sns.load_dataset("titanic")

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)


 def cat_summary(dataframe, col_name):
            print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                                "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
            print("########################################################################################")

def grab_col_names(dataframe , cat_th = 10 , car_th=20):
    cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]

    cat_but_car = [col for col in df.columns if
                   df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat

    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in df.columns if df[col].dtypes in ["int64" , "float64"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observation : {dataframe.shape[0]}")
    print(f"Variables : {dataframe.shape[1]}")
    print(f"cat_cols : {len(cat_cols)}")
    print(f"num_cols : {len(num_cols)}")
    print(f"cat_but_car : {len(cat_but_car)}")
    print(f"num_but_car : {len(num_but_cat)}")

    return cat_cols , num_cols , cat_but_car

cat_cols , num_cols , cat_but_car = grab_col_names(df)

df.head()

df["survived"].value_counts()
cat_summary(df, "survived")


## Hedef Değişkenin Kategorik Değişkenler ile Analizi

df.groupby("sex")["survived"].mean()


def target_summary_with_cat(dataframe , target ,categorical_col):
    print(pd.DataFrame({"TARGET_MEAN" : dataframe.groupby(categorical_col)[target].mean()}) , end="\n\n\n")

target_summary_with_cat(df , "survived" ,"sex")

target_summary_with_cat( df , "survived" , col)

for col in cat_cols:
    target_summary_with_cat(df , "survived" , col)
# Hedef Değişkenin Sayısal Değişkenler İle Analizi)

def target_summary_with_num(dataframe , target , numerical_col):
    print(dataframe.groupby(target).agg({numerical_col : "mean"}) ,end="\n\n\n")

target_summary_with_num(df , "survived" ,"age")

target_summary_with_num(df , "survived" ,col)





# 6-Korelasyon Analizi

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option("display.max_columns" , None)
pd.set_option("display.width" ,500)
df = sns.load_dataset("titanic")
df = df.iloc[:, 1:-1]
df.head()

num_cols = [col for col in df.columns if df[col].dtype in [int , float]]

corr = df[num_cols].corr()







