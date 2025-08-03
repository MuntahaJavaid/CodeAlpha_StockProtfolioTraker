stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 350
}
print("Stock Prices: \n AAPL: 180 \n TSLA: 250\n GOOGL: 2700\n AMZN: 3300\n MSFT: 350")
                                         # Get user input
portfolio = {}
while True:
    stock = input("Enter stock symbol (or type 'done' to finish): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        quantity = int(input(f"How many shares of {stock} do you own? "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    else:
        print("❌ Invalid stock symbol! Try again.")

                                        # Calculate total investment
total_value = 0
print("\n📊 Your Portfolio Summary:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock} - {qty} shares × ${price} = ${value}")

print(f"\n💼 Total Investment Value: ${total_value}")

                                        #Optionally save to file
save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Your Portfolio Summary:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock} - {qty} shares × ${price} = ${value}\n")
        f.write(f"\nTotal Investment Value: ${total_value}")
    print("📁 Saved to 'portfolio_summary.txt' ")
