print("Hello World by Nilesh Tayde")

cost_price= int(input("cp= "))
selling_price= int(input("sp= "))
if cost_price> selling_price:
    print ("loss = " ,cost_price - selling_price)
else:
    print ("profit = " ,selling_price- cost_price)


a=int(input("enter no="))
if a%2==0:
    print("even")
else:
    print("odd")



b=int(input("enter no="))
if b>=18:
    print("elegible for voting")
else:
    print("Not elegible for voting")


f = input()
g = input()

if sorted(f) == sorted(g):
    print("Anagram")
else:
    print("Not Anagram")