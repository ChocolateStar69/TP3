class Cancion:
    def __init__(self, titulo, nombre_disco, nombre_interprete, idioma, genero, cantidad_reproducciones):
        self.titulo = titulo
        self.disco = nombre_disco
        self.interprete = nombre_interprete
        self.idioma = idioma
        self.genero = genero
        self.reproducciones = cantidad_reproducciones


def write(registro):
    print("Titulo:", registro.titulo, "Nombre del disco:", registro.disco, "Nombre del interprete:", registro.interprete,
          "\nIdioma:", registro.idioma, "Genero:", registro.genero, "Cant. de reproducciones:", registro.reproducciones)
    print("-"*100)