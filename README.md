# Dosa Restaurant Order Analysis

## Overview

This project aims to enhance the order management system of a new Dosa restaurant by analyzing order data over the past year. The goal is to create structured JSON files that provide insights into customers and menu items.

## Features

- **Customer Data**: Extracts customer names and their phone numbers from order data.
- **Menu Item Data**: Compiles a list of menu items with their prices and the number of times each item has been ordered.

## File Structure

- `example_orders.json`: Sample order data used for testing.
- `customers.json`: Contains a mapping of phone numbers to customer names.
- `items.json`: Lists menu items with their prices and order counts.
- `script.py`: Python script for processing the order data.

## Requirements

- Python 3.x
- json module (standard library)

## Usage

To run the script, use the following command in your terminal:

```bash
python script.py example_orders.json
