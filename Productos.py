Animales = [
    "perro", "gato", "pajaro", "roedor", "pez", "reptil"
]
Categorias = [
    "alimentacion", "juguetes", "higiene", "accesorios", "salud"
]

def validar_producto(tabla_inventario):
    errores= []

    if tabla_inventario["Codigo"].duplicated().any():
        errores.append("Codigo repetido")

    if (tabla_inventario["Stock"] <= 0).any():
        errores.append("El stock no puede ser negativo")

    if(tabla_inventario["Precio"] <= 0).any():
        errores.append("El precio no puede ser negativo")

    for animal in tabla_inventario["Animal"]:
        if animal not in Animales:
            errores.append(f"Animal no valido: {animal} (Perro, Gato, Pajaro, Roedor, Pez, Pez, Reptil")

    for categoria in tabla_inventario["Categoria"]:
        if categoria not in Categorias:
            errores.append(f"Categoría inválida: {categoria} (Alimentacion, Jueguetes, Higiene, Accesorios, Salud")

    return errores
