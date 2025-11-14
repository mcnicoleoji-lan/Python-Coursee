def total_calc(bill_amount, tip_perc=10):
    total = bill_amount * (1 + 0.01 * tip_perc)
    total = round(total, 2)
    print(f"Please pay ${total}")

total_calc(150)        # uses default 10%
total_calc(150, 20)    # uses 20%

