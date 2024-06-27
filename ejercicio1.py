from datetime import datetime, timedelta

class Fecha:
    def __init__(self, dia=None, mes=None, year=None):
        if dia is None or mes is None or year is None:
            fecha_actual= datetime.date.today()
            self.dia = fecha_actual.day
            self.mes = fecha_actual.month
            self.year = fecha_actual.year
        else: 
            self.dia = dia
            self.mes = mes
            self.year = year

    def calcular_dif_fecha(self, otra_fecha):
        fecha_inicial = datetime.date(self.year, self.mes, self.dia)
        fecha_final = datetime.date(otra_fecha.year, otra_fecha.mes, otra_fecha.dia)
        diferencia = fecha_final - fecha_inicial
        return diferencia

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.year:04d}"
    
    def __add__(self, otra_fecha):
        nueva_fecha = date(self.year,self.mes,self.dia) + timedelta (days=days)
        return Fecha (nueva_fecha.dia, nueva_fecha.mes, nueva_fecha.year)

    def __eq__(self,otra_fecha):
        return (self.dia == otra_fecha.dia and
                self.mes == otra_fecha.mes and
                self.year == otra_fecha.year)



