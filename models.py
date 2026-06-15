'''4 classes:
Food item -> price, category and popularity
item list -> list of food items
Transaction -> selected items, total cost of the transaction
Customer -> names, purchase history
'''


class FoodItem:
    def __init__(self, name, price, category, popularity):
        self.name = name
        self.price = price
        self.category = category
        self.popularity = popularity
    
    def get_price(self):
        return self.price
    
    def get_category(self):
        return self.category
    
    def get_popularity(self):
        return self.popularity


class ItemList:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
    
    def get_items(self):
        return self.items
    
    def filter_by_category(self, category):
        return [item for item in self.items if item.get_category() == category]
    
    def get_all_categories(self):
        categories = set()
        for item in self.items:
            categories.add(item.get_category())
        return list(categories)


class Transaction:
    def __init__(self):
        self.selected_items = []
        self.total_cost = 0.0
    
    def add_item(self, item):
        self.selected_items.append(item)
        self.calculate_total()
    
    def remove_item(self, item):
        if item in self.selected_items:
            self.selected_items.remove(item)
            self.calculate_total()
    
    def calculate_total(self):
        self.total_cost = sum(item.get_price() for item in self.selected_items)
        return self.total_cost
    
    def get_items(self):
        return self.selected_items


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchase_history = []
    
    def get_name(self):
        return self.name
    
    def add_purchase(self, transaction):
        self.purchase_history.append(transaction)
    
    def get_purchase_history(self):
        return self.purchase_history
    
    def is_valid_customer(self):
        return len(self.purchase_history) > 0


# Demo Script
if __name__ == "__main__":
    print("=== ByteBites System Demo ===\n")
    
    # Create FoodItems
    print("1. Creating food items...")
    burger = FoodItem("Spicy Burger", 8.99, "Burgers", 4.8)
    soda = FoodItem("Large Soda", 2.99, "Drinks", 4.5)
    fries = FoodItem("Crispy Fries", 3.49, "Sides", 4.7)
    ice_cream = FoodItem("Vanilla Ice Cream", 4.99, "Desserts", 4.9)
    lemonade = FoodItem("Fresh Lemonade", 3.50, "Drinks", 4.6)
    print(f"   Created: {burger.name}, {soda.name}, {fries.name}, {ice_cream.name}, {lemonade.name}\n")
    
    # Build ItemList and add items
    print("2. Building menu (ItemList)...")
    menu = ItemList()
    menu.add_item(burger)
    menu.add_item(soda)
    menu.add_item(fries)
    menu.add_item(ice_cream)
    menu.add_item(lemonade)
    print(f"   Added {len(menu.get_items())} items to menu\n")
    
    # Show all categories
    print("3. Available categories:")
    categories = menu.get_all_categories()
    for category in sorted(categories):
        print(f"   - {category}")
    print()
    
    # Filter by category
    print("4. Filtering by category (Drinks):")
    drinks = menu.filter_by_category("Drinks")
    for item in drinks:
        print(f"   - {item.name}: ${item.get_price()} (popularity: {item.get_popularity()})")
    print()
    
    # Sort menu by popularity
    print("5. Menu sorted by popularity (highest first):")
    sorted_menu = sorted(menu.get_items(), key=lambda item: item.get_popularity(), reverse=True)
    for item in sorted_menu:
        print(f"   - {item.name}: ${item.get_price()} (popularity: {item.get_popularity()})")
    print()
    
    # Create a transaction and add items
    print("6. Creating a customer order (Transaction)...")
    order = Transaction()
    order.add_item(burger)
    order.add_item(fries)
    order.add_item(soda)
    print(f"   Items in order:")
    for item in order.get_items():
        print(f"     - {item.name}: ${item.get_price()}")
    print(f"   Order total: ${order.calculate_total():.2f}\n")
    
    # Create customer and record purchase
    print("7. Recording customer purchase...")
    customer = Customer("Alice")
    customer.add_purchase(order)
    print(f"   Customer: {customer.get_name()}")
    print(f"   Valid customer: {customer.is_valid_customer()}")
    print(f"   Total purchases: {len(customer.get_purchase_history())}")
    print(f"   Last order total: ${customer.get_purchase_history()[0].total_cost:.2f}")