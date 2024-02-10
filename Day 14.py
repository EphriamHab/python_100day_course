import random
data = [
    {
        'name': 'Cristiano Ronaldo',
        'country': 'Portugal',
        'occupation': 'Footballer',
        'followers': 422
    },
    {
        'name': 'Dwayne Johnson',
        'country': 'United States',
        'occupation': 'Actor',
        'followers': 270
    },
    {
        'name': 'Kylie Jenner',
        'country': 'United States',
        'occupation': 'Entrepreneur',
        'followers': 313
    },
    {
        'name': 'Selena Gomez',
        'country': 'United States',
        'occupation': 'Singer',
        'followers': 288
    },
    {
        'name': 'Leo Messi',
        'country': 'Argentina',
        'occupation': 'Footballer',
        'followers': 216
    }
]


def format_data(account):   
    account_name = account['name']
    account_desc = account['occupation']
    account_country = account['country']

    return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
       return guess =='a'
    else:
       return guess =='b'
        
        
score = 0 
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:      
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a['followers']
    b_follower_count = account_b['followers']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score +=1
        print(f"You're right! current score {score}.")
    else:
        game_should_continue = False
        print(f"Sorry that is wrong. Final score {score}")