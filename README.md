# Proyecto DataOps – ETL Automatizado

Este proyecto implementa un pipeline ETL automatizado como parte de un ejercicio académico en el diplomado de Ingeniería de Datos. El flujo extrae datos desde una base de datos PostgreSQL, aplica transformaciones con Python y exporta los resultados en formato CSV. Todo el proceso está empaquetado en Docker y preparado para ejecutarse mediante Jenkins en un flujo CI/CD.

## 📦 Estructura del proyecto

```
dataops-rrhh/
├── etl/
│   ├── main.py              # Script ETL principal
│   ├── requirements.txt     # Dependencias de Python
├── output/                  # Carpeta para archivos exportados (.csv)
├── Dockerfile               # Imagen Docker para empaquetar y ejecutar el ETL
├── jenkins/
│   └── Jenkinsfile          # Declaración del pipeline CI/CD
├── docs/                    # Documentación técnica y capturas
└── README.md                # Este archivo
```

## 🚀 Instrucciones de uso

### ▶️ 1. Ejecutar localmente (recomendado para desarrollo)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r etl/requirements.txt
python etl/main.py
```

### 🐳 2. Ejecutar con Docker
```bash
docker build -t etl-job .
docker run --rm -v "$(pwd)/output:/app/output" etl-job
```

> ⚠️ Si usas Git Bash en Windows y hay espacios en tu ruta, usa:
> `winpty docker run --rm -v "$(pwd)/output:/app/output" etl-job`

### 🔁 3. Ejecutar en Jenkins
El Jenkinsfile contiene las instrucciones para clonar el repositorio, construir la imagen y ejecutar el ETL automáticamente.

## ⚙️ Requisitos

- Python 3.10+ (usado localmente: 3.13.2)
- Docker
- Jenkins (para CI/CD)
- Acceso a PostgreSQL (credenciales provistas por el diplomado)

## 📄 Licencia

Este proyecto es de uso académico y no debe utilizarse en producción sin validación adicional.
