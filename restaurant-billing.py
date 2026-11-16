"""
Restaurant Billing System
PS No.: 31
Language: Python 3

Menu:
    Dosa  - Rs. 80
    Idli  - Rs. 40
    Thali - Rs. 150
    Tea   - Rs. 20

Rules:
    10% discount when subtotal is more than Rs. 500.
    GST is 5% of the amount after discount.
"""

MENU = {
    "dosa": 80,
    "idli": 40,
    "thali": 150,
    "tea": 20
}


def calculate_subtotal(order):
    """Return the sum of all item amounts."""
    return sum(item["amount"] for item in order)


def calculate_discount(subtotal):
    """Give 10% discount only when subtotal is greater than 500."""
    if subtotal > 500:
        return subtotal * 0.10
    return 0.0


def calculate_gst(amount_after_discount):
    """Calculate 5% GST on the discounted amount."""
    return amount_after_discount * 0.05


def print_menu():
    print("\n----------- RESTAURANT MENU -----------")
    for item, price in MENU.items():
        print(f"{item.title():<12} Rs. {price:.2f}")
    print("---------------------------------------")
    print("Type 'bill' to generate the bill.")


def add_order_item(order, item_name, quantity):
    """Validate and add an item to the order."""
    item_name = item_name.strip().lower()

    if item_name not in MENU:
        available = ", ".join(name.title() for name in MENU)
        print(f"Item not on the menu. Available: {available}")
        return False

    if not isinstance(quantity, int) or quantity < 1:
        print("Quantity must be at least 1.")
        return False

    amount = MENU[item_name] * quantity
    order.append({
        "name": item_name,
        "quantity": quantity,
        "price": MENU[item_name],
        "amount": amount
    })

    print(f"{item_name.title()} x{quantity} added | Amount: {amount:.0f}")
    return True


def generate_bill(order):
    """Print the complete formatted customer bill."""
    if not order:
        print("\nNo items ordered. Cannot generate a bill.")
        return

    subtotal = calculate_subtotal(order)
    discount = calculate_discount(subtotal)
    amount_after_discount = subtotal - discount
    gst = calculate_gst(amount_after_discount)
    grand_total = amount_after_discount + gst

    print("\n" + "=" * 48)
    print("                 RESTAURANT BILL")
    print("=" * 48)
    print(f"{'Item':<14}{'Qty':>5}{'Price':>12}{'Amount':>15}")
    print("-" * 48)

    for item in order:
        print(
            f"{item['name'].title():<14}"
            f"{item['quantity']:>5}"
            f"{item['price']:>12.2f}"
            f"{item['amount']:>15.2f}"
        )

    print("-" * 48)
    print(f"{'Subtotal:':<30}Rs. {subtotal:>12.2f}")
    print(f"{'Discount (10%):':<30}Rs. {discount:>12.2f}")
    print(f"{'GST (5%):':<30}Rs. {gst:>12.2f}")
    print("=" * 48)
    print(f"{'GRAND TOTAL:':<30}Rs. {grand_total:>12.2f}")
    print("=" * 48)
    print("              Thank you! Visit again.")
    print("=" * 48)


def main():
    """Run the restaurant billing application."""
    order = []

    print("WELCOME TO THE RESTAURANT BILLING SYSTEM")
    print_menu()

    while True:
        item_name = input("\nEnter order item (or 'bill'): ").strip()

        if item_name.lower() in ("bill", "generate bill", "done", "exit"):
            generate_bill(order)
            break

        if not item_name:
            print("Please enter an item name.")
            continue

        quantity_text = input("Enter quantity: ").strip()

        try:
            quantity = int(quantity_text)
        except ValueError:
            print("Invalid quantity. Enter a whole number.")
            continue

        add_order_item(order, item_name, quantity)


if __name__ == "__main__":
    main()