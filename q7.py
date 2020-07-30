primes = [2]


def find_prime(lim):
    while len(primes) < lim+1:
        for i in range(50):
            for x in range(2, round(i/2)+1):
                if i % x == 0:
                    break
                else:
                    primes.append(i)
    else:
        print(list(set(primes)))


find_prime(10)
