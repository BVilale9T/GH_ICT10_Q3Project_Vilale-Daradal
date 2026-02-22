from pyscript import display, document

# List of student names
students = [
    "Alejandro Enriquez",
    "ALLEN DARADAL",
    "BEA VILALE",
    "CALEB ARIAS",
    "Calvin Garcia",
    "CARL JOSEPH RUFO",
    "DERYCK TAN",
    "HARMONY GAIL YAO",
    "IVY ZOSA",
    "JALAINIE ABDULLAH",
    "KHLOE ESPINA",
    "Leona Abeleda",
    "Lord Cedric Friedrich Bonzon",
    "MARTINA CAJUCOM",
    "MIGUEL JOAQUIN SANCHEZ",
    "Phoebe Shanelle Catimbang",
    "Prince Akishino Gano",
    "RAMON SANTOS",
    "RENZO ISAAC ARCE",
    "Sang-heon Choi",
    "Sean Matthew Cotioco",
    "Sebastian Chilli Gyrvan Ong",
    "SIMRANDIP KAUR",
    "SKYLER ESCOBAR"
]

def show_stud(e):
    # Clears previous output
    document.getElementById("output").innerHTML = ""

    # Loops through the list and displays each student name
    for x in students:
        display(x, target="output")