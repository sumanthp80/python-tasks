class Mobile:
    m1 = "Samsung Mobiles" #Global attributes
    def price(self):
        m1 = "Costly mobiles"   #Local attributes
        return m1
Sam_m = Mobile()
print(Sam_m.m1)
print(Sam_m.price())