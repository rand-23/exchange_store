USD = 1
EUR = 0.99
SAR = 3.75
print("===========================")
print("Welcome to $$ Exchange Store $$")
print("===========================\n")

From = input("Exchange From(USD, EUR, SAR): ").upper()
Amount = float(input("How Much? "))
To = input("Exchange To(USD, EUR, SAR): ").upper()


NewAmount = 0
if From == To:
    print("You will keep your amount as it is: ", Amount, From)
    exit()
elif From == "USD" and To == "EUR":
    NewAmount = Amount * EUR
   
elif From == "USD" and To == "SAR":
    NewAmount = Amount * SAR

elif From == "EUR" and To == "USD":
    NewAmount = Amount / EUR

elif From == "EUR" and To == "SAR":    
    NewAmount = Amount / EUR * SAR

elif From == "SAR" and To == "USD":
     NewAmount = Amount / SAR

elif From == "SAR" and To == "EUR":
 NewAmount = Amount / SAR *EUR

else:
    print("You wrote wrong currancy!")
    exit()
print("You will give: " + str(Amount) + From + ", and you will take: " + str(NewAmount) + To)