#Program to enter and calculate the new insurance policy
#for One Stop Insurance Company
#Date written : NOV 21 2023
#Author : SIREESHA KUPPAMPATI
import datetime
import FormatValues as FV
print()

# Setting program constants
POL_NUM = 1944
BASIC_PREM = 869.00
DISC_ADDT_CARS = 0.25
EXTRA_LIAB_COV_COST = 130.00
GLS_COV_COST = 86.00
LOANER_CARCOV_COST = 58.00
HST_RATE = 0.15
PROC_MON_FEE = 39.99
# Defining program functions
def CalcFullpay():
    global Payment1
    global Payment_Type
    Payment_Type = "Full Payment"
    Payment1 = PROC_MON_FEE + Tot_Ins_Premium
    print(Payment_Type)
    print(Payment1)
def CalcMonthpay():
    global Payment2
    global ClaimAmt
    Payment_Type = "Monthly Payment"
    Payment2 = (PROC_MON_FEE + Tot_Ins_Premium) / 8
    print(Payment_Type)
    print(Payment2)
def CalcDownpay():
    global Payment3
    global ClaimAmt
    Payment_Type = "Monthly Payment with Down Pay" 
    Down_Pay =float(input("How much do you want to down pay : "))  
    Payment3 = ((Tot_Ins_Premium - Down_Pay) + PROC_MON_FEE) / 8
    print(Payment_Type)
    print(Payment3)

