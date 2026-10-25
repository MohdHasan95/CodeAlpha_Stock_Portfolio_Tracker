
# CodeAlpha Python Internship
# Task 1: Stock Portfolio Tracker

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = []
total_investment = 0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(stock, "- $", price)

while True:
    stock_name = input(
        "\nEnter stock name (or DONE to finish): "
    ).upper().strip()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock! Please try again.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

    except ValueError:
        print("Please enter a valid number.")
        continue

    price = stock_prices[stock_name]
    investment = price * quantity

    portfolio.append((stock_name, quantity, price, investment))
    total_investment += investment

    print("Stock added successfully!")
    print("Investment: $", investment)

print("\n" + "=" * 45)
print("          PORTFOLIO SUMMARY")
print("=" * 45)

if not portfolio:
    print("No stocks added.")
else:
    print(f"{'Stock':<10}{'Qty':<8}{'Price':<10}{'Total':<10}")
    print("-" * 45)

    for stock, qty, price, investment in portfolio:
        print(f"{stock:<10}{qty:<8}{price:<10}{investment:<10}")

    print("-" * 45)
    print(f"Total Investment: ${total_investment:.2f}")

    save = input("\nSave portfolio? (yes/no): ").lower().strip()

    if save == "yes":
        print("\n1. Save as TXT")
        print("2. Save as CSV")

        choice = input("Enter choice (1/2): ")

        if choice == "1":
            with open("portfolio.txt", "w") as file:
                file.write("STOCK PORTFOLIO SUMMARY\n")
                file.write("-" * 40 + "\n")

                for stock, qty, price, investment in portfolio:
                    file.write(
                        f"{stock} | Qty: {qty} | "
                        f"Price: ${price} | Total: ${investment}\n"
                    )

                file.write(
                    f"\nTotal Investment: ${total_investment:.2f}"
                )

            print("Portfolio saved as portfolio.txt")

        elif choice == "2":
            import csv

            with open("portfolio.csv", "w", newline="") as file:
                writer = csv.writer(file)

                writer.writerow(
                    ["Stock", "Quantity", "Price", "Investment"]
                )

                for item in portfolio:
                    writer.writerow(item)

                writer.writerow(
                    ["", "", "Total", total_investment]
                )

            print("Portfolio saved as portfolio.csv")

        else:
            print("Invalid choice. File not saved.")

print("\nThank you for using Stock Portfolio Tracker!")
print("Developed for CodeAlpha Python Internship")
