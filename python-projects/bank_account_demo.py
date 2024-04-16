from bank_account import BankAccount

account1 = BankAccount(1234567)
account2 = BankAccount(1234513, 345.00)

print(account1)
print(account2)

account1.deposit(40.00)
account2.withdraw(10.00)

print(account1)
print(account2)





