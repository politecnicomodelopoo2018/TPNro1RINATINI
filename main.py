from sistema import Sistema

ElSistema = Sistema()

ElSistema.cargar_archivos('datos.json')


print('Punto 1')
for item in ElSistema.listaVuelos:
    print('Vuelo: '+ str(item.fecha) + ' ' + item.hora + ' ' + 'desde ' + item.origen + ' hasta ' + item.destino )
    for item2 in item.getPasajeros():
        print(item2.nombre + ' ' + item2.apellido)
    print('\n')

print('Punto 2')
for item in ElSistema.listaVuelos:
    print('Vuelo: ' + str(item.fecha) + ' ' + item.hora + ' ' + 'desde ' + item.origen + ' hasta ' + item.destino)
    print(item.PasajeroMasJovenPorVuelo())

print('Punto 3')
print(ElSistema.VuelosQueNoAlcanzenLaTripMinima())

print('Punto 4')
for item in ElSistema.VuelosConTripulantesNoAutorizados():
    print(item)

print('Punto 5')
for item in ElSistema.TripulantesQueVolaronMasDeUnaVezAlDia():
    print(item)

print('Punto 6')
for item in ElSistema.listaVuelos:
    print('Vuelo: ' + str(item.fecha) + ' ' + item.hora + ' ' + 'desde ' + item.origen + ' hasta ' + item.destino)
    print(item.PasajerosVipOEspeciales())

print('Punto 7')
for item in ElSistema.listaVuelos:
    print('Vuelo: ' + str(item.fecha) + ' ' + item.hora + ' ' + 'desde ' + item.origen + ' hasta ' + item.destino)
    print(item.IdiomasPorVuelo())