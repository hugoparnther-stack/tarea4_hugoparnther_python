# 🚗 Sistema de Control de Velocidad Vehicular

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Estado](https://img.shields.io/badge/Estado-Completado-brightgreen?style=for-the-badge)
![UPI](https://img.shields.io/badge/Universidad-UPI%20Panamá-red?style=for-the-badge)

> **Tarea 4** · Programación I · Universidad del Panamá Internacional

---

## 📋 Descripción

Programa en Python que simula un sistema de registro y control de velocidad vehicular. El sistema solicita un límite de velocidad, registra la velocidad de cada vehículo y determina si circula dentro del límite o si debe recibir una multa. Al finalizar, genera un reporte completo.

---

## ⚙️ Funcionalidades

| Función | Descripción |
|---|---|
| 🎯 Límite de velocidad | El usuario define el límite permitido en km/h |
| 🚘 Registro de vehículos | Ingresa la velocidad de cada vehículo uno por uno |
| ⚠️ Detección de exceso | Calcula cuánto excede el límite cada infractor |
| ✅ Vehículos correctos | Identifica los que circulan dentro del límite |
| 📊 Reporte final | Muestra el total de multas emitidas |

---

## 🧠 Conceptos aplicados

```
✔ Variables
✔ Entrada de datos con input()
✔ Ciclo for
✔ Estructuras if - else
✔ Operadores aritméticos
✔ Operadores de comparación
```

---

## ▶️ Ejemplo de ejecución

```
==================================================
  SISTEMA DE CONTROL DE VELOCIDAD VEHICULAR
==================================================

Ingrese el límite de velocidad permitido (km/h): 80
Ingrese la cantidad de vehículos a registrar: 3

--------------------------------------------------
  REGISTRO DE VEHÍCULOS
--------------------------------------------------

Vehículo #1 - Ingrese su velocidad (km/h): 75
  ✔  El vehículo #1 circula dentro del límite permitido.

Vehículo #2 - Ingrese su velocidad (km/h): 110
  ⚠  MULTA: El vehículo #2 excede el límite en 30.0 km/h.

Vehículo #3 - Ingrese su velocidad (km/h): 80
  ✔  El vehículo #3 circula dentro del límite permitido.

==================================================
  REPORTE FINAL
==================================================
  Límite de velocidad:    80.0 km/h
  Vehículos registrados:  3
  Total de multas:        1
  Sin infracción:         2
==================================================
```

---

## 🚀 ¿Cómo ejecutarlo?

**1.** Clona el repositorio:
```bash
git clone https://github.com/TU_USUARIO/tarea1-velocidades.git
```

**2.** Entra a la carpeta:
```bash
cd tarea1-velocidades
```

**3.** Ejecuta el programa:
```bash
python tarea4_hugoparnther.py
```

---

## 👤 Autor

**Hugo Parnther**  
Estudiante de Programación · Universidad del Panamá Internacional  

---

<p align="center">Hecho con 🐍 Python</p>
