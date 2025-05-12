from menu import products


def get_product_by_id(id: int):
    for i in range(len(products)):
        if products[i].get("_id") == id:
            return products[i]
    else:
        return {}


def get_products_by_type(type: str):
    list_type = []
    for i in range(len(products)):
        if products[i].get("type") == type:
            list_type.append(products[i])
    return list_type


# 2ª forma possivel
def get_product_by_id_2(id: int):
    x = next(filter(lambda item: item.get("_id") == id, products), {})
    return x


# 2ª forma possivel
def get_products_by_type_2(type: str):
    x = list(filter(lambda item: item.get("type") == type, products))
    return x
