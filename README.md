Expense Tracker CLI
    A Python program that tracks and analyzes expenses from a CSV file using Pandas and NumPy.

How to Run

    Ensure Python 3.8+ is installed.

    Install dependencies:

        bash
        pip install pandas numpy matplotlib or pip install -r reuirements.txt

    Place your expenses.csv in the same folder.

    Run:

        bash
        python expense_tracker.py


Sample Input (expenses.csv)

    csv
    Date,Category,Amount,Description
    2025-06-10,Food,150,Pizza at Dominos
    2025-06-11,Transport,50,Rickshaw fare
    2025-06-12,Rent,5000,June Rent
    2025-06-12,Utilities,200,Electricity Bill


    Sample Output
    1. Total Spending Overview
    text
    Total Amount Spent: $5400.00  
    Highest Expense: $5000.00 (Rent)  
    Lowest Expense: $50.00 (Transport)  


    2. Category-wise Analysis
    text
    Category    Total     Count   Percentage  
    ----------------------------------------  
    Rent        $5000.00   1       92.59%  
    Utilities   $200.00    1       3.70%  
    Food        $150.00    1       2.78%  
    Transport   $50.00     1       0.93%  


    3. Pie Chart (Bonus)
    https://pie_chart.png

Features Implemented
    ✅ Total Spending Overview

    Calculates total, highest, and lowest expenses.

    ✅ Category-wise Analysis

    Sum, transaction count, and percentage per category.

    ✅ Data Visualization (Bonus)

    Generates a pie chart of expenses.

    ✅ CSV Integration

    Reads from/writes to expenses.csv.
