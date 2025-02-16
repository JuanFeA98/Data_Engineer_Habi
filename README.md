# 🚀 Proyecto de Procesamiento de Datos

Este proyecto realiza la extracción, limpieza y carga de datos en una base de datos utilizando Python y Docker.

---

## 📌 Estructura del Proyecto

```
/DE_HABI
│── /Config
│   ├── config.yml
│── /Data
│   ├── /Final
│   ├── /Processed
│   ├── /Raw
│── /src
│   ├── read_data.py
│   ├── clean_data.py
│   ├── load_records.py
│── /Utils
│   ├── functions.py
│   ├── consultas_mysql.py
│── /SQL
│   ├── /CREATE
│   │   ├── TBL_DIM_USERS.sql
│   │   ├── TBL_FCT_PROPERTIES.sql
│   ├── /INSERT
│   │   ├── TBL_DIM_USERS.sql
│   │   ├── TBL_FCT_PROPERTIES.sql
│── .dockerignore
│── .gitignore
│── requirements.txt
│── Dockerfile
│── main.py
│── README.md
```

---

## 🛠️ Requisitos Previos

Asegúrate de tener instalados:
- Python 3.12
- Docker 

Si deseas ejecutar el proyecto sin Docker, instala las dependencias manualmente:

```bash
pip install -r requirements.txt
```

---

## 🐳 Uso con Docker

### 1️⃣ **Construir la imagen**
Desde la raíz del proyecto, ejecuta:

```bash
docker build -t habi:latest .
```

### 2️⃣ **Ejecutar el contenedor**

```bash
docker run -e user="user" -e password="password" -e host="host" -e database="habi_bbdd" -e port="3306" habi:latest
```

## 🚀 Flujo de Ejecución

El proceso sigue estos pasos:
1. **Lectura de datos** con `read_data.py`
2. **Limpieza de datos** con `clean_data.py`
3. **Carga de datos** en la base de datos con `load_records.py`

El punto de entrada es `main.py`, que coordina toda la ejecución.

---

## 📝 Notas Adicionales
- Modifica `config.ini` si necesitas cambiar configuraciones.
- Asegúrate de tener los archivos SQL necesarios en `/SQL/INSERT/` y `/SQL/CREATE/`.

---

¡Listo! Con estos pasos, se puede ejecutar el pipeline de datos en Docker. 🚀
