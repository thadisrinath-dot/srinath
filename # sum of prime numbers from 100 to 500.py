# sum of prime numbers from 100 to 500
total = 0 # to store sum

for num in  range(100, 501): # numbers from 100 to 500
    if num > 1:
        is_prime = True
        for i in range( 2,int(num ** 0.5) + 1): # checkprime
            if num % i == 0:
                is_prime = False
                break
            if is_prime:
                total += num

            print("sum of prime numbers between 100 and 500 is:", total)