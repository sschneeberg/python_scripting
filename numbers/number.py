with open('numbers/primes.txt', "r") as primes:
    primes_list = primes.readlines()
    for i in range(len(primes_list)):
        primes_list[i] = str(int(primes_list[i]) * 2)
    double_primes = open("number/double_primes.txt", "r+")
    double_primes.write("\n".join(primes_list))
    double_primes.close()



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
