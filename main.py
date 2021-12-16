# QAP 5 - One Stop Insurance Company
# Heather Bartlett
# Started Dec 5 2021 - Last Modified Dec 8 2021

import datetime

# Opens the file and reads the values
f = open("OSICDef.dat", "r")
# Sets up constants from file
POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISC_RATE = float(f.readline())
EXTRA_LIABILITY = float(f.readline())
GLASS_COVERAGE = float(f.readline())
LOANER_CAR_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
MONTHLY_PROCESSING_FEE = float(f.readline())

while True:
    # User inputs
    # Adding validations
    while True:
        AllowedChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        CustFirstName = input("Enter the customers first name: ")
        if CustFirstName.title() == "" or set(CustFirstName).issubset(AllowedChar) == False:
            print("Name cannot be empty or contain numbers. Please enter again.")
        else:
            break
    while True:
        AllowedChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        CustLastName = input("Enter the customers last name: ")
        if CustLastName.title() == "" or set(CustLastName).issubset(AllowedChar) == False:
            print("Name cannot be empty or contain numbers. Please enter again.")
        else:
            break
    while True:
        AllowedChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-.'1234567890")
        Address = input("Enter the address: ")
        if Address.title() == "" or set(Address).issubset(AllowedChar) == False:
            print("Address cannot be empty or contain invalid characters. Please enter again.")
        else:
            break
    while True:
        AllowedChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.")
        City = input("Enter the city: ")
        if City == "" or set(City).issubset(AllowedChar) == False:
            print("City cannot be empty or contain invalid characters. Please enter again.")
        else:
            break
    while True:
        AllowedChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        Province = input("Enter the province: ")
        if Province == "" or set(Province).issubset(AllowedChar) == False:
            print("Province cannot be empty or contain invalid characters. Please enter again.")
        else:
            break
    while True:
        AllowedChar = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890")
        PostalCode = input("Enter the postal code (A1A1A1): ")
        if PostalCode == "" or set(PostalCode).issubset(AllowedChar) == False:
            print("Postal code cannot be empty or contain invalid characters. Please enter again.")
        elif len(PostalCode) != 6:
            print("Postal code must be exactly 6 characters. Please enter again.")
        else:
            break
    while True:
        AllowedChar = set("1234567890")
        CustPhoneNum = input("Enter the customers phone number (9999999999): ")
        if len(CustPhoneNum) != 10 or set(CustPhoneNum).issubset(AllowedChar) == False:
            print("Phone number must be exactly 10 digits and only contain numbers. Please enter again.")
        else:
            break

    print()
    while True:
        NumCars = int(input("Enter the number of cars being insured: "))
        if NumCars == "":
            print("Cannot be blank. Please enter again.")
        else:
            break
    while True:
        ExtraLiability = input("Would you like extra liability up to $1,000,000? (Y/N) ")
        if ExtraLiability.upper() == "Y":
            ExtraLiabilityCost = EXTRA_LIABILITY
            break
        elif ExtraLiability.upper() == "N":
            ExtraLiabilityCost = 0
            break
        else:
            print("Must be Y or N. Please enter again.")
    while True:
        GlassCoverage = input("Would you like glass coverage? (Y/N) ")
        if GlassCoverage.upper() == "Y":
            GlassCoverageCost = GLASS_COVERAGE
            break
        elif GlassCoverage.upper() == "N":
            GlassCoverageCost = 0
            break
        else:
            print("Must be Y or N. Please enter again")
    while True:
        LoanerCar = input("Loaner car coverage? (Y/N) ")
        if LoanerCar.upper() == "Y":
            LoanerCarCost = LOANER_CAR_COVERAGE
            break
        elif LoanerCar.upper() == "N":
            LoanerCarCost = 0
            break
        else:
            print("Must be Y or N. Please enter again.")
    while True:
        PaymentType = input("Do you want to pay in full or monthly? (F/M) ")
        if PaymentType.upper() == "M":
            break
        elif PaymentType.upper() == "F":
            break
        else:
            print("Must be F or M. Please enter again.")

    # Calculations
    ExtraCarDisc = BASIC_PREMIUM * ADD_CAR_DISC_RATE
    if NumCars > 1:
        InsurancePremium = BASIC_PREMIUM + ((NumCars - 1) * ExtraCarDisc)
    else:
        InsurancePremium = BASIC_PREMIUM

    TotalExtraCosts = ExtraLiabilityCost + GlassCoverageCost + LoanerCarCost
    TotalInsurancePremium = TotalExtraCosts + InsurancePremium
    HSTCost = HST_RATE * TotalInsurancePremium
    TotalCost = TotalInsurancePremium + HSTCost
    if PaymentType.upper() == "M":
        MonthlyPayment = (TotalCost + MONTHLY_PROCESSING_FEE) / 12


    # Display receipt
    print()
    print(" " *15, "ONE STOP INSURANCE COMPANY")
    print(" " *16, "INSURANCE POLICY RECEIPT")
    print("=" *56)
    print("Policy Number:                          {}".format(POLICY_NUM))
    print("Customer Name:                          {} {}".format(CustFirstName, CustLastName))
    print("Address:                       {} {} {} {}".format(Address, City, Province, PostalCode))
    print("Phone Number:                           {}".format(CustPhoneNum))
    print()
    print("Amount of Cars Being Insured:                       {}".format(NumCars))
    print("Extra Liability:                                    {}".format(ExtraLiability.upper()))
    print("Glass Coverage:                                     {}".format(GlassCoverage.upper()))
    print("Loaner Car:                                         {}".format(LoanerCar.upper()))
    print("Payment Type:                                       {}".format(PaymentType.upper()))
    print("=" * 56)
    print("Total Extra Costs:                           ${:,.2f}".format(TotalExtraCosts))
    print("Total Insurance Premium:                     ${:,.2f}".format(TotalInsurancePremium))
    print("HST:                                         ${:,.2f}".format(HSTCost))
    print("Total Cost:                                  ${:,.2f}".format(TotalCost))
    print()
    print()

    # Increase policy number for next policy, making sure everything is in the file
    POLICY_NUM += 1
    f = open("OSICDef.dat", "w")
    f.write("{}\n".format(str(POLICY_NUM)))
    f.write("{}\n".format(str(BASIC_PREMIUM)))
    f.write("{}\n".format(str(ADD_CAR_DISC_RATE)))
    f.write("{}\n".format(str(EXTRA_LIABILITY)))
    f.write("{}\n".format(str(GLASS_COVERAGE)))
    f.write("{}\n".format(str(LOANER_CAR_COVERAGE)))
    f.write("{}\n".format(str(HST_RATE)))
    f.write("{}\n".format(str(MONTHLY_PROCESSING_FEE)))
    f.close()

    # Add policy to file
    f = open("Policies.dat", "a")
    f.write("{}, ".format(POLICY_NUM))
    f.write("{}, ".format(CustFirstName))
    f.write("{}, ".format(CustLastName))
    f.write("{}, ".format(Address))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Province))
    f.write("{}, ".format(PostalCode))
    f.write("{}, ".format(CustPhoneNum))
    f.write("{}, ".format(NumCars))
    f.write("{}, ".format(ExtraLiability))
    f.write("{}, ".format(GlassCoverage))
    f.write("{}, ".format(LoanerCar))
    f.write("{}, \n".format(PaymentType))

    print("Policy processed and saved.")
    print()

    # Give user option to continue
    Continue = input("Would you like to enter another policy? (Y/N) ")
    if Continue.upper() == "N":
        break

