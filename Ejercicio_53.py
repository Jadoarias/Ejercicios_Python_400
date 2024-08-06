tienda = {
    'frutas': {
        'manzana': 0.5,
        'banana': 0.3,
        'naranja': 0.4
    },
    'verduras': {
        'zanahoria': 0.2,
        'brocoli': 0.8,
        'espinaca': 0.5
    },
    'lácteos': {
        'leche': 1.0,
        'queso': 2.5,
        'yogur': 1.5
    }
}

def mostrarproductos(tienda):
    for categoria, producto in tienda.items():
        for producto, precio in producto.items():
            print(producto, precio)

mostrarproductos(tienda)