from menu import products


def calculate_tab(table: list):
    total = 0
    list_id = []
    list_qtd = []
    price_list = []

    for x in table:
        list_id.append(x["_id"])
    for x in table:
        list_qtd.append(x["amount"])
    for x in products:
        if x["_id"] in list_id:
            price_list.append(x["price"])
    for x in range(len(list_qtd)):
        total = total + (list_qtd[x] * price_list[x])

    return {"subtotal": f"${round(total, 2)}"}
