from web3 import Web3


input_str = '0x0000000000000000000000000000000000000000000000000000000008f0d180'

decoded = int(input_str, 16)
decoded=decoded/1000000

print(decoded) # Output: 150000000000