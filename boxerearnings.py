#Here's an example of a Python program that calculates 
#a boxer's earnings by maximizing the total amount earned, 
#with the constraint that there can be no contiguous matches:
def calculate_max_earnings(matches):
    n = len(matches)
    if n == 0:
        return 0

    earnings = [0] * n
    earnings[0] = matches[0]

    for i in range(1, n):
        earnings[i] = max(matches[i], earnings[i-1])
        if i > 1:
            earnings[i] = max(earnings[i], earnings[i-2] + matches[i])

    return earnings[-1]

# Example usage:
matches = [100, 50, 200, 80, 120]
max_earnings = calculate_max_earnings(matches)
print("Maximum earnings:", max_earnings)
