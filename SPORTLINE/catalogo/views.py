# views.py
from django.shortcuts import render, redirect
from urllib.parse import quote

# =====================================
# PRODUCTOS DEL CATÁLOGO
# =====================================
PRODUCTOS = [  
  {
    "id": 1,
    "nombre": "Camiseta Otr B Tee de Mujer",
    "descripcion": "Camiseta Adidas Otr B Tee para mujer, diseñada para ofrecer comodidad y ligereza durante entrenamientos y uso diario.",
    "precio": 39.95,
    "precio_oferta": 33.96,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/camisa2.webp",
    "tipo": "camisas"
  },
  {
    "id": 2,
    "nombre": "Pantalón Largo Frozen Leggings de Niña",
    "descripcion": "Leggings Adidas Frozen para niña, cómodos y ideales para actividades diarias o deportivas.",
    "precio": 7.99,
    "categoria": "Gym",
    "color": "N/A",
    "talla": "S, M, L",
    "imagen": "catalogo/pantalon1.webp",
    "tipo": "leggins"
  },
  {
    "id": 3,
    "nombre": "Pantalón Corto UA Launch 7S de Hombre",
    "descripcion": "Short Under Armour Launch 7S para hombre, ligero y diseñado para entrenamientos y running.",
    "precio": 24.99,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/short1.webp",
    "tipo": "shorts"
  },
  {
    "id": 4,
    "nombre": "Abrigo UA Velociti Storm de Hombre",
    "descripcion": "Abrigo Under Armour UA Velociti Storm para hombre, diseñado para protección contra el clima y máximo confort.",
    "precio": 99.95,
    "categoria": "Casual",
    "color": "N/A",
    "talla": "M, L, XL",
    "imagen": "catalogo/sudadera1.webp",
    "tipo": "sudaderas"
  },
  {
    "id": 5,
    "nombre": "Zapatillas ZoomX Vaporfly Next 4 de Hombre",
    "descripcion": "Zapatillas Nike ZoomX Vaporfly Next 4 para hombre, diseñadas para máximo rendimiento y velocidad.",
    "precio": 329.95,
    "precio_oferta": 280.46,
    "categoria": "Calzado",
    "color": "N/A",
    "talla": "40, 41, 42, 43, 44",
    "imagen": "catalogo/zapato1.webp",
    "tipo": "tennis"
  },
  {
    "id": 6,
    "nombre": "Balón Puma Orbita 6 Copa Unisex",
    "descripcion": "Balón Puma Orbita 6 Copa, diseñado para alto rendimiento y uso profesional.",
    "precio": 18.95,
    "categoria": "Accesorios",
    "color": "N/A",
    "talla": "",
    "imagen": "catalogo/balon1.webp",
    "tipo": "balones"
  },
  {
    "id": 7,
    "nombre": "Camiseta Otr B Tee de Mujer",
    "descripcion": "Camiseta Adidas Otr B Tee para mujer, diseñada para brindar comodidad y ligereza en entrenamientos y actividades diarias.",
    "precio": 39.95,
    "precio_oferta": 33.96,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/camisa3.webp",
    "tipo": "camisas"
  },
  {
    "id": 8,
    "nombre": "Pantalón Largo Essentials Linear Leggings de Niña",
    "descripcion": "Leggings Adidas Essentials para niña, cómodos y perfectos para uso diario o deportivo.",
    "precio": 18.20,
    "categoria": "Niñas",
    "color": "N/A",
    "talla": "S, M, L",
    "imagen": "catalogo/pantalon2.webp",
    "tipo": "leggins"
  },
  {
    "id": 9,
    "nombre": "Pantalón Corto UA Trail Run 5S de Hombre",
    "descripcion": "Short Under Armour Trail Run 5S para hombre, ideal para trail, running y entrenamientos exigentes.",
    "precio": 44.99,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/short2.webp",
    "tipo": "shorts"
  },
  {
    "id": 10,
    "nombre": "Camiseta Performance Long-T 2 de Hombre",
    "descripcion": "Camiseta On Performance Long-T 2 para hombre, ligera y diseñada para entrenamientos y alto rendimiento.",
    "precio": 74.99,
    "categoria": "Casual",
    "color": "N/A",
    "talla": "M, L, XL",
    "imagen": "catalogo/sudadera2.webp",
    "tipo": "sudaderas"
  },
  {
    "id": 11,
    "nombre": "Zapatillas Zoom Vapor Cage 4 Rafa de Hombre",
    "descripcion": "Zapatillas Nike Zoom Vapor Cage 4 Rafa para hombre, diseñadas para máximo control y durabilidad en la cancha.",
    "precio": 179.99,
    "precio_oferta": 152.99,
    "categoria": "Calzado",
    "color": "N/A",
    "talla": "40, 41, 42, 43, 44",
    "imagen": "catalogo/zapato2.webp",
    "tipo": "tennis"
  },
  {
    "id": 12,
    "nombre": "Balón Epp Club Unisex",
    "descripcion": "Balón Adidas Epp Club, ideal para entrenamientos y juego recreativo.",
    "precio": 19.95,
    "categoria": "Accesorios",
    "color": "N/A",
    "talla": "",
    "imagen": "catalogo/balon2.webp",
    "tipo": "balones"
  },
  {
    "id": 13,
    "nombre": "Camiseta Otr Mel Tee de Mujer",
    "descripcion": "Camiseta Adidas Otr Mel Tee para mujer, cómoda y diseñada para un rendimiento óptimo en actividades deportivas.",
    "precio": 54.95,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/camisa4.webp",
    "tipo": "camisas"
  },
  {
    "id": 14,
    "nombre": "Pantalón Largo Jordan Sneaker School Knit de Niño",
    "descripcion": "Pantalón Jordan Sneaker School Knit para niño, cómodo, moderno y perfecto para uso diario.",
    "precio": 29.24,
    "categoria": "Niños",
    "color": "N/A",
    "talla": "S, M, L",
    "imagen": "catalogo/pantalon3.webp",
    "tipo": "leggins"
  },
  {
    "id": 15,
    "nombre": "Pantalón Corto UA Day Of The Day de Hombre",
    "descripcion": "Short Under Armour Day Of The Day para hombre, cómodo y ligero para entrenamientos y uso diario.",
    "precio": 24.99,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/short3.webp",
    "tipo": "shorts"
  },
  {
    "id": 16,
    "nombre": "Abrigo Climate de Hombre",
    "descripcion": "Abrigo On Climate para hombre, diseñado para brindar calidez y comodidad en climas fríos.",
    "precio": 139.95,
    "precio_oferta": 118.96,
    "categoria": "Casual",
    "color": "N/A",
    "talla": "M, L, XL",
    "imagen": "catalogo/sudadera3.webp",
    "tipo": "sudaderas"
  },
  {
    "id": 17,
    "nombre": "Zapatillas Zoom Fly 6 de Hombre",
    "descripcion": "Zapatillas Nike Zoom Fly 6 para hombre, creadas para brindar velocidad y comodidad en cada entrenamiento.",
    "precio": 249.95,
    "categoria": "Calzado",
    "color": "N/A",
    "talla": "40, 41, 42, 43, 44",
    "imagen": "catalogo/zapato3.webp",
    "tipo": "tennis"
  },
  {
    "id": 18,
    "nombre": "Balón Puma Orbita 6 MS Unisex",
    "descripcion": "Balón Puma Orbita 6 MS, diseñado para entrenamientos y juego recreativo con excelente durabilidad.",
    "precio": 19.95,
    "categoria": "Accesorios",
    "color": "N/A",
    "talla": "",
    "imagen": "catalogo/balon3.webp",
    "tipo": "balones"
  },
  {
    "id": 19,
    "nombre": "Camiseta Run It de Mujer",
    "descripcion": "Camiseta Adidas Run It para mujer, ideal para running y actividades deportivas gracias a su comodidad y ligereza.",
    "precio": 32.95,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/camisa5.webp",
    "tipo": "camisas"
  },
  {
    "id": 20,
    "nombre": "Pantalón Largo T7 Relaxed Track Pant de Mujer",
    "descripcion": "Pantalón Puma T7 Relaxed Track Pant para mujer, cómodo y moderno para uso diario o entrenamiento.",
    "precio": 43.75,
    "categoria": "Femenino",
    "color": "N/A",
    "talla": "S, M, L",
    "imagen": "catalogo/pantalon4.webp",
    "tipo": "leggins"
  },
  {
    "id": 21,
    "nombre": "Pantalón Corto UA Run Anywhere de Hombre",
    "descripcion": "Short Under Armour Run Anywhere para hombre, ideal para running y entrenamientos intensos.",
    "precio": 44.99,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/short4.webp",
    "tipo": "shorts"
  },
  {
    "id": 22,
    "nombre": "Abrigo Launch Lightweight Jkt de Hombre",
    "descripcion": "Abrigo Under Armour Launch Lightweight Jkt para hombre, ligero y cómodo para entrenamientos y uso diario.",
    "precio": 84.99,
    "categoria": "Casual",
    "color": "N/A",
    "talla": "M, L, XL",
    "imagen": "catalogo/sudadera4.webp",
    "tipo": "sudaderas"
  },
  {
    "id": 23,
    "nombre": "Zapatillas Zoom Fly 5 de Hombre",
    "descripcion": "Zapatillas Nike Zoom Fly 5 para hombre, ideales para entrenamientos cómodos y carreras de larga distancia.",
    "precio": 149.99,
    "precio_oferta": 127.49,
    "categoria": "Calzado",
    "color": "N/A",
    "talla": "40, 41, 42, 43, 44",
    "imagen": "catalogo/zapato4.webp",
    "tipo": "tennis"
  },
  {
    "id": 24,
    "nombre": "Balón Epp Club Unisex",
    "descripcion": "Balón Adidas Epp Club, ideal para entrenamientos y juegos recreativos.",
    "precio": 19.95,
    "categoria": "Accesorios",
    "color": "N/A",
    "talla": "",
    "imagen": "catalogo/balon4.webp",
    "tipo": "balones"
  },
  {
    "id": 25,
    "nombre": "Camiseta Otr B Tee de Hombre",
    "descripcion": "Camiseta Adidas Otr B Tee para hombre, diseñada para brindar comodidad y rendimiento en actividades deportivas.",
    "precio": 36.95,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/camisa1.webp",
    "tipo": "camisas"
  },
  {
    "id": 26,
    "nombre": "Pantalón 3/4 W Nk Bliss Vctry Pant de Mujer",
    "descripcion": "Pantalón Nike Bliss Victory 3/4 para mujer, ligero y cómodo para entrenamiento o uso diario.",
    "precio": 32.50,
    "precio_oferta": 27.62,
    "categoria": "Femenino",
    "color": "N/A",
    "talla": "S, M, L",
    "imagen": "catalogo/pantalon5.webp",
    "tipo": "leggins"
  },
  {
    "id": 27,
    "nombre": "Pantalón Corto Run It Brand Love de Hombre",
    "descripcion": "Short Adidas Run It Brand Love para hombre, diseñado para brindar comodidad y ligereza durante el running.",
    "precio": 29.99,
    "categoria": "Running",
    "color": "N/A",
    "talla": "S, M, L, XL",
    "imagen": "catalogo/short5.webp",
    "tipo": "shorts"
  },
  {
    "id": 28,
    "nombre": "Camiseta UA Launch Long Sleeve de Hombre",
    "descripcion": "Camiseta Under Armour Launch Long Sleeve para hombre, ligera y diseñada para entrenamientos y uso deportivo.",
    "precio": 44.95,
    "categoria": "Casual",
    "color": "N/A",
    "talla": "M, L, XL",
    "imagen": "catalogo/sudadera5.webp",
    "tipo": "sudaderas"
  },
  {
    "id": 29,
    "nombre": "Zapatillas Znsored Hi Prem Lea de Hombre",
    "descripcion": "Zapatillas Adidas Znsored Hi Prem Lea para hombre, combinando estilo urbano y comodidad para el uso diario.",
    "precio": 59.99,
    "precio_oferta": 50.99,
    "categoria": "Calzado",
    "color": "N/A",
    "talla": "40, 41, 42, 43, 44",
    "imagen": "catalogo/zapato5.webp",
    "tipo": "tennis"
  },
  {
    "id": 30,
    "nombre": "Balón Nike Phantom Unisex",
    "descripcion": "Balón Nike Phantom, diseñado para mayor control y durabilidad durante entrenamientos y partidos recreativos.",
    "precio": 25.95,
    "categoria": "Accesorios",
    "color": "N/A",
    "talla": "",
    "imagen": "catalogo/balon5.webp",
    "tipo": "balones"
  }

]