# Policy listing
Today = datetime.datetime.now()
print()
print()
print("ONE STOP INSURANCE COMPANY")
print("POLICY LISTING AS OF", Today.strftime("%d-%b-%y"))
print()
print("POLICY  CUSTOMER             INSURANCE     EXTRA      TOTAL")
print("NUMBER  NAME                  PREMIUM      COSTS     PREMIUM")
print("="*68)
print(" {}   {} {}              ${:,.2f}     ${:,.2f}   ${:,.2f}".format(POLICY_NUM, CustFirstName, CustLastName, TotalInsurancePremium, TotalExtraCosts, TotalCost))
print("="*68)
print("Total Policies:")
# Struggling to figure out how to print multiple policies
print()
print()

# Monthly payment listing
print("ONE STOP INSURANCE COMPANY")
print("MONTHLY PAYMENT LISTING AS OF", Today.strftime("%d-%b-%y"))
print()
print("POLICY  CUSTOMER               TOTAL                TOTAL         MONTHLY")
print("NUMBER  NAME                  PREMIUM      HST      COST          PAYMENT")
print("="*70)
print(" {}   {} {}              ${:,.2f}     ${:,.2f}   ${:,.2f}    ${:,.2f}".format(POLICY_NUM, CustFirstName, CustLastName, TotalInsurancePremium, HSTCost, TotalCost, MonthlyPayment))
print("="*70)
print("Total Policies:")
# Unsure of how to make this part work