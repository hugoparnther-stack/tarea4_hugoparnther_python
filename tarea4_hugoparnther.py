# ============================================================
#  Sistema de Registro de Velocidades de Vehículos
#  Tarea 4 - Estructuras repetitivas y condicionales
# ============================================================

print("=" * 50)
print("  SISTEMA DE CONTROL DE VELOCIDAD VEHICULAR")
print("=" * 50)

# --- Entrada de datos generales ---
limite = float(input("\nIngrese el límite de velocidad permitido (km/h): "))
cantidad = int(input("Ingrese la cantidad de vehículos a registrar: "))

# --- Contador de multas ---
total_multas = 0

print("\n" + "-" * 50)
print("  REGISTRO DE VEHÍCULOS")
print("-" * 50)

# --- Ciclo principal de registro ---
for i in range(1, cantidad + 1):
    velocidad = float(input(f"\nVehículo #{i} - Ingrese su velocidad (km/h): "))

    if velocidad > limite:
        exceso = velocidad - limite
        total_multas += 1
        print(f"  ⚠  MULTA: El vehículo #{i} excede el límite en {exceso:.1f} km/h.")
    else:
        print(f"  ✔  El vehículo #{i} circula dentro del límite permitido.")

# --- Reporte final ---
print("\n" + "=" * 50)
print("  REPORTE FINAL")
print("=" * 50)
print(f"  Límite de velocidad:   {limite:.1f} km/h")
print(f"  Vehículos registrados: {cantidad}")
print(f"  Total de multas:       {total_multas}")
print(f"  Sin infracción:        {cantidad - total_multas}")
print("=" * 50)
