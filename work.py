#Operators Arthemetic,Assignment,relational,
x=2
y=3
a=x+y
print(a)
x+=2
print(x)
x<y
c=x==y
print(c)
# Datatype (int, float,boolean,complex, string)
c=2+3j
print(c)
#String method using Build in function
firstName="mukagasaraba"
secondName="rachel"
country="rwanda"
district="rusizi"
lendMoney= 200,000
payedBack=50,000
currency="rwf"
print(f"Dear {firstName.capitalize()} {secondName.capitalize()} who is {2021-1978} years old from {country.upper()} in {district.title()}.We are extrimly excited to give you your remining {200000-5000} {currency.upper()}.")

# dataStructure
foodList=["Bread","Cakes","Meat","Rolls"]
foodList[2]
print(foodList[0:2])
print(foodList[-3:-1])
foodList.append("Marshmallow")
foodList.insert(1,"beans")
foodList.extend(["sweet potatoes","millet "])
foodList.remove("Meat")
foodList.sort()
foodList.reverse()
print(foodList)
foodList.clear()
print(foodList)
#  for loop.Make a list from a nother list
a=[[1,2,3],[4,5,6],[7,8,9]]
b=[]
b=[e for sublist in a  for e in sublist]
print(b)
