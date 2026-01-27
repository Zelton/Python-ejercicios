# F-string
nombre = "Adrián"
age = 31
musica = "rock"
ciudad = "Salamanca"
mascota1 = "Kiara"
mascota2 = "Arai"
sueldo = "1445"

print(f"Hola, me llamo {nombre}, en 4 años tendré {age + 4}\n"
f"Vivo en {ciudad} y me encanta escuchar {musica}\n"
f"Tengo dos mascotas {mascota1} y {mascota2}\n"
f"Mi salario hace unos meses era {int(sueldo) -100}")

# F-strings y funcion input()

print(f"Hola,¿cómo te llamas?")
nombre = input()
print(f"Encantado de concoerte {nombre}\n"
f"Acabas de entrar en TrainLeveling\n"
f"Se te pondrá a prueba diariamente.\n"
f"Pero antes debo saber tu edad, ¿cuántos años tienes?")
edad = input()
print(f"Bienvenido a tu camino hacia la cima.")