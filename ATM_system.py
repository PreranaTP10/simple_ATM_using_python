balance=10000
print('...Welcome to ATM...')
while True:
    print('\n'
          '1.Balance\n'
          '2.Withdraw\n'
          '3.Deposit\n'
          '4.Quit\n')
    Option=int(input( 'Please select Option: '))
    if Option==1:
        print('Balance : ',balance)

    elif Option==2:
        print('Balance : ',balance)
        withdraw=float(input('Enter amount to withdraw: '))
        if withdraw>0:
            balance-=withdraw
            print('Withdrawal Successful. Your A/c Balance is : ',balance)

        elif withdraw>balance:
            print('No funds in account .')
        else:
            print('Please enter valid amount.')

    elif Option==3:
        Deposit=float(input('Enter amount to deposit : '))
        if Deposit>0:
            balance+=Deposit
            print('Deposit successful. Your A/c balance is : ',balance)
        else:
            print('No Deposit Made.')
    elif Option==4:
        print('Thank you for visiting...')
        break
    else:
        print('Invalid Input...')

