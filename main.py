from management.product_handler import get_product_by_id
from management.product_handler import get_products_by_type
from management.product_handler import add_product
from management.product_handler import menu_report
from management.product_handler import add_product_extra
from management.tab_handler import calculate_tab
from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_product_by_id(1))
    print(get_products_by_type("drink"))

    new_product = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food"
    }
    print(add_product(products, **new_product))

    table_1 = [{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]
    table_2 = [
        {"_id": 10, "amount": 3},
        {"_id": 20, "amount": 2},
        {"_id": 21, "amount": 5},
    ]
    print(calculate_tab(table_2))

    print(menu_report())

    new_product_2 = {
        "title": "X-Python",
        "price": 5.0,
        "rating": 5,
        "description": "Sanduiche de Python",
        "type": "fast-food",
        "extra_key_1": "extra_value_1",
        "extra_key_2": "extra_value_2"
    }
    required_keys = ("description", "price", "rating", "title", "type")

    print(add_product_extra(products, *required_keys, **new_product_2))
