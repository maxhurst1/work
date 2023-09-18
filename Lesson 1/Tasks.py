morse = {
   "A": ".-",
   "B": "-...",
   "C": "-.-.",
   "D": "-..",
   "E": ".",
   "F": "..-.",
   "G": "--.",
   "H": "....",
   "I": "..",
   "J": ".---",
   "K": "-.-",
   "L": ".-..",
   "M": "--",
   "N": "-.",
   "O": "---",
   "P": ".--.",
   "Q": "--.-",
   "R": ".-.",
   "S": "...",
   "T": "-",
   "U": "..-",
   "W": ".--",
   "X": "-..-",
   "Y": "-.--",
   "Z": "--.."
}

def menu():
    print("1. area of tri \n2. power calc \n3. sum of 2 num \n4. convert age to day \n5. morse code \n6. profit!")
    option = input("enter option: ")

    if option == "1":
        print(triArea(input("base: "),input("height: ")))
    elif option == "2":
        print(circuit_power(input("voltage: "), input("current: ")))
    elif option == "3":
        print(addition(input("number one: "), input("number 2: ")))
    elif option == "4":
        print(calc_age(input("age: ")))
    elif option == "5":
        print(encode_morse(input("content: ")))
    elif option == "6":
        print(profit({
            "cost_price": input("cost price: "),
            "sell_price": input("sell price: "),
            "inventory": input("inventory: ")
        }))
    else:
        print("invalid option")

def triArea(base, height):
    return (int(base) * int(height)) / 2

# print(triArea(input("base: "),input("height: ")))

def circuit_power(voltage, current):
    return int(voltage) * int(current)

# print(circuit_power(input("voltage: "), input("current: ")))

def addition(num, numm):
    num = int(num)
    numm = int(numm)

    if num % 7 == 0 or numm % 7 == 0:
        return num / numm
    elif num % 11 == 0 or numm % 11 == 0:
        return num * numm
    
    return num + numm

# print(addition(input("number one: "), input("number 2: ")))

def calc_age(age):
    return int(age) * 365

# print(calc_age(input("age: ")))

def encode_morse(content):
    result = ""
    
    for char in content:
        if char in morse.keys():
            result += morse[char]
        else:
            result += char

    return result

# print(encode_morse(input("content: ")))

def profit(obj):
    cost = float(obj["cost_price"]) * float(obj["inventory"])
    sales = float(obj["sell_price"]) * float(obj["inventory"])

    return round(sales - cost)

'''
print(profit({
        "cost_price": input("cost price: "),
        "sell_price": input("sell price: "),
        "inventory": input("inventory: ")
    }))
'''

while True:
    menu()
