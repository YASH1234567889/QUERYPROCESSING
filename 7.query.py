import pandas as pd
sales_data = pd.DataFrame({
    'item': ['Item A', 'Item B', 'Item A', 'Item C', 'Item B', 'Item A'],
    'sale_value': [200, 150, 250, 300, 100, 275],
    'date': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04', '2024-11-05', '2024-11-06']
})
pivot_table = pd.pivot_table(sales_data, 
                             values='sale_value', 
                             index='item', 
                             aggfunc=['max', 'min'])

print(pivot_table)
