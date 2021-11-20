import random

def pwd_generator(): 
    """Generate random password with combination 3 alphabet, 2 number and 2 character """
    
    a="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    n="1234567890"
    c="""}{()[]"'~`!@#$%^&*_-+=|\\/:;<>,.?"""

    return "".join(random.sample(a,3)) + "".join(random.sample(n,2))+"".join(random.sample(c,2)) 