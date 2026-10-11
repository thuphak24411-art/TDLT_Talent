def view_details(original_price, annual_rate, years):
    details=[]
    for i in range(1, years+1):
        remaining_value= original_price-annual_rate*i
        details.append(f"Năm {i}, sau khấu hao còn {remaining_value}")
        i=i+1
    return details
