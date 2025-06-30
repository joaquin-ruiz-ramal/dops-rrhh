import pandas as pd
import sqlalchemy
import urllib.parse
import os
from datetime import datetime

# === Configuración de conexión ===
db_user = "usr_ro_dmc_rrhh_estudiantes"
raw_pass = "fZp!jHt0j6%89^B4I*L*29bz4b^"
db_pass = urllib.parse.quote_plus(raw_pass)
db_host = "mgg.vps.webdock.cloud"
db_port = "5432"
db_name = "dmc"
schema = "rrhh"
table = "empleado"

# === Crear engine SQLAlchemy ===
engine = sqlalchemy.create_engine(
    f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
)

# === Ejecutar consulta ===
query = f"SELECT * FROM {schema}.{table}"

try:
    df = pd.read_sql_query(query, engine)
except Exception as e:
    print("❌ Error al conectar o consultar:", e)
    exit()

# === Transformaciones ===
df["tip_documento"] = df["tip_documento"].str.upper()
df["nom_empleado"] = df["nom_empleado"].str.title()
df["ape_empleado"] = df["ape_empleado"].str.title()
df["nom_empleado_completo"] = df["nom_empleado"] + " " + df["ape_empleado"]
df["mnt_tope_comision"] = df["mnt_tope_comision"].fillna(0)
df["salario_anual"] = round(df["mnt_salario"] * 12, 2)

# === Definir ruta de salida segura ===
try:
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Para .py
except NameError:
    base_dir = os.getcwd()  # Por si lo corres en notebook (fallback)

output_dir = "/app/output"
os.makedirs(output_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = os.path.join(output_dir, f"empleados_transformados_{timestamp}.csv")

# === Exportar resultado ===
try:
    df.to_csv(output_file, index=False, encoding="utf-8-sig")
    print(f"✅ Archivo exportado correctamente en: {output_file}")
except Exception as e:
    print(f"❌ Error al exportar el archivo: {e}")
