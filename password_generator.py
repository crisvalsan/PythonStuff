import random
import string

message = """[Password generator]
Enter the desire length for password: """
passLength = int(input(message))
passwd = list(string.ascii_letters + string.digits + string.punctuation)
generatedPasswd = random.shuffle(passwd)
finalPasswd = []
for gen in range(passLength):
    finalPasswd.append(random.choice(passwd))

print("".join(finalPasswd))

#seguir con en forloop