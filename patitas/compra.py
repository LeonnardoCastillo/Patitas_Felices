class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            carrito = self.session["carrito"] = {}
        self.carrito=carrito 
    
    def agregar(self, patitas):
        if patitas.code not in self.carrito.keys():
            self.carrito[patitas.code]={
                "patitas_id":patitas.code, 
                "nombre": patitas.nombre,
                "precio": str (patitas.precio),
                "cantidad": 1,
                "total": patitas.precio,
            }
        else:
            for key, value in self.carrito.items():
                if key==patitas.code:
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = patitas.precio
                    value["total"]= value["total"] + patitas.precio
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified=True


    def eliminar(self, patitas):
        id = patitas.code
        if id in self.carrito: 
            del self.carrito[id]
            self.guardar_carrito()
    
    def restar (self,patitas):
        for key, value in self.carrito.items():
            if key == patitas.code:
                value["cantidad"] = value["cantidad"]-1
                value["total"] = int(value["total"])- patitas.precio
                if value["cantidad"] < 1:   
                    self.eliminar(patitas)
                break
        self.guardar_carrito()
     
    def limpiar(self):
        self.session["carrito"]={}
        self.session.modified=True 