# ByteBites UML Class Diagram

```
┌──────────────────────────────────┐
│            Customer              │
├──────────────────────────────────┤
│ - name : String                  │
│ - transactionID : int            │
├──────────────────────────────────┤
│ + login() : bool                 │
│ + purchaseHistory() : List       │
└────────────────┬─────────────────┘
                 │ places 1..*
                 ▼
┌──────────────────────────────────┐
│           Transaction            │
├──────────────────────────────────┤
│ - items : List<Food>             │
│ - totalCost : float              │
├──────────────────────────────────┤
│ + getCustomer() : Customer       │
│ + computeTotal() : float         │
└────────────────┬─────────────────┘
                 │ contains 1..*
                 ▼
┌──────────────────────────────────┐
│              Food                │
├──────────────────────────────────┤
│ - name : String                  │
│ - price : float                  │
│ - category : String              │
│ - quantity : int                 │
│ - popularityRating : float       │
├──────────────────────────────────┤
│ + getQuantity() : int            │
│ + addQuantity(amount: int)       │
└──────────────────────────────────┘
                 ▲
                 │ manages
┌────────────────┴─────────────────┐
│              Menu                │
├──────────────────────────────────┤
│ - items : List<Food>             │
├──────────────────────────────────┤
│ + add_item(food: Food)           │
│ + get_all_items() : List<Food>   │
│ + filter_by_category(            │
│     category: String) : List     │
└──────────────────────────────────┘
```

## Relationships
- `Customer` → `Transaction`: a customer places one or more transactions
- `Transaction` → `Food`: a transaction contains one or more food items
- `Menu` → `Food`: menu manages the collection of available food items

## Notes
- `Menu.items` — list of all available Food objects
- `Transaction.items` — list of Food objects selected by the customer
