# StdClass
Allow dot access from a python dictionary

example

```
from datetime import datetime
from decimal import Decimal

# dictionary
customer_dict = {
    'name': 'Kevin',
    'timestamp': datetime.now(),
    'purchases': [
        {
            'item_name': 'Gatorade',
            'price': Decimal('1.27')
        },
        {
            'item_name': 'Chocolate Bar',
            'price': Decimal('.99')
        }

    ]

}

customer_class = StdClass(customer_dict)

# dot access on attributes
print(customer_class.name)

# key access remains
print(customer_class['name'])

# classes are created recursively
for purchase in customer_class.purchases:
    print(purchase.item_name, purchase.price)
```



