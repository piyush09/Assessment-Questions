def CountFrequency(votes):
    freq = {}
    for item in votes:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1

    for key, value in freq.items():
        print (key, value)

    max_freq_name = []
    for key, value in freq.items():
        if value == max(freq.values()):
            max_freq_name.append(key)

    max_freq_name.sort()
    print (max_freq_name[-1])

# votes = ["victor", "veronica", "ryan", "dave", "maria", "farah", "farah", "ryan", "veronica"]
# votes = ["Alex", "Michael", "Harry", "Dave", "Michael", "Victor", "Harry", "Alex", "Mary", "Mary"]
# votes = ["john", "johnny", "jackie", "johnny", "john", "jackie", "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]
# votes = ["Vamsi", "Krishna", "Vamsi", "Krishna", "Tallapudi"]
votes = ["Joe", "Mary", "Mary", "Joe"]
CountFrequency(votes)