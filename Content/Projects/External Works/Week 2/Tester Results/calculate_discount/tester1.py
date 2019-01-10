def calculate_discount(num_items, cost_before_discount):
    discount = cost_before_discount
    new_cost = cost_before_discount
    if num_items >= 20:
        discount = discount * 0.25
        new_cost = new_cost - discount
    elif num_items >= 15:
        discount = discount * 0.2
        new_cost = new_cost - discount
    elif num_items >= 10:
        discount = discount * 0.05
        new_cost = new_cost - discount
    elif num_items < 10:
        new_cost = new_cost - 0
        
    return new_cost        
        
