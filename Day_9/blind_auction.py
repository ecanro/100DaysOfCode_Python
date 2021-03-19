from arts_pro import logo9

print(logo9)
bidders = []


def firts_bidder():
    name = input('What is your name?: ')
    bid = input('What is your bid?: $')

    bidder_dictionary = {}
    bidder_dictionary['name'] = name
    bidder_dictionary['bid'] = bid
    bidders.append(bidder_dictionary)


add_new = input("Are there any other bidders? Type 'yes or 'no'.")
if add_new == 'yes':
    firts_bidder()
else:
    for bid in bidders:
        if bidders[bid]:
            print('bidder_dictionary[bid]')

firts_bidder()
bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()