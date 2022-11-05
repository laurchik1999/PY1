import string
from random import sample

def get_random_password(n=8) -> str:
    if n<=0:
        raise ValueError("Длина пароля должна быть больше нуля")
    all_ = string.ascii_lowercase + string.ascii_uppercase + string.digits
    password = ''.join(sample(all_, n))
    return password



print(get_random_password())
print(get_random_password(15))
