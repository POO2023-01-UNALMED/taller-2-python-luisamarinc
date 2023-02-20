class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ("verde","rojo" ,"amarillo","negro" , "blanco"):
            self.color = color


class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro =  registro
    
    def asignarTipo(self, tipo):
        if tipo in ("electrico","gasolina"):
            self.tipo = tipo

class Auto:
    cantidadCreado = 0
    
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo= modelo
        self.precio = precio
        self.registro = registro
        self.marca = marca
        self.asientos = asientos
        self.motor =  motor

    def cantidadAsientos(self):
        numeroAsientos = 0

        for asiento in self.asientos:
            if type(asiento) == Asiento:
                numeroAsientos += 1
        
        return numeroAsientos

    def verificarIntegridad(self):
        if(self.registro == self.motor.registro):
            for asiento in self.asientos:
                if type(asiento) == Asiento:
                    if asiento.registro != self.registro:
                        return "Las piezas no son originales"
            return "Auto original"
        else:
            return "Las piezas no son originales"                
                
        



        