def find_roots(polynomial, start, end, step=0.01):
    x = start
    previous_value = polynomial(x)
    
    while x <= end:
        x += step
        current_value = polynomial(x)
        
        if previous_value * current_value <= 0:
            root = x - step * (current_value / (current_value - previous_value))
            yield root
        
        previous_value = current_value
