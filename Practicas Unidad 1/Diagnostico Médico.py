import random
import tkinter as tk
from datetime import datetime, timedelta

# ============================================================
# LÓGICA DEL SISTEMA MÉDICO (con proposiciones)
# ============================================================

def generar_diagnostico():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    peso = entry_peso.get()
    estatura = entry_estatura.get()
    oxigenacion = int(entry_oxigenacion.get())
    frecuencia_cardiaca = int(entry_fc.get())
    temperatura = float(entry_temp.get())

    fiebre = var_fiebre.get()
    tos = var_tos.get()
    dolor = var_dolor.get()

    # ----------------------------------------------------------
    # PROPOSICIONES
    # ----------------------------------------------------------

    # P: la oxigenación es baja
    P = oxigenacion >= 90

    # Q: la frecuencia cardiaca es anormal (muy alta o muy baja)
    Q = frecuencia_cardiaca > 130 or frecuencia_cardiaca < 40

    # R: la temperatura es muy alta
    R = temperatura >= 39.5

    # S: el paciente tiene al menos un síntoma
    S = fiebre or tos or dolor

    # ----------------------------------------------------------
    # DISYUNCIÓN: URGENCIA = P ∨ Q ∨ R
    # ----------------------------------------------------------

    urgencia = P or Q or R

    # ----------------------------------------------------------
    # DIAGNÓSTICO (según síntomas)
    # ----------------------------------------------------------

    if fiebre and tos:
        diagnostico = "Posible infección respiratoria"
    elif tos and dolor:
        diagnostico = "Posible irritación respiratoria"
    elif fiebre:
        diagnostico = "Se recomienda valoración profesional"
    else:
        diagnostico = "No se identificó un patrón claro"

    # ----------------------------------------------------------
    # ESTADO FINAL: urgencia -> cita con doctor -> está bien
    # ----------------------------------------------------------

    if urgencia:
        estado = "URGENCIA: acude al área de Urgencias de inmediato."
        necesita_cita = False

    elif S:
        estado = "Necesitas valoración médica, se te asignará un doctor."
        necesita_cita = True

    else:
        estado = "Estás bien, no es necesario ir con un doctor."
        necesita_cita = False
        diagnostico = "Sin hallazgos, paciente sano"

    # ----------------------------------------------------------
    # CITA (solo si necesita_cita = True)
    # ----------------------------------------------------------

    if necesita_cita:
        doctores = ["Dr. Ramírez", "Dra. López", "Dr. Hernández", "Dra. Torres"]
        doctor_asignado = random.choice(doctores)

        dias_espera = random.randint(1, 7)
        hora_cita = random.randint(8, 17)

        fecha_cita = datetime.now() + timedelta(days=dias_espera)
        fecha_cita_str = fecha_cita.strftime("%d/%m/%Y")

    # ----------------------------------------------------------
    # RESULTADO
    # ----------------------------------------------------------

    resultado = (
        f"Hola {nombre}, este es tu diagnóstico:\n\n"
        f"Edad          : {edad} años\n"
        f"Peso          : {peso} kg\n"
        f"Estatura      : {estatura} cm\n"
        f"Oxigenación   : {oxigenacion}%\n"
        f"Frec. cardiaca: {frecuencia_cardiaca} lpm\n"
        f"Temperatura   : {temperatura} °C\n\n"
        f"Diagnóstico   : {diagnostico}\n"
        f"Estado        : {estado}\n"
    )

    if necesita_cita:
        resultado += f"Cita asignada : con {doctor_asignado} el {fecha_cita_str} a las {hora_cita}:00 hrs"

    texto_resultado.config(state="normal")
    texto_resultado.delete("1.0", tk.END)
    texto_resultado.insert(tk.END, resultado)
    texto_resultado.config(state="disabled")


# ============================================================
# INTERFAZ GRÁFICA (tkinter)
# ============================================================

ventana = tk.Tk()
ventana.title("Sistema de Diagnóstico Médico")
ventana.geometry("380x630")

tk.Label(ventana, text="SISTEMA DE DIAGNÓSTICO MÉDICO", font=("Arial", 13, "bold")).pack(pady=10)

tk.Label(ventana, text="Nombre:").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Edad:").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Peso (kg):").pack()
entry_peso = tk.Entry(ventana)
entry_peso.pack()

tk.Label(ventana, text="Estatura (cm):").pack()
entry_estatura = tk.Entry(ventana)
entry_estatura.pack()

tk.Label(ventana, text="Oxigenación (SpO2 %):").pack()
entry_oxigenacion = tk.Entry(ventana)
entry_oxigenacion.pack()

tk.Label(ventana, text="Frecuencia cardiaca (lpm):").pack()
entry_fc = tk.Entry(ventana)
entry_fc.pack()

tk.Label(ventana, text="Temperatura (°C):").pack()
entry_temp = tk.Entry(ventana)
entry_temp.pack()

tk.Label(ventana, text="Síntomas:").pack(pady=(10, 0))

var_fiebre = tk.BooleanVar()
var_tos = tk.BooleanVar()
var_dolor = tk.BooleanVar()

tk.Checkbutton(ventana, text="Fiebre", variable=var_fiebre).pack()
tk.Checkbutton(ventana, text="Tos", variable=var_tos).pack()
tk.Checkbutton(ventana, text="Dolor de garganta", variable=var_dolor).pack()

tk.Button(ventana, text="Generar diagnóstico", command=generar_diagnostico).pack(pady=10)

texto_resultado = tk.Text(ventana, height=11, width=42, state="disabled")
texto_resultado.pack(pady=10)

ventana.mainloop()