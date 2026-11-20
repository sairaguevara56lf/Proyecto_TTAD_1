import json

with open("data.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)

ventas = datos["ventas"]  


def total_facturado():
    total = 0  
    for venta in ventas:
        
        total += venta["cantidad"] * venta["precio_unitario"]
    return total


def ventas_por_categoria():
    facturacion_categoria = {} 
    unidades_categoria = {}     

    for venta in ventas:
        categoria = venta["categoria"]
        importe = venta["cantidad"] * venta["precio_unitario"]

    
        if categoria not in facturacion_categoria:
            facturacion_categoria[categoria] = 0
            unidades_categoria[categoria] = 0

        facturacion_categoria[categoria] += importe
        unidades_categoria[categoria] += venta["cantidad"]

    return {
        "facturacion": facturacion_categoria,
        "unidades": unidades_categoria,
    }


def producto_mas_vendido():
    unidades_producto = {}  

    for venta in ventas:
        producto = venta["producto"]
        if producto not in unidades_producto:
            unidades_producto[producto] = 0
        unidades_producto[producto] += venta["cantidad"]

    
    mejor_producto = max(unidades_producto, key=unidades_producto.get)
    return mejor_producto, unidades_producto[mejor_producto]


if __name__ == "__main__":
    print("Total facturado:", total_facturado())
    print("Ventas por categoría:", ventas_por_categoria())
    print("Producto más vendido:", producto_mas_vendido())