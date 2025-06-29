https://roadmap.sh/projects/expense-tracker
Expense Tracker CLI - Python
Overview

A lightweight command-line expense tracker built with Python's native libraries. This tool helps you manage personal finances by tracking expenses without external dependencies.
Features

    Add expenses: Record expenses with description and amount

    List expenses: View all recorded expenses

    Update expenses: Modify existing entries

    Delete expenses: Remove expenses

    Financial summaries: View total expenses or filter by month

    Budget tracking: Set monthly budgets and get spending alerts

    Data export: Export expenses to CSV format

Installation

No installation required! Just ensure you have Python 3.13:

Usage

Run commands directly from your terminal:
Basic Operations


# Add an expense
python expense_tracker.py add --desc "Groceries" --amount 50 --category "Food"

# List all expenses
python expense_tracker.py list

# Update an expense
python expense_tracker.py update --id 1 --amount 55

# Delete an expense
python expense_tracker.py delete --id 1

Budget Management

# Set monthly budget (month as number 01-12)
python expense_tracker.py set_budget --month 06 --amount 1000

# Will display alerts like:
# "You have reached 1.0% of your 06 month budget (1000)"

Data Analysis

# View summary
python expense_tracker.py summary

# Filter by month (numeric)
python expense_tracker.py summary --month 06

# Export to CSV
python expense_tracker.py save --name expenses.csv

Technical Details

    Data Storage: Uses local JSON files (expenses.json, budgets.json)

    Dependencies: Only Python native libraries:

        argparse for command handling

        csv for data export

        time for timestamping

        os for file operations

Notes

    Dates are automatically generated (user cannot input custom dates)

    Month parameters always use numeric format (01-12)

    No external packages required

Example Workflow

    Set a June budget:


python expense_tracker.py set_budget --month 06 --amount 1000

    Add some expenses:

python expense_tracker.py add --desc "Rent" --amount 800
python expense_tracker.py add --desc "Food" --amount 200

    Check your status:

python expense_tracker.py summary --month 06
Output: "You have reached 100.0% of your 06 month budget (1000)"