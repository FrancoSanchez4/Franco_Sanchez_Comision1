#defino funcion para los datos del paciente
def imprimirDatosPaciente(NombreCompleto, FechaDeNacimiento):
    print("Paciente:")
    print(NombreCompleto)
    print(FechaDeNacimiento)

#defino funcion para detalles del medicamento
def imprimirDetallesMedicamentos(NombreMedicamento, Dosis, InstruccionesDeUso):
    print("Medicación:")
    print(NombreMedicamento)
    print(Dosis)
    print(InstruccionesDeUso)

def imprimirSiguienteTurno(Fecha):
    print("Proxima turno")
    print(Fecha)

#entrada de datos
NombreCompleto = input("Ingrese nombre completo del paciente: ")
FechaDeNacimiento = input("Ingrese fecha de nacimiento del paciente: ")
NombreMedicamento = input("Ingrse nombre del medicamento: ")
Dosis = input("Ingrese dosis del medicamento: ")
InstruccionesDeUso = input("Ingrese Instrucciones de uso: ")
Fecha = input("Ingrese fecha de la próxima consulta: ")
print("Clinica Mayo")
print("25 de Mayo 1816, Villa María, Córdoba, Argentina")
imprimirDatosPaciente(NombreCompleto, FechaDeNacimiento)
imprimirDetallesMedicamentos(NombreMedicamento, Dosis, InstruccionesDeUso)
imprimirSiguienteTurno(Fecha)
