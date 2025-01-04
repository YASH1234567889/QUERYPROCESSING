import pandas as pd
sales_data = pd.DataFrame({
    'item': ['Item A', 'Item B', 'Item A', 'Item C', 'Item B', 'Item A'],
    'units_sold': [5, 3, 7, 2, 4, 6],
    'date': ['2024-11-01', '2024-11-02', '2024-11-03', '2024-11-04', '2024-11-05', '2024-11-06']
})
pivot_table = pd.pivot_table(sales_data, 
                             values='units_sold', 
                             index='item', 
                             aggfunc='sum')
print(pivot_table)
