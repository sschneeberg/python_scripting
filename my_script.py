#Write with "filename", "w" and .write() will overwrite a file or create one
hello_file = open("hello.txt", "w") 
hello_file.write("Goodbye")
hello_file.close()

# don't have to call close with this syntax:
with open("person.txt", "w") as person_file:
    person_file.write("Simone")

#append to a file with "a"
with open("person.txt", "a") as person_file:
    person_file.write("\nSimone")

# strange things are happening here:
# with open("person.txt", "r+") as person_file:
#     print(person_file.read())
#     person_file.write("\nSimone")
#     print(person_file.read())
#     person_file.close()
#     person_file = open("person.txt")

with open('numbers/primes.txt', "r") as primes:
    primes_list = primes.readlines()
    for i in range(len(primes_list)):
        primes_list[i] = str(int(primes_list[i]) * 2)
    double_primes = open("numbers/double_primes.txt", "r+")
    double_primes.write("\n".join(primes_list))
    double_primes.close()


with open("numbers/fives.txt", "r") as fives:
    fives_list = fives.readlines()
    fives_collect = []
    for line in fives_list:
        if "five" in line.lower() or "fift" in line.lower():
            fives_collect.append(line)
    contains_five =  open("numbers/contains_five.txt", "w")
    contains_five.write("".join(fives_collect))
    contains_five.close()
