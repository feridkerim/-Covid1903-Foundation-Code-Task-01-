category_id=0
class Category:
    def __init__(self,_name,):
        global category_id
        category_id+=1
        self.id=category_id
        self.categoryName=_name


