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
        if products[i].get("type") == type.lower():
            list_type.append(products[i])
    return list_type


# 2ª forma
def get_product_by_id_2(id: int):
    x = next(filter(lambda item: item.get("_id") == id, products), {})
    return x


# 2ª forma
def get_products_by_type_2(type: str):
    x = list(filter(lambda item: item.get("type") == type, products))
    return x


def add_product(products: list, **kwargs):
    dict_1 = kwargs

    if len(products) == 0:
        dict_1["_id"] = 1
    else:
        x = []
        for y in products:
            x.append(y["_id"])
            x.sort()
        dict_1["_id"] = x[-1] + 1
    products.append(dict_1)
    return dict_1
