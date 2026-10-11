def calc_depreciation(p, trans_fee, install_fee, years):
    original_price=round(p+trans_fee+install_fee,2)
    annual_rate=round(original_price/years,2)
    monthly_rate=round(annual_rate/12,2)
    return original_price, annual_rate, monthly_rate

