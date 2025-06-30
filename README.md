# Proyecto DataOps – ETL Automatizado

Este proyecto implementa un pipeline ETL automatizado como parte de un ejercicio académico en el diplomado de Ingeniería de Datos. El flujo extrae datos desde una base de datos PostgreSQL, aplica transformaciones con Python y exporta los resultados en formato CSV. Todo el proceso está empaquetado en Docker y preparado para ejecutarse mediante Jenkins en un flujo CI/CD.

## Estructura del proyecto

```
dataops-rrhh/
├── etl/
│   ├── main.py              # Script ETL principal
│   ├── requirements.txt     # Dependencias de Python
├── output/                  # Carpeta para archivos exportados (.csv)
├── Dockerfile               # Imagen Docker para ejecutar el ETL
├── instalacionDocker.sh     # Script de instalación de Docker y herramientas
├── docker-compose.yml       # Levanta Jenkins como contenedor
├── docs/                    # Documentación técnica y capturas
└── README.md                # Este archivo
```

## Instrucciones de uso

### 1. Ejecutar localmente

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r etl/requirements.txt
python etl/main.py
```

### 2. Ejecutar con Docker

```bash
docker build -t etl-job .
docker run --rm -v "$(pwd)/output:/app/output" etl-job
```

**Nota para Git Bash en Windows:** si hay espacios en la ruta, usar:

```bash
winpty docker run --rm -v "$(pwd)/output:/app/output" etl-job
```

### 3. Desplegar Jenkins en una VM

El archivo `instalacionDocker.sh` automatiza la instalación de Docker, Java y Git en una máquina virtual Linux. Una vez ejecutado, se puede iniciar Jenkins con:

```bash
docker-compose up -d
```

Esto levanta Jenkins en el puerto 80 de la VM. Desde la interfaz web, se configuró un pipeline manual que:

- Clona este repositorio
- Construye la imagen Docker
- Ejecuta el contenedor con el ETL

Este procedimiento replica lo realizado en clase y no requiere un Jenkinsfile en el repositorio.

## Requisitos

- Python 3.10+ (localmente se usó 3.13.2)
- Docker
- Jenkins (opcional, para CI/CD)
- Acceso a base de datos PostgreSQL (credenciales provistas por el diplomado)

## Licencia

Este proyecto es de uso académico y no debe utilizarse en producción sin validación adicional.
