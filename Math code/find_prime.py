def find_primes(lower_bound, upper_bound):
	bool_arr = [True] * (upper_bound + 1)
	bool_arr[0] = False
	bool_arr[1] = False
	
	prime = 2
	while prime < len(bool_arr):
		for i in range(prime ** 2, len(bool_arr), prime):
			bool_arr[i] = False
		
		prime += 1
		while prime < len(bool_arr) and bool_arr[prime] == False:
			prime += 1
		
	primes = []
	for i in range(lower_bound, len(bool_arr)):
		if bool_arr[i] == True:
			primes.append(i)
	return primes
	
all_primes = find_primes(1, 1000)
print(len(all_primes))
print(all_primes)