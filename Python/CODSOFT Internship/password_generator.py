print("Welcome to password genratoe.")
import string
import random
alphabets = int(input(f"Enet no of alphabets: "))
numbers = int(input(f"Enter no of numbers : "))
special = int(input(f"Enter spec chars: "))

alphs = string.ascii_letters
numbs = string.digits
spec = "!@#$%^&*()_+-=[]{}|;:',.<>/?"

password = ''

password += ''. join(random.choice(alphs) for any in range(1, alphabets+1))
password += ''.join(random.choice(numbs) for no in range(1, numbers+1))
password += ''.join(random.choice(spec) for spe in range (1, special+1))

pass_list = list(password)
random.shuffle(pass_list)

final_password = ''.join(pass_list)
print(final_password)
