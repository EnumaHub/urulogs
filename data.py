import pymongo
import datetime


conn = pymongo.MongoClient(
            'localhost',
            27017
        )



def categoria(categoria):
    if categoria == 'Carne':
        categoria = 'carnes_rojas_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]
        Objetos = []

        for coleccion in listacategorias:
            Objetos += coleccion.find({})

        categoria = 'pescaderia_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]


        for coleccion in listacategorias:
            Objetos += coleccion.find({})

        
        categoria = 'pollo_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]

        for coleccion in listacategorias:
            Objetos += coleccion.find({})   

    elif categoria == 'Lacteos':
        categoria = 'lacteos_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]
        Objetos = []

        for coleccion in listacategorias:
            Objetos += coleccion.find({})    

    elif categoria == 'FrutYVerd':
        categoria = 'frut_y_verd_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]
        Objetos = []

        for coleccion in listacategorias:
            Objetos += coleccion.find({})   

    elif categoria == 'Fiambres':
        categoria = 'fiambres_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]
        Objetos = []

        for coleccion in listacategorias:
            Objetos += coleccion.find({})   

    elif categoria == 'Quesos':
        categoria = 'queso_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]
        Objetos = []

        for coleccion in listacategorias:
            Objetos += coleccion.find({})   

    elif categoria == 'Perfumeria':
        categoria = 'perfumeria_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]
        Objetos = []

        for coleccion in listacategorias:
            Objetos += coleccion.find({})   

    elif categoria == 'Pastas':
        categoria = 'pastas_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]
        Objetos = []

        for coleccion in listacategorias:
            Objetos += coleccion.find({})  

    elif categoria == 'Canasta':
        categoria = 'canasta_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]
        Objetos = []

        for coleccion in listacategorias:
            Objetos += coleccion.find({})

    elif categoria == 'Mascotas':
        categoria = 'mascotas_tb'
        cat_disco = display_disco(categoria)
        cat_ti = display_tiendainglesa(categoria)
        listacategorias = [cat_disco, cat_ti]
        Objetos = []

        for coleccion in listacategorias:
            Objetos += coleccion.find({})   

    return Objetos


def categoria_ti(categoria):
    Objetos = []
    if categoria == 'Carne':
        categoria = 'carnes_rojas_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

        categoria = 'pescaderia_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})
        
        categoria = 'pollo_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    elif categoria == 'Lacteos':
        categoria = 'lacteos_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    elif categoria == 'FrutYVerd':
        categoria = 'fritas_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})
        categoria = 'verduras_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    elif categoria == 'Fiambres':
        categoria = 'fiambres_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    elif categoria == 'Quesos':
        categoria = 'quesos_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    elif categoria == 'Perfumeria':
        categoria = 'perfumeria_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    elif categoria == 'Pañales':
        categoria = 'paniales_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    elif categoria == 'Canasta':
        categoria = 'canasta_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    elif categoria == 'Mascotas':
        categoria = 'mascotas_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    elif categoria == 'Limpieza':
        categoria = 'limpieza_tb'
        cat_ti = display_tiendainglesa(categoria)
        Objetos += cat_ti.find({})

    return Objetos


def categoria_disco(categoria):
    Objetos = []
    if categoria == 'Carne':
        categoria = 'carnes_rojas_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})

        categoria = 'pescaderia_tb'
        cat_disco = display_disco(categoria)
        
        Objetos += cat_disco.find({})
        
        categoria = 'pollo_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})   

    elif categoria == 'Lacteos':
        categoria = 'lacteos_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})    

    elif categoria == 'FrutYVerd':
        categoria = 'frut_y_verd_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})   

    elif categoria == 'Fiambres':
        categoria = 'fiambres_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})   

    elif categoria == 'Quesos':
        categoria = 'queso_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})   

    elif categoria == 'Perfumeria':
        categoria = 'perfumeria_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})   

    elif categoria == 'Pastas':
        categoria = 'pastas_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})  

    elif categoria == 'Canasta':
        categoria = 'canasta_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})

    elif categoria == 'Mascotas':
        categoria = 'mascotas_tb'
        cat_disco = display_disco(categoria)
        Objetos += cat_disco.find({})   

    return Objetos

def display_todos():
    Objetos = []
    todos_disco = list_colecciones_disco()    
    todos_ti = list_colecciones_tiendainglesa()
    for coleccion in todos_disco:
        coleccion = display_disco(coleccion)
        Objetos += coleccion.find({})
    for coleccion in todos_ti:
        coleccion = display_tiendainglesa(coleccion)
        Objetos += coleccion.find({})

    return Objetos

