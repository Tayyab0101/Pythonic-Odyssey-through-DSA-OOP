art = """
  .       ..-. 
   \     /(   )
    \   /  `-. 
     \ /  (   )
      '    `-'  """

game_logo = '''                                
  |   ||,---.|   |,---.,---.
  |---|||  _.|---||--- |---'
  |   |||   ||   ||    |  \_ 
  `   '``---'`   '`---'`   `-
  |    ,---.. . .,---.,---. 
  |    |   || | ||--- |---' 
  |    |   || | ||    |  \_  
  `---'`---'`-'-'`---'`   `-   '''
  
data = [
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 215,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 183,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 250,
        'description': 'Actor and former wrestler',
        'country': 'United States'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 211,
        'description': 'Singer and actress',
        'country': 'United States'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 230,
        'description': 'Footballer',
        'country': 'Argentina'
    }]

#start code
import os
import random

print(game_logo)

score = 0
# def accoun info
def account_info(account):
    a_name = account["name"]
    a_description = account["description"]
    a_country = account["country"]
    return (f"{a_name}, {a_description}, from {a_country}")
#picking info
account1 = random.choice(data)
account2 = random.choice(data)
continue_flag = True
while continue_flag:
    account1 = account2
    account2 = random.choice(data)
    while account1 == account2:
        account2 = random.choice(data)
    def check_answer(guess, follower1, follower2):
        if follower1>follower2:
            if guess == 1:
                return True
            else:
                return False
        else:
            if guess == 1:
                return False
            else:
                return True

    #dislpay
    print(f"compare1: {account_info(account1)}")
    print(art)
    print(f"compare2: {account_info(account2)}")

    guess = int(input("\n Who is having more followers Type 1 or 2?  "))
    follower1 = account1["follower_count"]
    follower2 = account2["follower_count"]
    os.system("cls")
    print(game_logo)
    is_correct = check_answer(guess, follower1, follower2)
    if is_correct == True:
        score +=1
        print(f"You are right. Ypur score is {score}")
    else:
        print(f"You are wrong. Your final score is {score}")
        continue_flag = False