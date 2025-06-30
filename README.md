# Proyecto ETL con Docker y Jenkins (DataOps)

Este proyecto implementa un flujo ETL utilizando Python, PostgreSQL, Docker y Jenkins como parte de una práctica del diplomado de Ingeniería de Datos. El proceso sigue los principios de DataOps, incorporando automatización, trazabilidad y despliegue controlado.

---

## Estructura del Proyecto


dataops-rrhh/
│
├── etl/                    # Contiene el script ETL (main.py) y el requirements.txt
├── output/                 # Archivos CSV generados por el ETL
├── docs/                   # Documentación del proyecto
├── .gitignore              # Archivos a excluir del control de versiones
├── Dockerfile              # Imagen Docker para ejecutar el ETL
├── instalacionDocker.sh    # Script para preparar entorno en la VM
├── docker-compose.yml      # Define el contenedor Jenkins
└── README.md               # Este archivo


---

## Tecnologías utilizadas

- *Python 3.13.2*  
- *Pandas, SQLAlchemy, Psycopg2*  
- *Docker Desktop (local)*  
- *PostgreSQL (remoto)*  
- *Jenkins (en VM Ubuntu con Docker)*  
- *Git + GitHub*

---

## Instrucciones de ejecución local (opcional)

1. Clonar el repositorio:

bash
git clone https://github.com/tu-usuario/dataops-rrhh.git
cd dataops-rrhh


2. Crear entorno virtual:

bash
python -m venv venv
source venv/Scripts/activate  # En Windows


3. Instalar dependencias:

bash
pip install -r etl/requirements.txt


4. Ejecutar el ETL localmente:

bash
python etl/main.py


---

## Ejecutar con Docker

bash
docker build -t etl-job .
docker run --rm -v "$PWD/output:/app/output" etl-job


*Si usas Git Bash y tienes rutas con espacios, usa winpty*:

bash
winpty docker run --rm -v "$PWD/output:/app/output" etl-job


---

## Automatización CI/CD con Jenkins

- Jenkins fue desplegado en una VM Ubuntu mediante Docker
- Se configuró un *proyecto libre*, sin Jenkinsfile
- El pipeline realiza:
  1. Clonación del repositorio
  2. Construcción de la imagen etl-job
  3. Ejecución del contenedor que genera el archivo .csv
- Se habilitó un *webhook de GitHub* para disparar el pipeline automáticamente ante cada push

---

## Documentación

La documentación completa se encuentra en la carpeta docs/ e incluye:

- Descripción del flujo ETL
- Estructura del proyecto
- Evidencia del pipeline funcionando
- Configuración del entorno

---

## 🙌 Autor

*Joaquin Ruiz Ramal*  