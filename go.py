def xor(x, y):
    ans = ""
    for i in range(len(y)):
        if x[i] == y[i]:
            ans += '0'
        else:
            ans += '1'
    return ans

def divide(dividend, divisor):
    a = len(divisor)
    temp = dividend[0:a]
    while a < len(dividend):
        if temp[0] == '1':
            temp = xor(divisor, temp) + dividend[a]
        else:
            temp = xor('0' * a, temp) + dividend[a]
        a += 1
    if temp[0] == '1':
        temp = xor(divisor, temp)
    else:
        temp = xor('0' * a, temp)
    return temp

# Predefined generator polynomials
keys = ['1100000001111', '11000000000000101', '10001000000100001']

print("Choose the CRC")
print("1. CRC - 12")
print("2. CRC - 16")
print("3. CRC - CCITT")

n = int(input("Enter your choice (1/2/3): "))

send = input("Enter the string of binary data bits to be sent from the sender: ")
rec = input("Enter the string of binary data received at the receiver side: ")

# Select the appropriate key
key = keys[n - 1]

# Encoding on sender's side
length = len(key)
send1 = send + '0' * (length - 1)
rem = divide(send1, key)

# Decoding on receiver's side
ans = divide(rec, key)

# Check for transmission errors
if ans == '0' * (len(key) - 1):
    print("No error in transmission")
else:
    print("Frame error detected")