# =====================================
# FUNCIONES AUXILIARES
# =====================================

def _buscar_producto(producto_id):
    for p in PRODUCTOS:
        if p["id"] == producto_id:
            return p
    return None


def get_carrito(request):
    """
    Normaliza el carrito: si está en formato LISTA, lo convierte a diccionario.
    Estructura final:
    {
      "1": {"cantidad": 2},
      "3": {"cantidad": 1},
      ...
    }
    """
    carrito = request.session.get("carrito", {})

    # Versión antigua: lista [1,2,3]
    if isinstance(carrito, list):
        nuevo = {}
        for pid in carrito:
            pid = str(pid)
            if pid in nuevo:
                nuevo[pid]["cantidad"] += 1
            else:
                nuevo[pid] = {"cantidad": 1}
        carrito = nuevo
        request.session["carrito"] = carrito

    # Si no es dict, lo reseteamos
    if not isinstance(carrito, dict):
        carrito = {}
        request.session["carrito"] = carrito

    return carrito


def obtener_total_items(request):
    carrito = get_carrito(request)
    return sum(item.get("cantidad", 0) for item in carrito.values())


# =====================================
# VISTAS PRINCIPALES
# =====================================

def landing_catalogo(request):
    filtro_tipo = request.GET.get("tipo")

    if filtro_tipo:
        productos_mostrar = [p for p in PRODUCTOS if p["tipo"] == filtro_tipo]
    else:
        productos_mostrar = PRODUCTOS

    tipos = sorted(set(p["tipo"] for p in PRODUCTOS))

    return render(request, "landing_productos.html", {
        "productos": productos_mostrar,
        "tipos": tipos,
        "filtro_actual": filtro_tipo,
        "titulo": "Sportline - Ropa Deportiva",
        "slogan": "Activa tu mejor versión.",
        "cantidad_items": obtener_total_items(request),
    })