def query(value):
    #value = "/^" + value + "/i"
    Objetos = []
    todos_disco = list_colecciones_disco()    
    todos_ti = list_colecciones_tiendainglesa()
    for coleccion in todos_disco:
        coleccion = display_disco(coleccion)
        encontrados = coleccion.find( { 'nombre': { '$regex': value, "$options": "i" }  } )
        Objetos += encontrados
    for coleccion in todos_ti:   
        coleccion = display_tiendainglesa(coleccion)     
        encontrados = coleccion.find( { 'nombre': { '$regex': value, "$options": "i" }  } )
        Objetos += encontrados

    return Objetos



def display_disco(tabla):
    db = conn['disco']
    return db[tabla]

def list_colecciones_disco():
    db = conn['disco']
    return db.list_collection_names()


def display_tiendainglesa(tabla):
    db = conn['tiendainglesa']
    return db[tabla]

def list_colecciones_tiendainglesa():
    db = conn['tiendainglesa']
    return db.list_collection_names()

def display_objeto(nombre):
    if nombre is not None:
        listacolecciones = list_colecciones_tiendainglesa()
        for coleccion in listacolecciones:
            collection = display_tiendainglesa(coleccion)
            articulo = collection.find_one({'nombre': nombre})
            if articulo is not None:
                return articulo
            else:
                listacolecciones = list_colecciones_disco()
                for coleccion in listacolecciones:
                    collection = display_disco(coleccion)   
                    articulo = collection.find_one({'nombre': nombre})
                    if articulo is not None:
                        return articulo


def fecha_hoy():
    return datetime.datetime.today().strftime("%d/%m/%y")


def hacer_descuento(precio=0, porcentaje=0):
    percent = precio * porcentaje / 100
    precio = precio - percent
    return int(precio)

def discount_percentage(penultimo_precio, precio_actual):
    try:
        percent_discount = abs(int(precio_actual / penultimo_precio * 100) - 100)
    except ZeroDivisionError:
        percent_discount = 100
    return percent_discount




def contiene_coma(palabra):
    return ["," in palabra for p in palabra]

def contiene_punto(palabra):
    return ["." in palabra for p in palabra]



def rebajas(porcentaje=0):
    if not porcentaje:
        porcentaje = 0
    #procentaje = int(porcentaje)
#.sort('precios.precio', pymongo.ASCENDING)
    todos = display_todos()
    

    #DD = datetime.timedelta(days=dias)
    #hoy = datetime.datetime.today()
    #resta_fechas = hoy - DD
    Objetos = [] 
    Descuentos = []   
    
    for objeto in todos:        
        if len(objeto['precios']) > 1:                                
            penultimo_precio = objeto['precios'][-2]['precio']
            penultimo_fecha = objeto['precios'][-2]['fecha']
            penultimo_precio = penultimo_precio.split('$', 1)[1]
            penultimo_precio = str(penultimo_precio)
            if contiene_punto(penultimo_precio):
                penultimo_precio = "".join(penultimo_precio.split(',', 2)[:1])
                penultimo_precio = penultimo_precio.replace(".", "")
                penultimo_precio = int(penultimo_precio)                                
            else:
                penultimo_precio = penultimo_precio.replace(",","")
                penultimo_precio = penultimo_precio.replace(".","")
                penultimo_precio = int(penultimo_precio)                                                 

            ultimo_precio = objeto['precios'][-1]['precio']
            ultimo_precio = ultimo_precio.split('$', 1)[1]

            ultimo_precio = str(ultimo_precio)
            if contiene_punto(ultimo_precio):
                ultimo_precio = "".join(ultimo_precio.split(',', 2)[:1])
                ultimo_precio = ultimo_precio.replace(".", "")
                                              
            else:
                ultimo_precio = ultimo_precio.replace(",","")
                ultimo_precio = ultimo_precio.replace(".","")
                
            
            ultimo_precio = int(ultimo_precio)  
                
            if porcentaje == 0:
                if penultimo_precio > ultimo_precio:
                    Objetos.append(objeto)
                    descuento_objeto = discount_percentage(penultimo_precio, ultimo_precio)
                    Descuentos.append(descuento_objeto)
            else:                
                rebaja_hecha = hacer_descuento(penultimo_precio, porcentaje)
                rebaja_hecha_10 = hacer_descuento(penultimo_precio, (porcentaje+9.0))
                if (rebaja_hecha >= ultimo_precio) and (rebaja_hecha_10 < ultimo_precio):
                    Objetos.append(objeto)
                    descuento_objeto = discount_percentage(penultimo_precio, ultimo_precio)
                    Descuentos.append(descuento_objeto)
                elif (porcentaje >= 40.0) and (rebaja_hecha >= ultimo_precio):
                    Objetos.append(objeto)
                    descuento_objeto = discount_percentage(penultimo_precio, ultimo_precio)
                    Descuentos.append(descuento_objeto)


    return Objetos, Descuentos


