# ByteBites UML Class Diagram

```
┌─────────────────────────────┐
│          Customer           │
├─────────────────────────────┤
│ - name                      │
│ - transactionID             │
├─────────────────────────────┤
│ + purchaseHistory()         │
│ + login()                   │
└─────────────┬───────────────┘
              │ places
              │ 1..*
              ▼
┌─────────────────────────────┐
│         Transaction         │
├─────────────────────────────┤
│ - items                     │
│ - totalCost                 │
├─────────────────────────────┤
│ + getCustomer()             │
│ + computeTotal()            │
└─────────────┬───────────────┘
              │ contains
              │ 1..*
              ▼
┌─────────────────────────────┐
│            Food             │
├─────────────────────────────┤
│ - name                      │
│ - price                     │
│ - category                  │
│ - quantity                  │
├─────────────────────────────┤
│ + getQuantity()             │
│ + addQuantity()             │
└─────────────────────────────┘
              ▲
              │ manages
              │
┌─────────────┴───────────────┐
│            Menu             │
├─────────────────────────────┤
│ - items                     │
├─────────────────────────────┤
│ + add_item(food)            │
│ + get_all_items()           │
│ + filter_by_category()      │
└─────────────────────────────┘
```

## Relationships
- `Customer` → `Transaction`: a customer places one or more transactions
- `Transaction` → `Food`: a transaction contains one or more food items
- `Menu` → `Food`: menu manages the collection of available food items

## Notes
- `Menu.items` — list of all available Food objects
- `Transaction.items` — list of Food objects selected by the customer
