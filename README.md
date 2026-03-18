# Smart-Transaction-Risk-Detector
A system to analyze transactions and generate risk report : Day-6 Challenge of Python

## Description 
This project is a python based application designed to create a system to analyze the transactions and generate a risk report.The program takes the number of transactions. Then, it stores the transactions in a list and classifies them as invalid, normal, large and high risk based on its value. These categories transactions are stored in a dictionary. It also identifies the frequent transactions, large spending and suspicious activity to determine whether the risk level is low, moderate or high.

## Objectives
 - To analyze transaction data efficiently
 - To classify transactions based on predefined rules
 - To detect suspicious spending patterns
 - To determine the overall risk level of a user

## Features
- Accepts multiple transaction inputs
- Classifies transactions into :
  - Normal
  - Large
  - High Risk
  - Invalid
- Detects patterns such as:
  - Frequent transactions
  - Large spending
  - Suspicious activity

= Provides final risk classification:
  - Low Risk
  - Moderate Risk
  - High Risk

- Displays a personalized suggestion based on spending

## Algorithm (Steps)

1. Start the program 
2. The number of transactions and transaction amount are taken as input.
3. The transaction amounts are stored in the form of list. 
4. Initialising the lists for normal, large , high risk and invalid transactions.
5. Use a loop to check each transaction.
6. Uses the conditional statements to classify the transaction based on its value.
7. All the categorised transaction are stored in a dictionary.
8. List comprehension is used to get the valid transactions.
9. The total transactions and total amount is calculated using tuple.
10. Some of the patterns are checked like frequent transaction, large spending and suspicious activity using conditional statements.
11. Risk score is calculated based on these conditions and categories them as low, moderate and high risks.
12. Categorised transactions, total number of transactions, total amount and risks have been displayed. 
13. Stop the program.

## Concepts Used

- Lists
- Loops (for)
- Conditional Statements
- List Comprehension
- Dictionary
- Tuple

## Pattern Detection Rules

- Frequent Transactions → More than 5 transactions
- Large Spending → Total amount > 5000
- Suspicious Pattern → 3 or more high-risk transactions

## Personalization Feature
The program provides customized feedback based on the user’s transaction behavior. If invalid transactions are detected, it alerts the user about incorrect inputs. It also gives suggestions based on total spending: low spending indicates good control, moderate spending suggests monitoring expenses, and high spending warns the user to be cautious. This makes the program more interactive and informative.

## Learning Outcomes 
This project helped in understanding important Python concepts like list comprehension, dictionaries, and tuples, along with improving logical thinking and problem-solving skills. It also provided experience in analyzing data, detecting patterns, and designing structured solutions for real-world scenarios.

## Reflection 
A key logic decision in this project was using a risk score system to determine the final classification. This approach makes the program flexible and easy to extend with additional rules in the future.
