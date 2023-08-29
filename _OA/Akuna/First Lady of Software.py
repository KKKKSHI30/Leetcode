def findNumberOfWays(n_intervals, n_processes):
    mod = int(1e9) + 7

    if n_processes == 1 and n_intervals == 1:
        return 1
    elif n_intervals == 1:
        return 0
    else:
        result = (n_processes * pow(n_processes - 1, n_intervals - 1)) % mod
        return result

n_intervals = 3
n_processes = 2
