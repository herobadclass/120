#Jeffrey Feng
#CMPT 120 D100
#Assignment #1
#DUE: OCT 2nd 2017
#Purpose of this program is to convert worldcoins, bytecoins and bitcoins to the total amount of bitcoins and its value in Canadian dollars, and convert
#Canadian dollars to worldcoins, bytecoins, bitcoins and the leftover change along with a code based on the calculations

from random import randint

#start of program purpose
print("Welcome to the cryptocurrency exchange system.")
print()
print("You will be able to calculate the following,")
print("a. worldcoins, bytecoins and bitcoins to the total of bitcoins and Canadian dollars (CAD),")
print("b. Canadian dollars (CAD) to worldcoin, bytecoin and bitcoins.")
print()
print("The user will be shown a secret code based on the calculations and values provided by the user.")
print()
print()
print("Please follow the system prompts.")
#end of program purpose
print()
#start of program
print("Let's begin!")
print()
print("Provide the bitcoin rate in Canadian dollars")
CAD_to_bitcoin = float(input("Enter the amount of Canadian dollars per 1 bitcoin: "))
print()
#start calculation a)
condition = input("Do you wish to proceed with calculation a? (type 'yes' to proceed): ")
print()
if(condition == "yes"):
    print("--------------------------------------------------")
    print("Calculation a):")
    print()
    worldc = int(input("Provide the number of Worldcoins: "))
    bytec = int(input("Provide the number of Bytecoins: "))
    bitc = int(input("Provide the number of Bitcoins: "))
    totalbitc = (worldc * 32) + (bytec * 8) + bitc
    print("The coins provided above is equal to", totalbitc, "bitcoin(s).")
    print()
    print(totalbitc, "bitcoin corresponds to", round(totalbitc * CAD_to_bitcoin,2), "Canadian dollars.")
    print()
    print("Caluclation a) is finished.")
    print("--------------------------------------------------")
else:
    print("Calculation a) was skipped.")
    print("--------------------------------------------------")
#end of calculation a)
print()
#start of calculation b)
print("--------------------------------------------------")
print("Calculation b):")
print()
user_CAD = float(input("Enter the amount of Canadian dallars to be converter into cryptocurrencies: "))
rema_CAD = user_CAD % CAD_to_bitcoin
user_bitc = user_CAD // CAD_to_bitcoin
print("trace of total bitcoin:",int(user_bitc))
user_worldc = user_bitc // 32
print("trace of final worldcoin:",int(user_worldc))
user_bitc = user_bitc % 32
print("trace of intermediate bitcoin:",int(user_bitc))
user_bytec = user_bitc // 8
print("trace of final bytecoin:",int(user_bytec))
user_bitc = user_bitc % 8
print("trace of final bitcoin:",int(user_bitc))
print()
print("The coins you will recive with",user_CAD,"Canadian dollars are:")
print(int(user_worldc),"Wroldcoins")
print(int(user_bytec),"Bytecoins")
print(int(user_bitc),"Bitcoins")
print("and your change is",rema_CAD,"Canadian dollars.")
print()
print("Calculaton b) is finsihed.")
print("--------------------------------------------------")
#end of calculation b)
print()
#start of calculation c)
print("--------------------------------------------------")
print("Calculation c):")
print()  
if((user_bitc % 2) == 0):
    code_dollar = "$$"
else:
    code_dollar = "$"
code_stars = "**"
code_worldc = "W" * int(user_worldc)
code_bytec = "B" * int(user_bytec)
code_sqrt = (user_CAD ** 0.5)
print("trace of the square root of the total money amount:",code_sqrt)
code = code_dollar + code_stars +code_worldc + code_stars + code_bytec + code_stars + str(int(code_sqrt))
if((len(code) % 2) == 0):
    print("trace of length of string",len(code))
    print("trace of length is even")
    code_length = "2"
else:
    print("trace of length of string",len(code))
    print("trace of length is odd")
    code_length = "1"
print("trace of number in 1st decimal place:",int((code_sqrt - int(code_sqrt))*10))
generated_num = randint(0, int((code_sqrt - int(code_sqrt))*10))
print("trace of number of exclamation marks:",generated_num)
print()
code_exclam = "!" * generated_num
code = code + code_length + code_exclam
print("The secret code is:",code)
print()
print("Calculation c) is finished.")
print("--------------------------------------------------")
#end of calculation c)
print()
print("This is the end of the program.")
#end of program
