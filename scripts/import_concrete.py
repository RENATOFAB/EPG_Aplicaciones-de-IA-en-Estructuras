#!/usr/bin/env python3
import sys
import os
import glob
import pandas as pd
from sqlalchemy import create_engine


def find_file(name=None):
    if name and os.path.exists(name):
        return name
    candidates = glob.glob('**/*.xls', recursive=True)
    if not candidates:
        return None
    if name:
        for c in candidates:
            if os.path.basename(c).lower() == name.lower():
                return c
    return candidates[0]


def main():
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    fname = find_file(arg)
    if not fname:
        print('No se encontró ningún archivo .xls en el workspace.')
        sys.exit(1)
    print('Usando archivo:', fname)

    # Cargar con pandas (motor xlrd para .xls)
    df = pd.read_excel(fname, engine='xlrd')
    print('Filas, columnas:', df.shape)
    print(df.head().to_string())

    # Guardar en SQLite
    os.makedirs('data', exist_ok=True)
    engine = create_engine('sqlite:///data/concrete_data.db')
    df.to_sql('concrete', engine, if_exists='replace', index=False)
    print("Importado a data/concrete_data.db en la tabla 'concrete'.")


if __name__ == '__main__':
    main()
