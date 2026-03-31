## Fraud Detection System (Basic Python Project)

This project is a simple rule-based fraud detection system built using basic Python concepts. It analyzes a transaction based on multiple conditions and assigns a risk score to determine whether the transaction is safe, suspicious, or fraudulent.

---

## How It Works

The system takes user input for a transaction and checks it against predefined rules:

* Transaction amount
* Current location vs usual location
* Time of transaction
* Number of recent transactions

Each condition increases the risk score based on how suspicious it is.

---

## Risk Logic

* High amount → +2 risk
* Unusual location → +2 risk
* Odd time (midnight to 4 AM) → +1 risk
* Too many transactions → +2 risk

---

## Final Decision

Based on total risk score:

* 0 to 2 → SAFE
* 3 to 4 → SUSPICIOUS
* 5 or more → FRAUD

---

## Concepts Used

This project is built using only basic Python:

* Variables
* Data types (int, string)
* Input and output
* if, elif, else
* Comparison operators
* Logical operators

---

## How to Run

1. Save the file as `fraud.py`
2. Open terminal
3. Run the program:

```
python fraud.py
```

4. Enter the required inputs when prompted

---

## Example

Input:

```
Amount: 80000
Location: Bangkok
Usual Location: Home City
Time: 2
Recent Transactions: 4
```

Output:

```
High amount detected  
Unusual location detected  
Odd time detected  
Too many transactions detected  

Risk Score: 7  
FRAUD  
```

---

## Purpose of Project

This project helps beginners understand:

* How real-world systems use rules to make decisions
* How logic building works in programming
* Basics of fraud detection systems
