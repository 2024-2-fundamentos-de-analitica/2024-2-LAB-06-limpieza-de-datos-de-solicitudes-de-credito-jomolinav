


def pregunta_01():

    import pandas as pd
    
    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";", index_col=0)
    df = df.copy()

    columnas = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "monto_del_credito", "línea_credito"]
    for col in columnas:
        if col in df.columns:
            df[col] = df[col].str.lower().str.strip()
            df[col] = df[col].str.replace("_", " ").str.replace("-", " ")
            df[col] = df[col].str.replace(",", "").str.replace("$", "")
            df[col] = df[col].str.replace(".00", "").str.strip()

    if "barrio" in df.columns:
        df["barrio"] = df["barrio"].str.lower()
        df["barrio"] = df["barrio"].str.replace("_", " ").str.replace("-", " ")

    if "comuna_ciudadano" in df.columns:
        df["comuna_ciudadano"] = pd.to_numeric(df["comuna_ciudadano"], errors="coerce", downcast="integer")
    if "monto_del_credito" in df.columns:
        df["monto_del_credito"] = pd.to_numeric(df["monto_del_credito"], errors="coerce")
    if "fecha_de_beneficio" in df.columns:
        df["fecha_de_beneficio"] = pd.to_datetime(
            df["fecha_de_beneficio"], format="%d/%m/%Y", errors="coerce"
        ).combine_first(
            pd.to_datetime(df["fecha_de_beneficio"], format="%Y/%m/%d", errors="coerce")
        )

    df = df.drop_duplicates()
    df = df.dropna()
    output_path = "files/output/solicitudes_de_credito.csv"
    df.to_csv(output_path, sep=";",index=False)
