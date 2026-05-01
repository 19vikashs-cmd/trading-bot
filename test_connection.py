from bot.client import get_client

client = get_client()

try:
    balance = client.futures_account_balance()
    print("Connection successful")
    print(balance)

except Exception as e:
    print("Connection failed")
    print(str(e))