import json

products = {'0001' : {'title' : 'Jaws Somnambula', 'category' : 'beer', 'price' : '250.00'},
            '0002' : {'title' : 'Jaws Citrazen', 'category' : 'beer', 'price' : '200.00'},
            '0003' : {'title' : 'gold mango' , 'category' : 'fruits', 'price' : '168.50'},
            '0004' : {'title' : 'Современные операционные системы', 'category' : 'book', 'price' : '3120.00'}
           }
discounts = {'category' : {'all' : 0.1, 'fruits' : 0.2, 'beer' : 0.05},
             'title' : {'Jaws Somnambula' : 0.3, 'gold mango' : 0.15, 'Современные операционные системы' : -0.5}
            }



with open('data.json', 'w') as f:
    json.dump(products, f, ensure_ascii=False, sort_keys=True, indent=4)

with open('discounts.json', 'w') as f:
    json.dump(discounts, f, ensure_ascii=False, sort_keys=True, indent=4)