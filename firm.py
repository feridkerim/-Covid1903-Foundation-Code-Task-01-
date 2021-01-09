firm_id = 0


class Firm:


    def __init__(self, _name,_category,):
        global firm_id
        firm_id += 1
        self.id=firm_id
        self.firmName = _name
        self.firmCategory=_category
