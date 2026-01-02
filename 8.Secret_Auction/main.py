import auction
print(auction.auction_hammer)

auction_data={}

continue_bid=True

while continue_bid:
    name=input("what's your name ?")
    bid=input("what's your bid ?")
    bid=int(bid.replace("$",''))

    auction_data[name]=bid

    print(auction_data)
    
    print("\n"*1000)
    add_bidders=input("are there any more bidders. yes or no \n").lower()

    if add_bidders=="no":
        continue_bid=False

max_bid=0
for i in auction_data:
    if auction_data[i]>max_bid:
        max_bid=auction_data[i]
print(f"highest bid is {max_bid} by {i}")
