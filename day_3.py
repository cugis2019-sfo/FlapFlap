'''
#learning about tables and data in python
#practicing variables
cadbury1 = "Milk Chocolate"
cadbury2 = "Dark Chocolate"
cadbury3 = "White Chocolate"


cadburymilk = 5
cadburydark = 3
cadburywhite = 8


chocolate1 = {"milk":5}
chocolate2 = {"dark":3}
chocolate3 = {"white":8}
print(chocolate1, chocolate2, chocolate3)
'''


#one-line variables
chocolate = {"cadburymilk":5, "cadburydark":3,"cadburywhite":8}

print(chocolate)


student = {"Steve":32,"Lia":28,"Vin":45,"Katie":38}
print(student)


gender = {"Steve":"male","Lia":"female","Vin":"male","Katie":"female"}
print(gender)


#pandas
import pandas
dir(pandas)

student = pandas.Series(student)
gender = pandas.Series(gender)
chocolate = pandas.Series(chocolate)

print(gender)
print(student)
print(chocolate)


#data-frame
chocolatedata = [chocolate]
chocolatedf = pandas.DataFrame(chocolatedata, index=["quantity"])
print(chocolatedf)


genderdata = [gender]
genderdf = pandas.DataFrame(genderdata, index=["quantity"])
print(genderdf)


studentdata = [student]
studentdf = pandas.DataFrame(studentdata, index=["quantity"])
print(studentdf)

studentlist = [["Steve",32,"male"],["Lia",28,"female"],["Vin",45,"male"],["Katie",38,"female"]]
studentlistdf = pandas.DataFrame(studentlist,columns=["Name","Age","Gender"],index=["1","2","3","4"])
print(studentlistdf)
        

studentdf1  = [student,gender]
print(studentdf1)

studentdf2 = pandas.DataFrame(studentdf1,index=["age","gender"])
print(studentdf2)

