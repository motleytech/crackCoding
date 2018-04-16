
# of 2s in ones position = n / 10 + (1 if n % 10 > 1 else 0)
# of 2s in 10s position = 10 * (n / 100) + (10 if (n % 100) / 10 > 2 else 0) + (n % 10 + 1 if (n % 100) / 10 == 2 else 0)
# of 2s in 100s position = 100 * (n / 1000) + (100 if (n % 1000) / 100 > 2 else 0) + (n % 100 + 1 if (n % 1000) / 100 == 2 else 0)



def count2Brute(num):
    count = 0
    for x in range(num + 1):
        count += str(x).count('2')

    return count

def count2s(num):
    pos = 0
    count = 0
    p1, p2 = 1, 10
    while num > pow(10, pos):
        p1, p2 = pow(10, pos), pow(10, pos+1)
        count += pow(10, pos) * (num / pow(10, pos+1)) + (pow(10, pos) if (num % pow))