def carrito(request):
    carrito = get_carrito(request)

    productos_en_carrito = []
    total_con_descuento = 0.0
    total_sin_descuento = 0.0

    for pid_str, datos in carrito.items():
        producto = _buscar_producto(int(pid_str))
        if not producto:
            continue

        cantidad = datos.get("cantidad", 1)

        precio_normal = float(producto["precio"])
        precio_final = float(producto.get("precio_oferta", precio_normal))

        subtotal = cantidad * precio_final
        subtotal_sin_desc = cantidad * precio_normal

        total_con_descuento += subtotal
        total_sin_descuento += subtotal_sin_desc

        # porcentaje de descuento por producto
        descuento_porcentaje = None
        if "precio_oferta" in producto:
            try:
                descuento_porcentaje = round(
                    (1 - (precio_final / precio_normal)) * 100
                )
            except ZeroDivisionError:
                descuento_porcentaje = None

        productos_en_carrito.append({
            "id": producto["id"],
            "nombre": producto["nombre"],
            "categoria": producto["categoria"],
            "cantidad": cantidad,
            "precio": precio_final,                 # precio que se está cobrando
            "precio_normal": precio_normal,         # referencia
            "precio_oferta": producto.get("precio_oferta"),
            "descuento_porcentaje": descuento_porcentaje,
            "subtotal": subtotal,
        })

    # porcentaje de descuento total del carrito
    descuento_total_porcentaje = None
    if total_sin_descuento > 0 and total_con_descuento < total_sin_descuento:
        descuento_total_porcentaje = round(
            (1 - (total_con_descuento / total_sin_descuento)) * 100
        )

    # WhatsApp de compra
    numero = "50363096495"
    if productos_en_carrito:
        partes = [
            f"{p['cantidad']}x {p['nombre']} (${p['subtotal']:.2f})"
            for p in productos_en_carrito
        ]
        mensaje = "Hola, me interesa realizar esta compra:\n" + "\n".join(partes)
        mensaje += f"\n\nTotal: ${total_con_descuento:.2f}"
        whatsapp_compra = f"https://wa.me/{numero}?text={quote(mensaje)}"
    else:
        whatsapp_compra = None

    return render(request, "carrito.html", {
        "productos": productos_en_carrito,
        "total": total_con_descuento,
        "cantidad_items": obtener_total_items(request),
        "whatsapp_compra": whatsapp_compra,
        "descuento_total_porcentaje": descuento_total_porcentaje,
    })


# =====================================
# ACCIONES DE CARRITO
# =====================================

def agregar_carrito(request, producto_id):
    carrito = get_carrito(request)
    pid = str(producto_id)

    if pid in carrito:
        carrito[pid]["cantidad"] += 1
    else:
        carrito[pid] = {"cantidad": 1}

    request.session["carrito"] = carrito
    return redirect("landing_catalogo")


def aumentar(request, producto_id):
    carrito = get_carrito(request)
    pid = str(producto_id)

    if pid in carrito:
        carrito[pid]["cantidad"] += 1

    request.session["carrito"] = carrito
    return redirect("carrito")


def disminuir(request, producto_id):
    carrito = get_carrito(request)
    pid = str(producto_id)

    if pid in carrito:
        carrito[pid]["cantidad"] -= 1
        if carrito[pid]["cantidad"] <= 0:
            carrito.pop(pid)

    request.session["carrito"] = carrito
    return redirect("carrito")


def eliminar(request, producto_id):
    carrito = get_carrito(request)
    pid = str(producto_id)

    if pid in carrito:
        carrito.pop(pid)

    request.session["carrito"] = carrito
    return redirect("carrito")


def vaciar_carrito(request):
    request.session["carrito"] = {}
    return redirect("carrito")