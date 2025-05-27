inventory = [
    # name,       category,   unit_price, units_sold, units_left
    ["Strawberry", "Fruit",      3.50,        40,          10],
    ["Broccoli",   "Vegetable",  2.20,        25,           8],
    ["Cheddar",    "Dairy",      5.00,        18,           4],
    ["Baguette",   "Bakery",     2.80,        35,           2],
    ["Blueberry",  "Fruit",      4.00,        22,           6],
    ["Spinach",    "Vegetable",  1.80,        30,          12],
    ["Yogurt",     "Dairy",      1.20,        50,          15],
    ["Croissant",  "Bakery",     3.00,        28,           3],
]

#Questions
# calculate the TotalRevenue
# List Low stock item if stock is less than 5
# calculte the categorywise Revenue

total_rev = sum(item[2]*item[3] for item in inventory)
print(f'Total Revenue: {total_rev}')  
#Output:
#Total Revenue: 669.0

for item in inventory:
    if item[4]<5:
        print(f'low stock:',item[4]) 
# Output:
# low stock: 4
# low stock: 2
# low stock: 3
        
total_revenue=1
for item in inventory:
    total_revenue = item[2]*item[3]
    print(f'Category: {item[1]} and total revenue is  {total_revenue:.2f}')
    
#Output:
# Category: Fruit and total revenue is  140.00
# Category: Vegetable and total revenue is  55.00
# Category: Dairy and total revenue is  90.00
# Category: Bakery and total revenue is  98.00
# Category: Fruit and total revenue is  88.00
# Category: Vegetable and total revenue is  54.00
# Category: Dairy and total revenue is  60.00
# Category: Bakery and total revenue is  84.00