def get_historial_precios(nombre):
    if nombre != None:
        #Busca en TiendaInglesa
        listacolecciones = list_colecciones_tiendainglesa()
        for coleccion in listacolecciones:
            collection = display_tiendainglesa(coleccion)
            articulo = collection.find_one({'nombre': nombre})
            #Si el articulo no esta en TI busca en Disco
            if articulo is not None:
                precios_articulo = []
                historial_precios = []
                historial_precios_punto = []
                fecha_historial_precios = []
                #Agrupa el precio y la fecha en el historial del articulo
                for precios in articulo['precios']:                            
                    precios_articulo.append(precios['precio'])                    
                    fecha_historial_precios.append(precios['fecha'].strftime("%d/%m/%y"))
                historial_precios_tiendainglesa = historial_precios.copy()
                #Le quita el $ y el espacio en blanco al precio para poder graficar
                historial_precios = [i.split('$', 1)[1] for i in precios_articulo]
                historial_precios = [i.strip() for i in historial_precios]
                #Le reemplaza la coma por el punto porque la grafica se confunde sino
                for q in historial_precios:
                    historial_precios_punto.append(q.replace(',','.'))
                max = 0    
                idxmin = 0  
                idxmax = 0     
                min = float(historial_precios_punto[0])                                
                for num in historial_precios_punto:                    
                    if float(num) >= max:
                        max = float(num) 
                        idxmax = historial_precios_punto.index(num)                                   
                    
                    if float(num) < min:
                        min = float(num)
                        idxmin = historial_precios_punto.index(num)
                fecha_precio_max = fecha_historial_precios[idxmax]
                fecha_precio_min = fecha_historial_precios[idxmin]
                return historial_precios_punto, fecha_historial_precios, max, min, fecha_precio_max, fecha_precio_min
            #Busca en Disco
            else:
                listacolecciones = list_colecciones_disco()                
                for coleccion in listacolecciones:
                    collection = display_disco(coleccion)   
                    articulo = collection.find_one({'nombre': nombre})
                    if articulo is not None:
                        precios_articulo = []
                        historial_precios = []
                        historial_precios_punto = []
                        fecha_historial_precios = []
                        #Agrupa el precio y la fecha en el historial del articulo
                        for precios in articulo['precios']:                            
                            precios_articulo.append(precios['precio'])
                            fecha_historial_precios.append(precios['fecha'].strftime("%d/%m/%y"))
                        #historial_precios_tiendainglesa = historial_precios.copy()
                        #Le quita el $ y el espacio en blanco al precio para poder graficar
                        historial_precios = [i.split('$', 1)[1] for i in precios_articulo]
                        historial_precios = [i.strip() for i in historial_precios]
                        for x in historial_precios:
                            if contiene_punto(x):
                                x = "".join(x.split(',', 2)[:1])
                                x = x.replace(".", "")
                                x = int(x)
                                historial_precios_punto.append(x)
                            else:
                                x = x.replace(",","")
                                x = x.replace(".","")
                                x = int(x) 
                                historial_precios_punto.append(x)
                        historial_precios_tiendainglesa = historial_precios_punto.copy()
                        #Le reemplaza la coma por el punto porque la grafica se confunde sino
                        #for q in historial_precios:
                         #   historial_precios_punto.append(q)

                        max = 0   
                        min = (historial_precios_punto[0])
                        idxmin = 0  
                        idxmax = 0                                                                   
                        for num in historial_precios_punto:                                
                            if (num) >= max:                                    
                                max = (num)
                                idxmax = historial_precios_punto.index(num)
                            
                            if (num) < min:                                    
                                min = (num)
                                idxmin = historial_precios_punto.index(num)
                        fecha_precio_max = fecha_historial_precios[idxmax]
                        fecha_precio_min = fecha_historial_precios[idxmin]
                        return historial_precios_punto, fecha_historial_precios, max, min, fecha_precio_max, fecha_precio_min
                        