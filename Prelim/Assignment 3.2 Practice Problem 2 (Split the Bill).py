# -*- coding: utf-8 -*-
"""Assignment 3.2 Practice Problem 2 (Split the Bill)

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NUItjKfm7Nqqo5ipUNfAs_q4bwPDRiB-

# **Assignment 3.2 Practice Problem 2 (Split the Bill)**

**Problem**


In the Splitwise app, people form groups and add the expenses of members of the group. This is especially useful for vacations, where people traveling in a group can maintain an account of their expenses and who paid the bills.

All people in the group are assigned distinct IDs between 1 and N, where N is the size of the group.

In addition to keeping a record of the expenditure, Splitwise also calculates the list of shortest-path transfers (defined later) that will settle up all dues.
"""

def compute_shortest_path_transfers(num_people, transactions):
    # Initialize balances dictionary to keep track of net amounts owed or owed by each person
    balances = {person_id: 0 for person_id in range(1, num_people + 1)}

    # Update balances based on transactions
    for transaction in transactions:
        # Parse transaction details
        paid_by = transaction['paid_by']
        split_as = transaction['split_as']

        # Update balances for amounts paid
        for payer_id, amount_paid in paid_by:
            balances[payer_id] -= amount_paid

        # Update balances for amounts borrowed
        for borrower_id, amount_borrowed in split_as:
            balances[borrower_id] += amount_borrowed

    # Separate people who owe money and people who are owed money
    borrowers = [(person_id, amount) for person_id, amount in balances.items() if amount > 0]
    lenders = [(person_id, -amount) for person_id, amount in balances.items() if amount < 0]

    # Sort both lists based on amounts owed or owed
    borrowers.sort(key=lambda x: (x[1], x[0]))  # Sort by amount owed and then by person ID
    lenders.sort(key=lambda x: (x[1], x[0]))    # Sort by amount lent and then by person ID

    # Initialize payments list
    payments = []

    # Iterate through borrowers and lenders, transferring money
    borrower_index, lender_index = 0, 0
    while borrower_index < len(borrowers) and lender_index < len(lenders):
        borrower_id, borrower_amount = borrowers[borrower_index]
        lender_id, lender_amount = lenders[lender_index]

        # Calculate transfer amount
        transfer_amount = min(borrower_amount, lender_amount)

        # Record payment and update balances
        payments.append([lender_id, borrower_id, transfer_amount])
        balances[borrower_id] -= transfer_amount
        balances[lender_id] += transfer_amount

        # Move to the next borrower or lender if their balance is settled
        if balances[borrower_id] == 0:
            borrower_index += 1
        if balances[lender_id] == 0:
            lender_index += 1

    return payments

# Sample Input
num_people = 4
transactions = [
    {"transaction_id": "#a1234", "paid_by": [[1, 60]], "split_as": [[2, 60]]},
    {"transaction_id": "#a2142", "paid_by": [[2, 40]], "split_as": [[3, 40]]},
    {"transaction_id": "#b3310", "paid_by": [[3, 30]], "split_as": [[4, 30]]},
    {"transaction_id": "#b2211", "paid_by": [[4, 30]], "split_as": [[3, 30]]},
    {"transaction_id": "#f1210", "paid_by": [[3, 20]], "split_as": [[1, 20]]}
]

# Compute shortest-path transfers
payments = compute_shortest_path_transfers(num_people, transactions)

# Print results
print(len(payments))
for payment in payments:
    print(*payment)