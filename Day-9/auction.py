clear = '\n' * 50
bids = {}
new_user = True

while new_user:
    name = input("Enter your name: ")
    bids[name] = input("Enter your bid: $")
    q = input("Is there a new user? (Y/N)")
    if q == "N":
        new_user = False
        break
    print(clear)

highest_bid = 0


for person in bids:
    highest_bidder = bids[person]
    if int(highest_bidder) > int(highest_bid):
        highest_bid = bids[person]
        highest_person = person

print(f"The highest bid is {highest_bid} and it is by {highest_person}")
