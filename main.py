import time
kilosRopa = 20
jabonPolvo = 1
jabonPasta = 1
cloro = 0.25
litosAgua = 20
lavadora = 1
mecate = 1
nublado = False

def separarRopa():
  print("separando ropa de color y blanca")


def tender():
  if (nublado):
    print("por el momento no se puede tender la ropa")
  else:
    print ("La ropa ha sido tendida")


def sacarDeLavadora():
  print("sacando la ropa de la lavadora")

def esperarCiclo():
  print("esperando a que termine el ciclo")
  time.sleep(3)
  print("el ciclo ha terminado")
  

def echarRopa():
  print("Echar la ropa a la lavadora")

def encenderLavadora():
  print("Encender la lavadora y esperar el agua a la mitad")



separarRopa()
echarRopa()
encenderLavadora()
esperarCiclo()
sacarDeLavadora()
tender()

