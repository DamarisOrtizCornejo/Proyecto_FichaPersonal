class Opciones:
    def __init__(self):
        pass

    def genero(self):
        GENERO= (('M', 'Masculino'),('F', 'Femenino'),)
        return GENERO

    def estado_civil(self):
        ESTADO_CIVIL = (('S','Soltero(a)'),('C','Casado(a)'),('D','Divorciado(a)'),
            ('V', 'Viudo(a)'),('U','Union Libre'),
        )
        return ESTADO_CIVIL

    def tipo_contrato(self):
        TIPO_CONTRATO = (('CI','Contrato indefinido'),('CT','Contarto temporal'),('CP','Contrato en prácticas'),
        )
        return TIPO_CONTRATO

    def tipo_sangre(self):
        TIPO_SANGRE = (('1','A+'),('2','A-'),('3','B+'),('4','B-'),('5','O+'),('6','0-'),('7','AB+'),('8','AB-'),
        )
        return TIPO_SANGRE

    def parentesco(self):
        PARENTESCO = (('M','Madre'),('P','Padre'),('H','Hermano(a)'),('A','Abuelo(a)'),('T','Tio(a)'),('Pr','Primo(a)'),('S','Sobrino(a)'),('C','Cuñado(a)'),('Pd','Padrastro'),('Md','Madrastra'),('Co','Conyuge'),('Hi','Hijo(a)'),('O','Otros'),
        )
        return PARENTESCO

