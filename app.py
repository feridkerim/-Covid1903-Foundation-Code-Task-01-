from db import products
from db import firms
from db import categories

firma = ["Nike","Gucci","Lacoste"]
kategoriya = ["Sport-ayaqqabi","Canta","Saat","Ayaqqabi","Aksessuar","T-Shirt","Jeans","Parfum",]
print("Firmalar: ",firma)
print("Kategoriyalar: ",kategoriya)

def firmalarAxtar(_firma_name):
    for Firm in firms:
        if Firm.firmName == _firma_name:
                print(f"{Firm.firmCategory}")




def kategoriyaAxtar(_categories_name):
    for Category in categories:
        if Category.categoryName == _categories_name:
            for Product in products:
                if Product.productCategory ==_categories_name:
                    print(f"{Product.productName}")


_firma_name = input("Firma adini daxil edin: ")

firmalarAxtar(_firma_name)


_categories_name = input("Kategoriya adini daxil edin: ")

kategoriyaAxtar(_categories_name)