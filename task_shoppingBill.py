
def calculateElectronicsGST(a, b):
    total = a + b
    gst = total * 18 / 100
    return total + gst


def calculateFashionGST(c, d):
    total = c + d
    gst = total * 13 / 100
    return total + gst


def calculateFoodGST(e):
    gst = e * 7 / 100
    return e + gst


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)
    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 20 / 100
    return total - discount


a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)
total = totalBill(a, b, c, d, e)
discount = total * 20 / 100
final_amount = calculateDiscountedBill(a, b, c, d, e)

print("Electronics after GST =", format(electronics, ".2f"))
print("Fashion after GST =", format(fashion, ".2f"))
print("Food after GST =", format(food, ".2f"))
print("Total after GST =", format(total, ".2f"))
print("Discount =", format(discount, ".2f"))
print("Final payable amount =", format(final_amount, ".2f"))
