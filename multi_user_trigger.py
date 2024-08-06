import random
import string

def generate_random_strings(num_strings, string_length):
    random_strings = []
    for _ in range(num_strings):
        random_string = ''.join(random.choices(string.ascii_letters, k=string_length))
        random_strings.append(random_string)
    return random_strings

# Generate 10 random strings, each of 3 characters
random_strings = generate_random_strings(10, 3)
print(random_strings)
