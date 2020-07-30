
def find_n_primes(n):
    result = []
    curr = 2
    while len(result) < n:
        for i in range(2, int(curr/2)+1):
            if curr % i == 0: # Number is divisible
                break
        else:
            result.append(curr)
        curr += 1
    return result


def main():
    r = find_n_primes(20)
    print(r)


if __name__ == "__main__":
    main()