# Main program starts here
# Defining  user input values
Curr_Date = datetime.datetime.now()
allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-")
ClaimsList1 = []
ClaimsList2 = []
while True:
    
    while True:
        Cust_Firstname = input("Enter the customer first name(Press END to finish) :    ").title()
        # Checking the firstname validation
        if Cust_Firstname == "":
                print("Customer Firstname must not be blank. Please re-enter:       ")

        elif set(Cust_Firstname).issubset(allowed_char) == False:
            print("Customer Firstname contains invalid characters. Please re-enter:     ")

        else:
            break
         #"END" to quit
    if Cust_Firstname.upper() == "END":
        print("Thank you for visiting !! :")
        break


    while True:
    
        Cust_Lastname = input("Enter the customer last name          :     ").title()
        # Checking the lastname validation
        if Cust_Lastname == "":
            print("Customer Lastname must not be blank. Please re-enter:    ") 
        elif set(Cust_Lastname).issubset(allowed_char) == False:
            print("Customer Lastname contains invalid characters. Please re-enter:    ")
        else:
            break
    FullCustName = Cust_Firstname + " " + Cust_Lastname  

    StAddr = input("Enter the customer street address          : ").upper() 
    City = input("Enter the city                             :    ").title()
    ProvLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
    while True:
        Prov = input("Enter the province (XX): ").upper()
        if Prov == "":
            print("Error - Province cannot be blank - Please reenter.")
        elif len(Prov) != 2:
            print("Error - Province is a 2 digit code - please reenter.")
        elif Prov not in ProvLst:
            print("Error - Not a valid province - please reenter.")
        else:
            break

    PostalCode = input("Enter the postal code                     :   ").upper() 
    Ph_Num = input("Enter the customer phone number (9999999999):    ")
    Ph_Num1 = "(" + Ph_Num[0:3] + ")" + Ph_Num[3:6] + "-" + Ph_Num[6:]

    Liab_Cov = input("Would you like the option for extra liability upto $1,000,000(Y/N): ").upper()
    Ext_service  = 0
    if Liab_Cov == "Y":
        Ext_service = "YES"
        EXTRA_LIAB_COV_COST = 130.00
    else:
        Ext_service  = "NO"
        EXTRA_LIAB_COV_COST = 0
    print()
    print(Ext_service)
    print(EXTRA_LIAB_COV_COST)
    print()

    Glas_Cov = input("Would you like the optional glass coverage(Y/N): ").upper()
    Glass_Service= 0
    if Glas_Cov == "Y":
        Glass_Service = "YES"
        GLS_COV_COST = 86.00
    else:
        Glass_Service  = "NO"
        GLS_COV_COST = 0
    print()
    print(Glass_Service)  
    print(GLS_COV_COST)
    print()

    LoanerCar_Cov = input("Would you like the optional loaner car coverage(Y/N): ").upper()
    Loaner_Service= 0
    if LoanerCar_Cov == "Y":
        Loaner_Service = "YES"
        LOANER_CARCOV_COST = 58.00
    else:
        Loaner_Service  = "NO"
        LOANER_CARCOV_COST = 0
    print()

    # CAlculation Part
    Total_Extra_Costs = EXTRA_LIAB_COV_COST + GLS_COV_COST + LOANER_CARCOV_COST
    
    NoCarsInsured = int(input("Enter the number of cars being insured:  "))
    print(NoCarsInsured)
    Discount =  NoCarsInsured * (BASIC_PREM - (BASIC_PREM * DISC_ADDT_CARS))
    print(Discount)
    if NoCarsInsured > 1:
        Premium = BASIC_PREM + Total_Extra_Costs + Discount
    else:
       Premium = BASIC_PREM + Total_Extra_Costs
    print(Premium)    
    HST = Premium * HST_RATE
    Tot_Ins_Premium = Premium + HST
    print(HST)
    print(Tot_Ins_Premium)

    Payment_Type = ["Full", "Monthly", "Down Pay"]
    while True:
        Status = input("Enter the Payment Type(Full, Monthly, Down Pay): ").title()
        if Status == "":
            print("Error - Status cannot be blank - please reenter.")
        elif Status not in Payment_Type :
            print("Error - invalid entry - must be Full, Monthly or Down Pay - please reenter.")
        else:
            break
    Inv_Date = FV.FDateS(Curr_Date)
    First_Pay_Date = FV.first_day_of_next_month(Curr_Date)
    print(Inv_Date)
    print(First_Pay_Date)

    if Status == "Full":
        CalcFullpay()
        ClaimAmt = Payment1
    elif Status == "Monthly":
        CalcMonthpay()
        ClaimAmt = Payment2
    elif Status == "Down Pay":
        CalcDownpay()
        ClaimAmt = Payment3
    else:
        break

    ClaimDate = FV.FDateS(First_Pay_Date)
    ClaimsList1.append(ClaimDate)
    ClaimsList2.append(ClaimAmt)
    print(ClaimsList1)
    print(ClaimsList2)
    print()
    print()
    print(f"                                                                                                         ")                  
    print(f"                          One Stop Insurance Company                     Policy Number:{POL_NUM:>4d}")                   
    print(f"                          Claim Receipt                                  Invoice Date:{Inv_Date:>12s}")
    print()
    print(f"                    ______________________________________________________________________________________")
    print()
    print(f"                         Customer fullname and Address:                  {FullCustName:<24s}")
    print(f"                                                                         {StAddr:<24s}")                       
    print(f"                                                                         {City:10s},  {Prov:<2s} {PostalCode:>6s} ")
    print(f"                                                                         {Ph_Num1:<12s}")
    print()
    print(f"                         Extra Liabilities Coverage :                    {Ext_service:<3s}:       {FV.FDollar2(EXTRA_LIAB_COV_COST):>10s}")
    print(f"                         Glass Coverage :                                {Glass_Service:<3s}:       {FV.FDollar2(GLS_COV_COST):>10s}")
    print(f"                         Loaner Car Coverage :                           {Loaner_Service:<3s}:       {FV.FDollar2(LOANER_CARCOV_COST):>10s}")
    print()
    print(f"                         Total Coverage Cost :                                      {FV.FDollar2(Total_Extra_Costs):>10s}")
    print(f"                         Number of Cars Insured:                                       {NoCarsInsured:>4d}")
    print(f"                         Premium :                                                    {FV.FDollar2(Premium):>6s} ")

    print(f"                         HST :                                                          {FV.FDollar2(HST):>5s} ")
    print(f"                         Total Insurance Premium :                                   {FV.FDollar2(Tot_Ins_Premium):>10s}")
    print()
    print(f"                         Payment Type :                               {Status:>8s}")
    print(f"                         Claim Amount :                                               {FV.FDollar2(ClaimAmt):>10s}")
    print(f"                         First Payment Date :                                        {FV.FDateS(First_Pay_Date):>12s}")
    print(f"                    -------------------------------------------------------------------------------------")
    print()
print()
print(f"                         Claim #       Claim Date      Amount")
print(f"                    ____________________________________________")
print()
i = 3
for i  in range(len(ClaimDate)):
    print(f"                          {i+1}          {ClaimsList1[i]}      {FV.FDollar2(ClaimsList2[i])}  ")
    print()
print(f"                   -------------------------------------------------------------------------------------")
print()
print()