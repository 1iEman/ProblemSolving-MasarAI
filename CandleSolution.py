
# Example input: 4 4 3 2 4 --> Output: 3
candles = list(map(int, input("Enter the candles: ").split()))

highest_ = candles[0]
for i in range(len(candles)):
    if (candles[i] > highest_):
        highest_ = candles[i]

counter = 0
for i in range(len(candles)):
    if candles[i] == highest_:
        counter += 1
print(counter)


