#Starting the program
print("Fraud Detection System")  

# Taking transaction details from user 
amount = int(input("Enter transaction amount: ")) 
curr_loc = input("Enter current location: ")
usual_loc = input("Enter usual location: ")  
hour = int(input("Enter hour (0-23): "))  
recent = int(input("Enter number of recent transactions: "))  

# Defining limit for system rules
AMOUNT_THRESHOLD = 50000  
TRANSACTION_LIMIT = 3  

#Risk score is zero in starting 
risk_score = 0

#Starting the checking 
print("\nChecking conditions...\n") 

#Checking if amount is reasonable or not 
if amount > AMOUNT_THRESHOLD:
    print("High amount detected")
    risk_score = risk_score + 2 

#Checking if location is matching or not 
if curr_loc != usual_loc:
    print("Unusual location detected")
    risk_score = risk_score + 2 

#Checking if time is odd or not 
if hour >= 0 and hour <= 4:
    print("Odd time detected")
    risk_score = risk_score + 1  

#Checking if transactions are too much or not (Number wise)
if recent > TRANSACTION_LIMIT:
    print("Too many transactions detected")
    risk_score = risk_score + 2  

print("\nFinal Result")  # final result show karne ke liye
print("Risk Score:", risk_score)  # total risk score print

#Taking final decision on based on risk 
if risk_score <= 2:
    print("SAFE") 

elif risk_score <= 4:
    print("SUSPICIOUS")  

else:
    print("FRAUD") 