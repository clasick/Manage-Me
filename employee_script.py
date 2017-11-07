#from pas.models import Employee

import random

employee = '''Ela Christon
Sebastian Pennington
Migdalia Durrance
Stephane Fahnestock
Carl Goulding
Marielle Eisenhower
Corine Fennel
Tammi Darity
Antonio Galban
Yolando Hilliker
Emmett Slape
Lorriane Pimentel
Teddy Melrose
Tommy Payan
Gisele Nardi
Tijuana Harder
Carri Simard
Luba Cottrell
Dede Dilley
Rich Valla
Nathanial Nocera
Salley Sampson
Aleta Wyche
Alejandra Bertone
Holli Shattuck
Jong Beaton
Alisia Encinas
Stewart Fregoso
Sacha Lytch
Caroline Cool
Leland Shaddix
Marcia Hiney
Roselia Hix
Sheryll Dominguez
Suanne Loftin
Weldon Boehm
Leandra Jaso
Kaye Zachery
Fatima Tullius
Sindy Watkins
Justina Nolette
Annette Severt
Cliff Lakin
Drema Blubaugh
Lee Reynold
Marhta Crosland
Granville Reaves
Na Shealey
Veda Beaston
Lucila Schall'''

print(employee.split('\n'))


s = string.digits

''.join(random.sample(s,10))

DESIGNATION = ['Developer', 'Designer', 'Debugger', 'Tester', 'Documenter']




 phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number is invalid. Enter up to 10 digits.")
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    designation = models.CharField(max_length=10, null=True)
    leader = models.BooleanField()
    join_date = models.DateField()
    department = models.ForeignKey(Department, null=True)
    panel = models.ForeignKey(Panel, null=True, blank=True, on_delete=models.SET_NULL)