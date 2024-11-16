import sys
import requests
# Get the value from command-line
if len(sys.argv) == 2:
    try:
       value = float(sys.argv[1])
    except:
        print("Command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)
# Get current price of Bitcoin as a float and print with the value given on the command-line as amount with four decimal places with a thousands seperator.
import requests

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response["bpi"]["USD"]["rate_float"]
    amount = bitcoin * value
    print(f"${amount:,.4f}")
except requests.RequestException:
    print("There was an ambiguous exception that occurred while handling your request.")
    sys.exit(1)
