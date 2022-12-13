import sys
import random


class BillSplitter:
    n_friends = 0

    def __init__(self):
        self.all_friends = dict()
        self.is_lucky = None
        self.bill = 0

    def get_n_of_friends(self):
        print('Enter the number of friends joining (including you):')
        return int(input())

    def get_final_bill(self):
        print('Enter the total bill value:')
        self.bill = int(input())

    def get_lucky_question(self):
        print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
        self.is_lucky = input()
        if self.is_lucky == 'No':
            print('No one is going to be lucky\n')
            self.split_bill()
        else:
            self.get_lucky_name()

    def get_friends(self):
        BillSplitter.n_friends = self.get_n_of_friends()
        self.no_friends()
        print('Enter the name of every friend (including you), each on a new line:')
        self.all_friends = {input(): 0 for _ in range(BillSplitter.n_friends)}

    def no_friends(self):
        if BillSplitter.n_friends < 1:
            print('No one is joining for the party')
            sys.exit()

    def get_lucky_name(self):
        name = random.choice(list(self.all_friends.keys()))
        print('{} is the lucky one!\n'.format(name))
        BillSplitter.n_friends -= 1
        del self.all_friends[name]
        self.split_bill()
        self.all_friends[name] = 0

    def split_bill(self):
        remainder = self.bill % BillSplitter.n_friends
        share = self.bill / BillSplitter.n_friends
        if remainder == 0:
            for i in self.all_friends.keys():
                self.all_friends[i] = int(share)
        else:
            for i in self.all_friends.keys():
                self.all_friends[i] = round(share, 2)

    def start(self):
        self.get_friends()
        self.get_final_bill()
        self.get_lucky_question()
        print(self.all_friends)