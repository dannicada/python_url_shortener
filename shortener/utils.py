import random
import string

def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    # new_code = ''
    # for _ in range(size):
    #     new_code += random.choice(chars)
    # return new_code


    return ''.join(random.choice(chars) for _ in range(size))

