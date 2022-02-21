def format_number(Non_negative):
    if int(Non_negative) < 0:
        return "Wrong"
    else:
        number = str(Non_negative)
        return "{:,}".format(Non_negative)

print(format_number(777777))