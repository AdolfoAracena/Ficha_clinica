class Patient():
    ##Atributo##
    name='' #Nombre
    dni='' #Dni
    weight=0 #Peso
    sex='' #Sexo
    direction='' #Direccion
    height=0 #Altura
    occupation='' #Occupation
    forescast='' #Prevision
    blood_group='' #Grupo sanguineo
    day='' #Dia nacimiento
    month='' #Mes nacimiento
    year='' #Año nacimiento
    cell_phone='' #Celular
    e_mail='' #E-mail
    marital_status='' #Estado civil
    morbid_background='' #Antecedentes morbidos
    previous_diagnosis='' #Diagnostico previos
    chronic_diseases='' #Enfermedades cronicas

    ##Fin atributo##


    def __init__(self,name,dni,weight,sex,direction,height,occupation,forescast,blood_group,day,month,year,cell_phone,e_mail,marital_status,morbid_background,previous_diagnosis,chronic_diseases):
        self.name=name
        self.dni=dni
        self.weight=weight
        self.sex=sex
        self.direction=direction
        self.height=height
        self.occupation=occupation
        self.forescast=forescast
        self.blood_group=blood_group
        self.day=day
        self.month=month
        self.year=year
        self.cell_phone=cell_phone
        self.e_mail=e_mail
        self.marital_status=marital_status
        self.morbid_background=morbid_background
        self.previous_diagnosis=previous_diagnosis
        self.chronic_diseases=chronic_diseases
    
    def print(self):
        print("--------Paciente--------")
        print("Nombre paciente:")
        print(self.name)
        print("Dni:")
        print(self.dni)
        print("Peso:")
        print(self.weight)
        print("Sexo:")
        print(self.sex)
        print("Direccion:")
        print(self.direction)
        print("Altura:")
        print(self.height)
        print("Ocupacion:")
        print(self.occupation)
        print("Prevision:")
        print(self.forescast)
        print("Grupo sanguineo:")
        print(self.blood_group)
        print("Fecha nacimiento:")
        print(self.day,"/",self.month,"/",year)
        print("Celular:")
        print("(+569)",self.cell_phone)
        print("e-mail:")
        print(self.e_mail)
        print("Estado civil:")
        print(self.marital_status)
        print("Antecedentes morbidos:")
        print(self.morbid_background)
        print("Diagnostico previos:")
        print(self.previous_diagnosis)
        print("Enfermedades cronicas:")
        print(self.chronic_diseases) 


print("Ingrese el nombre del paciente:")
name=(input())

print("Ingrese el Dni (sin punto ni guion):")
dni=int(input())

print("Ingrese el peso:")
weight=int(input())

print("Sexo: 1 (Masculino) o 2(Femenino)")
sex=int(input())

print("Direccion:")
direction=(input())

print("Altura:")
height=int(input())

print("Ocupacion:")
occupation=(input())

print("Prevision:")
forescast=(input())

print("Grupo sanguineo:")
blood_group=(input())

print("Fecha nacimiento")
print("Dia:")
day=int(input())
if(day>=31):
    print("Debe ingresar bien el dia")
    exit()
print("Mes:")
month=int(input())
if(month>=13):
    print("Debe ingresar bien el mes")
    exit()
print("Año:")
year=int(input())
if(year<=1900):
    print("Debe ingresar bien el año")
    exit()

print("Celular: (+569)")
cell_phone=int(input())
if(cell_phone<9999999):
    print("Debe ingresar bien el celular")
    exit()

print("E-mail:")
e_mail=(input())

print("Estado civil:")
marital_status=(input())

print("Antecendentes morbidos:")
morbid_background=(input())

print("Diagnostico previos:")
previous_diagnosis=(input())

print("Enfermedades cronicas:")
chronic_diseases=(input())

patient=Patient(name,dni,weight,sex,direction,height,occupation,forescast,blood_group,day,month,year,cell_phone,e_mail,marital_status,morbid_background,previous_diagnosis,chronic_diseases)

patient.print()