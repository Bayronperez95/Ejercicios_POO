import cuenta
#creando objeto
cuent=cuenta.Cuenta()
cuent.setNumero('140142546212')
cuent.setFecha('1/Enero/2021')
cuent.setApertura('Solicito')
cuent.setSaldo('50.000.444')
print(f'la cuenta : {cuent.getNumero()} del {cuent.getFecha()} {cuent.getApertura()} {cuent.getSaldo()} ')
print(cuent.Retiro())
#print(Consignar(','))
print('----------------------------------------------')
print('AQUI EMPIEZA LA SUBCLASE "CUENTA CORRIENTE HIJA DE CUENTA"')
#creando objeto
cuentacorriente=cuenta.Cuentacorriente()
cuentacorriente.setApertura('Aperturo')
cuentacorriente.setFecha('12/Abril/2021')
print(f'la cuenta corriente: {cuentacorriente.getApertura()} {cuentacorriente.getFecha()}')
print(cuentacorriente.setNumerochequera(','))
print('------------------------------------')