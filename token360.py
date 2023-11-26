import requests

# Define the API endpoint URL and transaction hash
url = "https://api.etherscan.io/api"
tx_hash = "0x4611586f56eff1a577e89ac395376542176fdca6dae395131a7973974181ca15"

# Define the API parameters
params = {
    "module": "proxy",
    "action": "eth_getTransactionReceipt",
    "txhash": tx_hash,
    "apikey": "5DGXBPP52NZ5N9H11WF32JVRZ9MWJVSZ6N"
}

response = requests.get(url, params=params).json()
am = response.get("result")
amm=am['logs']
for name in amm:
 ay=name['data']
 decoded = int(ay, 16)
 decoded=decoded/1000000
 print(decoded)