import argparse
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.orders import (
    place_market_order,
    place_limit_order
)


def main():
    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading symbol (e.g. BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        help="Order quantity"
    )

    parser.add_argument(
        "--price",
        required=False,
        help="Price (required for LIMIT)"
    )

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\nOrder Request Summary")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price:
            print(f"Price: {price}")

        if order_type == "MARKET":
            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:
            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\nOrder Response")
        print(response)

        print(f"Order ID: {response.get('orderId', 'N/A')}")
        print(f"Status: {response.get('status', 'N/A')}")
        print(f"Executed Quantity: {response.get('executedQty', 'N/A')}")
        print(f"Average Price: {response.get('avgPrice', 'N/A')}")

    except Exception as e:
        print(f"\nOrder failed: {str(e)}")


if __name__ == "__main__":
    main()