# Project Title: Travel Service System
# Group Members: Hendrick Amadeus L. Negapatan,David C. Ortiz, Eunice Kieth Hinayan
# Description: A system that allows users to choose transportation, select a tier,
# calculate fare, and print a receipt 

# these are our FUNCTIONS we use these to decompose the problem
def ShowMenu():
    print("\n=== Travel Services ===") #This displays the Travel Options
    print("1. Bus")
    print("2. Taxi")
    print("3. Van")
    print("4. Exit")

def GetTransportChoice(): #This asks the user which decision will he pick.If he answers anything else than the given numbers it will be shown as invalid
    while True:
        try:
            choice = int(input("Choose transport (1-4): "))
            if choice in [1, 2, 3, 4]:
                return choice
            else:
                print("Invalid choice! Try again.")
        except:
            print("Please enter a number.")

def GetTier():# Here It asks the user what tier of the transportation service they want. Here it also displays an invalid message if you choose a wrong number
    print("\n--- Service Tiers ---")
    print("1. Premium (Aircon, No Stops)")
    print("2. Standard (Aircon, With Stops)")
    print("3. Basic (No Aircon, With Stops)")
    
    while True:
        try:
            tier = int(input("Choose tier (1-3): "))
            if tier in [1, 2, 3]:
                return tier
            else:
                print("Invalid tier! Try again.")
        except:
            print("Enter a valid number.")

def GetDistance():#This will ask the user for the distance he/she will travel in order to compute the price
   while True:
        try:
            distance = float(input("Enter distance (km): "))
            if distance > 0:
                return distance
            else:
                print("Distance must be positive.")
        except:
            print("Invalid input! Enter a number.")

def CalculateFare(transport, tier, distance):#this is where we calculate the cost of the users journey
    # these are the Base rates
    if transport == 1:
        base_rate = 5   # Bus
    elif transport == 2:
        base_rate = 10  # Taxi
    else:
        base_rate = 8   # Van

    #  the price of the fare depends on the Tier multipliers
    if tier == 1:
        multiplier = 1.5
    elif tier == 2:
        multiplier = 1.2
    else:
        multiplier = 1

    return base_rate * distance * multiplier

def GetTransportName(transport): #This is where the user chooses their transportation choice
    if transport == 1:
        return "Bus"
    elif transport == 2:
        return "Taxi"
    else:
        return "Van"

def GetTierName(tier):
    if tier == 1:
        return "Premium (Aircon, No Stops)"
    elif tier == 2:
        return "Standard (Aircon, With Stops)"
    else:
        return "Basic (No Aircon, With Stops)"

def ComputeVAT(amount):
    return amount * 0.12

def ComputeTotal(amount, vat):
    return amount + vat

def PrintReceipt(transport, tier, distance, fare):# this is where we see the final receipt of the user
    transport_name = GetTransportName(transport)
    tier_name = GetTierName(tier)

    vat = ComputeVAT(fare)
    total = ComputeTotal(fare, vat)

    print("\n========== RECEIPT ==========")
    print("Transport:", transport_name)
    print("Tier:", tier_name)
    print("Distance:", distance, "km")
    print("-----------------------------")
    print("Base Fare: ₱", round(fare, 2))
    print("VAT (12%): ₱", round(vat, 2))
    print("-----------------------------")
    print("TOTAL: ₱", round(total, 2))
    print("=============================")

# this is our MAIN PROGRAM,where all the calculations happen and where it decides to end the program

while True:
    ShowMenu()
    choice = GetTransportChoice()

    if choice == 4:
        print("Thank you for using the system!")
        break

    tier = GetTier()
    distance = GetDistance()

    fare = CalculateFare(choice, tier, distance)

    PrintReceipt(choice, tier, distance, fare)
