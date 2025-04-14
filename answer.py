
# Example input: 4 4 3 2 4 --> Output: 3


candles = list(map(int, input("Enter the candles: ").split()))


longest = max(candles)

counter = 0
for i in range(len(candles)):
    if candles[i] == longest:
        counter += 1
print(counter)

