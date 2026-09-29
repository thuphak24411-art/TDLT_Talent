def calc_bill(old, new, group):
    bill=0
    kWh=old-new
    if kWh >= 0:
        if group=="no_prepaid":
            if kWh<=50:
                bill = kWh * 1549
            elif kWh<=100:
                bill = 50 * 1549 + (kWh - 50) * 1600
            elif kWh<=200:
                bill = 50 * 1549 + 50 * 1600 + (kWh - 100) * 1858
            elif kWh<=300:
                bill = 50 * 1549 + 50 * 1600 + 100 * 1858 + (kWh - 200) * 2340
            elif kWh<=400:
                bill = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + (kWh - 300) * 2615
            else:
                bill = 50 * 1549 + 50 * 1600 + 100 * 1858 + 100 * 2340 + 100 * 2615 + (kWh - 400) * 2701
        else:
            bill =  kWh * 2271
    else:
        return "old Kwh must be higher than new kWh"
    return bill