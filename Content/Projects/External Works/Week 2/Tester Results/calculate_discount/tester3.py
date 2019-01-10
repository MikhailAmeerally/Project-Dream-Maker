def calculate_discount(num_items, cost_before_discount):

    discount_in_dollars = 0

    if num_items >= 20:
        discount_in_dollars = cost_before_discount * 0.25
    elif num_items >= 15:
        discount_in_dollars = cost_before_discount * 0.2
    elif num_items >= 10:
        discount_in_dollars = cost_before_discount * 0.05
        
    return cost_before_discount - discount_in_dollars 
