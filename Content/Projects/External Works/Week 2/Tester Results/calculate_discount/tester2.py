def calculate_discount(num_items, cost_before_discount):

    new_cost = cost_before_discount

    if num_items >= 20:
        cost_before_discount = cost_before_discount * 0.25
        new_cost = new_cost - cost_before_discount

    elif num_items >= 15:
        cost_before_discount = cost_before_discount * 0.2
        new_cost = new_cost - cost_before_discount

    elif num_items >= 10:
        cost_before_discount = cost_before_discount * 0.05
        new_cost = new_cost - cost_before_discount
        
    return new_cost  
