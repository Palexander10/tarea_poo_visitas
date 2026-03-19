# 🏢 Sistema de Registro de Visitantes

Aplicación de escritorio desarrollada en **Python + Tkinter** que implementa un CRUD completo para registrar y gestionar visitantes en una oficina, aplicando **Arquitectura Modular por Capas** y principios de **Programación Orientada a Objetos**.

---

## 📋 Características

| Funcionalidad | Descripción |
|---|---|
| ✅ Registrar visitante | Valida campos, verifica cédula única y persiste en memoria |
| 📋 Listar visitantes | Tabla dinámica (`ttk.Treeview`) con filas alternas |
| ❌ Eliminar visitante | Elimina el registro seleccionado con confirmación |
| 🔄 Limpiar formulario | Resetea los campos a su estado inicial |

---

## 🗂️ Arquitectura del Proyecto

```
visitas_app/
│
├── main.py                   # Punto de entrada — orquesta las capas
│
├── modelos/
│   ├── __init__.py
│   └── visitante.py          # Data Class con propiedades encapsuladas
│
├── servicios/
│   ├── __init__.py
│   └── visita_servicio.py    # Lógica CRUD — cerebro del sistema
│
└── ui/
    ├── __init__.py
    └── app_tkinter.py        # Interfaz gráfica — solo presenta datos
```

### Principios aplicados
- **POO**: Clases, constructores `__init__`, métodos y propiedades.
- **Encapsulamiento**: La lista de visitantes es privada (`_visitantes`) en el servicio.
- **Inyección de Dependencias**: `AppTkinter` recibe `VisitaServicio` en su constructor.
- **Separación de Responsabilidades**: La UI no contiene lógica de negocio.

---

## ⚙️ Requisitos

- **Python 3.10** o superior (se usa `X | Y` type hints).
- **Tkinter** incluido en la instalación estándar de Python.
- Sin dependencias externas — solo biblioteca estándar.

---

## 🚀 Cómo ejecutar

### 1. Clonar el repositorio
```bash
git clone https://github.com/<tu-usuario>/tarea_poo_visitas.git
cd tarea_poo_visitas
```

### 2. Verificar Python
```bash
python --version   # debe ser 3.10+
```

### 3. Ejecutar la aplicación
```bash
python main.py
```

> **Nota para Windows:** si `python` no funciona, usa `py main.py`.

### Abrir en Visual Studio Code
```bash
code .
```
Luego presiona **F5** o ejecuta la tarea `Run Python File` con `main.py` abierto.

---

## 🖥️ Uso de la aplicación

1. **Completar** los campos Cédula, Nombre y Motivo.
2. **Clic en "Registrar Visitante"** → aparece en la tabla.
3. **Seleccionar una fila** de la tabla y clic en **"Eliminar Seleccionado"**.
4. **"Limpiar Campos"** resetea el formulario en cualquier momento.

---

## 👩‍💻 Autor

Por: Pablo Alexander Ramón Mosquera

