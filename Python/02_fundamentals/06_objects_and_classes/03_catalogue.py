class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        filtered_products = filter(lambda x: x[0].upper() == first_letter.upper(), self.products)
        return list(filtered_products)

    def __repr__(self):
        format_products = '\n'.join(sorted(self.products))
        return f'Items in the {self.name} catalogue:\n{format_products}'


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
