import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Constants
CSV_FILE = "expenses.csv"

def load_data():
    """Load and validate expense data"""
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        # Validate critical columns
        if not all(col in df.columns for col in ['Date', 'Category', 'Amount', 'Description']):
            raise ValueError("CSV missing required columns")
        # Clean data
        df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
        df = df.dropna(subset=['Amount'])
        return df
    return pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Description'])

def save_data(df):
    """Save data with validation"""
    df.to_csv(CSV_FILE, index=False)

def add_expense(df):
    """Add expense with input validation"""
    print("\n➕ Add New Expense")
    date = input("Date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format!")
        return df
    
    category = input("Category: ").strip().capitalize()
    description = input("Description: ").strip()
    
    try:
        amount = round(float(input("Amount: ")), 2)
    except ValueError:
        print("Invalid amount!")
        return df

    new_row = {'Date': date, 'Category': category, 
               'Amount': amount, 'Description': description}
    return pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

def calculate_stats(df):
    """NumPy-powered statistics calculation"""
    amounts = df['Amount'].to_numpy()
    return {
        'total': np.sum(amounts),
        'max': {'Amount': np.max(amounts), 
                'Details': df.loc[df['Amount'].idxmax()].to_dict()},
        'min': {'Amount': np.min(amounts),
                'Details': df.loc[df['Amount'].idxmin()].to_dict()}
    }

def category_analysis(df):
    """Complete category analysis as specified"""
    if df.empty:
        return None
    
    # NumPy calculations
    categories = df['Category'].unique()
    total_spent = np.sum(df['Amount'].to_numpy())
    
    results = []
    for cat in categories:
        cat_amounts = df[df['Category'] == cat]['Amount'].to_numpy()
        results.append({
            'Category': cat,
            'Total': np.sum(cat_amounts),
            'Count': len(cat_amounts),
            'Percentage': round(np.sum(cat_amounts) / total_spent * 100, 2)
        })
    
    # Sort by highest total
    return sorted(results, key=lambda x: x['Total'], reverse=True)

def show_analysis(df):
    """Display perfect output formatting"""
    if df.empty:
        print("No expenses to analyze!")
        return
    
    # 1. Total Spending Overview
    stats = calculate_stats(df)
    print("\n💵 TOTAL SPENDING OVERVIEW")
    print("="*50)
    print(f"• Total Amount Spent: ${stats['total']:.2f}")
    print(f"• Highest Expense: ${stats['max']['Amount']:.2f} ({stats['max']['Details']['Category']} - {stats['max']['Details']['Description']})")
    print(f"• Lowest Expense: ${stats['min']['Amount']:.2f} ({stats['min']['Details']['Category']} - {stats['min']['Details']['Description']})")
    
    # 2. Category-wise Analysis
    print("\n📊 CATEGORY-WISE ANALYSIS")
    print("="*50)
    print(f"{'Category':<15} {'Total':>12} {'Count':>8} {'%':>10}")
    print("-"*50)
    
    categories = category_analysis(df)
    for cat in categories:
        print(f"{cat['Category']:<15} ${cat['Total']:>11.2f} {cat['Count']:>8} {cat['Percentage']:>9.2f}%")
    
    print("="*50)
    print(f"{'TOTAL':<15} ${stats['total']:>11.2f} {len(df):>8} {'100.00':>9}%")

def show_pie_chart(df):
    """Bonus: Perfect pie chart visualization"""
    if df.empty:
        print("No data to visualize!")
        return
    
    category_totals = df.groupby('Category')['Amount'].sum()
    plt.figure(figsize=(10, 7))
    plt.pie(category_totals, 
            labels=category_totals.index,
            autopct='%1.1f%%',
            startangle=140,
            explode=[0.05]*len(category_totals))
    plt.title('Expense Distribution by Category', pad=20)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

def main():
    """Perfect CLI interface"""
    df = load_data()
    
    while True:
        print("\n💰 EXPENSE TRACKER MENU")
        print("1. View All Expenses")
        print("2. Add New Expense")
        print("3. Run Full Analysis")
        print("4. Show Pie Chart (Bonus)")
        print("5. Exit")
        
        choice = input("Choose (1-5): ").strip()
        
        if choice == '1':
            print("\n📋 ALL EXPENSES")
            print(df.to_string(index=False) if not df.empty else "No expenses found")
        
        elif choice == '2':
            new_df = add_expense(df)
            if not new_df.equals(df):
                df = new_df
                save_data(df)
        
        elif choice == '3':
            show_analysis(df)
        
        elif choice == '4':
            show_pie_chart(df)
        
        elif choice == '5':
            print("Goodbye! Data saved." if not df.empty else "Goodbye!")
            break
        
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("EXPENSE TRACKER SYSTEM".center(50))
    print("="*50)
    main()