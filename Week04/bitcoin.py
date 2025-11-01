import requests
import sys
#import json

try:
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    buy = float(sys.argv[1])
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=aff1b20be6f5cb3046ccd5a9ce2c7be077646895e83f1a87b3c56b1b6fd60d88").json()
    btc_data = response["data"]
    price = float(btc_data["priceUsd"])
    amount = buy*price
    print(f"${amount:,.4f}")
except ValueError:
    sys.exit("Command-line argument is not a number")
except requests.RequestException:
    sys.exit("RequestException")
