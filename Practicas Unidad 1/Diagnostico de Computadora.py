print("=" * 55)
print("     SISTEMA DE DIAGNÓSTICO DE COMPUTADORA")
print("=" * 55)
print("Te haré varias preguntas sobre electricidad, encendido,")
print("imagen y comportamiento del sistema para dar un")
print("diagnóstico más completo y una recomendación clara.\n")

nombre = input("¿Cuál es tu nombre? ")

diagnostico = causa = recomendacion = ""

electricidad = input("¿El equipo tiene electricidad? (s/n): ").strip().lower() in ("s", "si")

if not electricidad:
    diagnostico = "Falla en el suministro eléctrico"
    causa = "El contacto, cable o regulador no está pasando corriente."
    recomendacion = "Contacta a Mantenimiento Eléctrico - 722 228 4515. No sigas intentando encenderlo."

else:
    enciende = input("¿Enciende? (s/n): ").strip().lower() in ("s", "si")

    if not enciende:
        ruido = input("¿Escuchas algún clic, zumbido o pitido al encender? (s/n): ").strip().lower() in ("s", "si")
        quemado = input("¿Hay olor a quemado o humo? (s/n): ").strip().lower() in ("s", "si")

        diagnostico = "Falla en la fuente de poder o la placa base"
        causa = "El equipo no responde al botón de encendido"
        if ruido:
            causa += ", y el ruido detectado apunta a un componente que intenta arrancar sin lograrlo"
        causa += "."

        if quemado:
            diagnostico = "Posible daño eléctrico severo"
            recomendacion = "¡No lo enciendas de nuevo! Contacta a Mantenimiento Eléctrico de inmediato - 729 855 9514"
        else:
            recomendacion = "manda el equipo con Soporte Técnico de Hardware."

    else:
        imagen = input("¿Muestra imagen? (s/n): ").strip().lower() in ("s", "si")

        if not imagen:
            standby = input("¿El monitor tiene alguna luz de espera encendida? (s/n): ").strip().lower() in ("s", "si")
            pitidos = input("¿Escuchas pitidos (beeps) repetitivos al encender? (s/n): ").strip().lower() in ("s", "si")

            diagnostico = "falla de video, memoria RAM o conexión del monitor"
            causa = "el equipo enciende pero no llega imagen al monitor"
            if not standby:
                causa += "; el monitor no da señal de espera, revisa el cable de video"
            else:
                causa += "; el monitor está en espera pero sin señal, revisa la tarjeta de video o la RAM"
            if pitidos:
                causa += " (los pitidos son un código de error útil para soporte)"
            causa += "."
            recomendacion = "manda el equipo con Soporte Técnico de Hardware o llama al 855 947 5569"

        else:
            carga_so = input("¿El sistema operativo carga bien hasta el escritorio? (s/n): ").strip().lower() in ("s", "si")

            if not carga_so:
                diagnostico = "falla de arranque del sistema operativo o del disco"
                causa = "puede ser un disco dañado, archivos de sistema corruptos o una actualización fallida."
                recomendacion = "manda el equipo con Soporte Técnico de Software o llama al 729 685 7512"

            else:
                lento = input("¿Notas lentitud extrema o congelamientos frecuentes? (s/n): ").strip().lower() in ("s", "si")
                ruido_disco = input("¿Escuchas ruidos extraños del disco duro? (s/n): ").strip().lower() in ("s", "si")
                calor = input("¿El equipo se siente muy caliente o los ventiladores hacen mucho ruido? (s/n): ").strip().lower() in ("s", "si")
                pantallazos = input("¿Has tenido pantallas azules o reinicios inesperados? (s/n): ").strip().lower() in ("s", "si")

                if not any([lento, ruido_disco, calor, pantallazos]):
                    diagnostico = "funcionamiento correcto"
                    causa = "no se detectaron señales de falla eléctrica, de hardware ni de software."
                    recomendacion = "no es necesario contactar a nadie."
                elif ruido_disco or pantallazos:
                    diagnostico = "riesgo de falla en el disco duro o inestabilidad del sistema"
                    causa = "los ruidos del disco y/o las pantallas azules suelen anticipar una falla de disco, drivers o memoria."
                    recomendacion = "respalda tu información y contacta a Soporte Técnico de Software."
                else:
                    diagnostico = "sobrecalentamiento, requiere mantenimiento preventivo"
                    causa = "el exceso de calor y ruido de ventiladores sugiere acumulación de polvo o pasta térmica degradada."
                    recomendacion = "agenda una limpieza con Mesa de Ayuda / Mantenimiento Preventivo."

print("\n" + "=" * 55)
print(f"Hola {nombre}, este es tu diagnóstico:")
print(f"  Diagnóstico    : {diagnostico}.")
print(f"  Causa probable : {causa}")
print(f"  Recomendación  : {recomendacion}")
print("=" * 55)