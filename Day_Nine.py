student_scores = {
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] ="Outstanding"
    elif score > 80:
        student_grades[student] ="Exceeds Expectation"
    elif score > 70:
        student_grades[student] ="Acceptable"
    else:
        student_grades[student] ="Fail"

# Nesting
capitals = {
     "France":"Paris",
     "Germany":"Berlin",
 }

# Nesting a List in a Dictionary

travel_log =[
    {
        "coutry":"France",
        "visits":12,
        "cities":["paris","Lille","Dijon"]
    },
    {
        "country":"Germany",
        "visits":5,
        "cities":["Berlin","Hamburg","Stuttgart"]
    },
]

def add_new_country(country, visits, cities):
      new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
      travel_log.append(new_country)



add_new_country("Russia",2,["Moscow","Saint Petrsbu"])

print(travel_log)


bids = {}
bidding_finished = False

def find_highest_bidder(bids):
   higest_bid =0
   winner =""
   for bidder in bids:
       bid_amount = bids[bidder]
       if bid_amount > higest_bid:
           higest_bid =bid_amount
           winner = bidder
   print(f"The winner is {winner} with a bid of ${higest_bid}")
while not bidding_finished:
    name = input("what is your name?: ")
    price = int(input("what is your bid?: $"))
    bids[name] = price
    shoulde_continue = input("Are there other biders? Type 'yes' or 'no'")
    if shoulde_continue =="no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif shoulde_continue =="yes":
       bidding_finished = False
        