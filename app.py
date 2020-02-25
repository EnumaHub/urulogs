from flask import Flask, render_template, redirect, g, request, url_for
import pymongo
from flask_paginate import Pagination, get_page_args
import data
from errors.handlers import errors


app = Flask(__name__, static_url_path="/static", static_folder='static')
app.register_blueprint(errors)



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/disco')
def disco():

    listacolecciones = data.list_colecciones_disco()

    Objetos = []

    for coleccion in listacolecciones:
        collection = data.display_disco(coleccion)
        Objetos += collection.find({})

    def get_objetos(offset=0, per_page=25):
        return Objetos[offset: offset + per_page]

    
    page, a, offset = get_page_args(page_parameter='page')

    per_page = 20


    
    total = len(Objetos)
    pagination_objetos = get_objetos(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('disco.html',
                           objetos=pagination_objetos,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

@app.route('/tiendainglesa')
def tiendainglesa():
    listacolecciones = data.list_colecciones_tiendainglesa()

    Objetos = []

    for coleccion in listacolecciones:
        collection = data.display_tiendainglesa(coleccion)
        Objetos += collection.find({})

    def get_objetos(offset=0, per_page=25):
        return Objetos[offset: offset + per_page]

    
    page, a, offset = get_page_args(page_parameter='page')

    per_page = 20

    
    total = len(Objetos)
    pagination_objetos = get_objetos(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('tiendainglesa.html',
                           objetos=pagination_objetos,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

@app.route('/articulos/<string:nombre>/')
def objeto_detalles(nombre):
    try:
      articulo = data.display_objeto(nombre)
      historial_precios_punto, fecha_historial_precios, max, min, fecha_precio_max, fecha_precio_min = data.get_historial_precios(nombre)
    except (NameError, TypeError):
      return  render_template('errors/404.html')
    fecha_hoy = data.fecha_hoy()
    precio_hoy = historial_precios_punto[-1]

    


    return render_template('articulo.html', articulo = articulo,
                           historial_precios_punto=historial_precios_punto,
                           fecha_historial_precios=fecha_historial_precios,
                           max=max,
                           min=min,
                           fecha_hoy=fecha_hoy,
                           precio_hoy=precio_hoy,
                           fecha_precio_max=fecha_precio_max,
                           fecha_precio_min=fecha_precio_min)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/categorias')
def categorias():
    cats = ['Carne', 'Lacteos', 'FrutYVerd', 'Fiambres', 'Quesos', 'Pastas', 'Canasta', 'Mascotas', 'Perfumeria']
    return render_template('categorias.html', cats=cats)

@app.route('/disco/<string:categoria>')
def disco_categoria(categoria):
    categorias = data.categoria_disco(categoria)

    def get_objetos(offset=0, per_page=50):
        return categorias[offset: offset + per_page]

    
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    per_page = 13
    total = len(categorias)
    pagination_objetos = get_objetos(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('categoria.html',
                           categorias=pagination_objetos,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route('/tiendainglesa/<string:categoria>')
def ti_categoria(categoria):
    categorias = data.categoria_ti(categoria)

    def get_objetos(offset=0, per_page=50):
        return categorias[offset: offset + per_page]

    
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    per_page = 13
    total = len(categorias)
    pagination_objetos = get_objetos(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('categoria.html',
                           categorias=pagination_objetos,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )

@app.route('/categorias/<string:categoria>/')
def categoria(categoria):
    cat_productos = data.categoria(categoria)

    def get_objetos(offset=0, per_page=50):
        return cat_productos[offset: offset + per_page]

    
    page, per_page, offset = get_page_args(page_parameter='page',
                                           per_page_parameter='per_page')

    per_page = 13
    total = len(cat_productos)
    pagination_objetos = get_objetos(offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total,
                            css_framework='bootstrap4')
    return render_template('categoria.html',
                           cat_productos=pagination_objetos,
                           page=page,
                           per_page=per_page,
                           pagination=pagination,
                           )


@app.route('/search')
def search():
    
    
    value = request.args.get('query')
    encontrados = data.query(value)
    

    return render_template('search.html', encontrados=encontrados, value=value)  

@app.route('/rebajas')
def rebajas():
    value = request.args.get('rebaja')
    if value:
        value = float(value)
    objetos = data.rebajas(value)
    return render_template('rebajas.html', objetos=objetos, value=value)





if __name__ == '__main__':
    app.run(debug=True)