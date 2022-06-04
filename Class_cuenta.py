class Cuenta:
    """
    numero
    fecha
    apertura
    saldo
    """

#metodo constructor
    def init(self,numero,fecha,apertura,saldo):
        self.numero=numero
        self.fecha=fecha
        self.apertura=apertura
        self.saldo=saldo

#Metodo setter
    def setNumero(self,numero):
        self.numero=numero
    def setFecha(self,fecha):
        self.fecha=fecha
    def setApertura(self,apertura):
        self.apertura=apertura
    def setSaldo(self,saldo):
        self.saldo=saldo

#Metodo getter
    def getNumero(self):
        return self.numero
    def getFecha(self):
        return self.fecha
    def getApertura(self):
        return self.apertura
    def getSaldo(self):
        return self.saldo

#Metodo Retiro
    def Retiro(self):
        while True:
            self.retiro=int(input('Digite el valor a retirar: '))
            if self.retiro>0 and self.retiro<=self.saldo:
                self.saldo-=self.retiro
                return f'Retiro exitoso {self.saldo}'
            else:
                print(f'Cantidad insuficiente saldo disponible {self.saldo}')
                continue

#Metodo Consignar
    def Consignar(self,valor):
        self.saldo+=valor
        return (self,valor)
    """def obtenerInformacion(self):
        info='Informacion de la Cuenta'
        info+='\n numero: '+str(self.getNumero())
        info+='\n fecha: '+str(self.getFecha())
        info+='\n apertura: '+self.getApertura()
        info+='\n saldo: '+str(self.getSaldo())"""

#implementar la herencia, creo la clase cuenta corriente "Hereda de la clase cuenta"
class Cuentacorriente(Cuenta):
    """
    numerochequera
    """

#Metodo constructor de la hija
    def init(self):
        super().init()
        self.numerochequera='17898'
    #metodo getter
    def getNumerochequera(self):
        return self.numerochequera
    #metodo setter
    def setNumerochequera(self,numerochequera):
        self.numerochequera=numerochequera 