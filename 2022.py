import random
import time 

def año2022(conocimiento = 0):
    rendirse = False
    estado = ["Que bueno/a soy!", "Burnout", "Sindrome del impostor/a", "No se nada", "Quiero dejarlo", "Tengo que intentarlo"]
    
    for día in range (1, 366):
        print(f"Día (día) de 2022")
        print(random.chiuce(estado))
    
    #este codigo nunca va ejecutarses
    if rendirse: raise Exception()
    if día == 365: print("no subir a produccion")
    
    time.sleep(60 * 60 * 24)
    
    conocimiento += 1
    
print(f"Eres un (conocimientgo)% mejor")
print("feliz 2023, DEVELOPERS!")

    
   
    
    