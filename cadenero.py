from pyemenu import Menu, Form, Title

def main():
    options = ["Azimuth a Rumbo", 
                "Rumbo a Azimuth",
                "Coordenadas Finales"
                ]

    start_menu = Menu(options, title=Title("Cadenero Inicio"))
    start_menu.print()

if __name__ == "__main__":
    main()