import json
import sys
from collections import defaultdict

def load_orders(file_path):
    """Load order data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def extract_customer_info(orders):
    """Extract customer phone numbers and names."""
    customers = {}
    for order in orders:
        phone = order.get('phone')
        name = order.get('name')
        if phone and name:
            customers[phone] = name
    return customers

def extract_item_info(orders):
    """Aggregate menu items, their prices, and order counts."""
    item_data = defaultdict(lambda: {'price': 0, 'count': 0})
    for order in orders:
        for item in order.get('items', []):
            item_name = item['name']
            item_price = item['price']
            # Set price only if it's not already set
            if item_data[item_name]['price'] == 0:
                item_data[item_name]['price'] = item_price
            item_data[item_name]['count'] += 1
    return item_data

def save_to_json(file_name, data):
    """Save a dictionary to a JSON file."""
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def main(input_file):
    """Main function to process orders and create output files."""
    try:
        orders = load_orders(input_file)
        customer_info = extract_customer_info(orders)
        item_info = extract_item_info(orders)

        save_to_json('customers.json', customer_info)
        save_to_json('items.json', item_info)
        print("Data has been processed and saved successfully.")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading the file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_orders_json>")
        sys.exit(1)
    
    main(sys.argv[1])
