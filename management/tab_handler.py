from menu import products


def calculate_tab(table: list):
    total = 0
    dict_produtos = {produto["_id"]: produto["price"] for produto in products}

    for pedido in table:
        produto_id = pedido["_id"]
        qtd = pedido["amount"]
        if produto_id in dict_produtos:
            total += dict_produtos[produto_id] * qtd

    return {"subtotal": f"${round(total, 2)}"}
