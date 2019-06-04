import program_customers
import program_hosts


def main():
    try:
        while True:
            if user_input() == 'Customer':
                program_customers.run()
            else:
                program_hosts.run()
    except KeyboardInterrupt:
        return


def user_input():
    print('Press the letter in [ ] to indicate your selection')
    print()
    selection = input('Press [c] if you are a customer OR Press [o] if you are the owner/user.')
    if selection == 'c':
        return 'Customer'
    else:
        return 'Owner/user'


if __name__ == '__main__':
    main()