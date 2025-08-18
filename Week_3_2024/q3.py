def load_items(filename):
    items = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                if "|" in line:
                    name, price = line.strip().split("|")
                    items[name] = int(price)
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
    return items


def vending_machine(filename="VendingItems.txt"):
    items = load_items(filename)
    if not items:
        return

    available_items = list(items.keys())

    # Step 1: Take valid item input
    while True:
        item = input().strip()
        try:
            if item not in items:
                raise KeyError
            break
        except KeyError:
            print(f"Available Items are {available_items}.")
            print("Try Again.")

    price = items[item]

    # Step 2: Take valid money input
    while True:
        money = input().strip()
        try:
            money = int(money)
            break
        except ValueError:
            print(f"Bad Input {money}.")
            print("Try Again.")

    # Step 3: Check money vs price
    if money < price:
        print(f"Not enough money. {item} costs {price} Rs. Please try again.")
    elif money == price:
        print("Thank you for your purchase. Enjoy")
    else:
        change = money - price
        print("Thank you for your purchase. Enjoy")
        print(f"Do not forget to collect your change, {change} Rs.")


# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    vending_machine()
