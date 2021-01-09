product_id=0
class Product:

    def __init__(self,_firm,_category,_name):
        global product_id
        product_id += 1
        self.id=product_id
        self.productCompany=_firm
        self.productCategory=_category
        self.productName=_name

