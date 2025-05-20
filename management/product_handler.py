from menu import products


def get_product_by_id(id: int):
    if type(id) is not int:
        raise TypeError("product id must be an int")
    
    for i in range(len(products)):
        if products[i].get("_id") == id:
            return products[i]
    else:
        return {}


def get_products_by_type(tipo: str):
    if type(tipo) is not str:
        raise TypeError("product type must be a str")
    
    list_type = []
    for i in range(len(products)):
        if products[i].get("type") == tipo:
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


def menu_report():
    product_count = len(products)

    average_price = [n["price"] for n in products]
    average_price = round(sum(average_price) / len(average_price), 2)

    type_list = [n["type"] for n in products]
    list_x = []
    for n in range(len(type_list)):
        x = type_list.count(type_list[n])
        list_x.append({type_list[n]: x})
    list_y = []
    for n in list_x:
        if n not in list_y:
            list_y.append(n)
    maior_type = max(list_y, key=lambda x: list(x.values())[0])
    maior_type = list(maior_type)[0]

    return f"Products Count: {product_count} - Average Price: ${average_price} - Most Common Type: {maior_type}"