logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
from reprlib import clear

bids = {}
biding_finished = False


def find_heghtest_bidder(bidding_record):
    height_bid = 0
    winner = ""
    for bidder in bidding_record:
        bidder_amount = bidding_record[bidder]
        if bidder_amount > height_bid:
            height_bid = bidder_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${height_bid}")


while biding_finished:
    name = input("What is your name?")
    price = input("What is your bid?$")
    bids[name] = price
    should_continue = input("Are there any other bidders?Type 'yes' or 'no'")
    if should_continue == 'no':
        biding_finished = True
        find_heghtest_bidder(bids)
    elif should_continue == '':
        clear()
