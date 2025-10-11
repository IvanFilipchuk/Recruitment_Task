import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    if not isinstance(df, pd.DataFrame) or not isinstance(role, str) or not isinstance(new_column, str):
        return pd.DataFrame()

    label_pattern = re.compile(r'^[A-Za-z_]+$')

    if not label_pattern.match(new_column):
        return pd.DataFrame()

    for col in df.columns:
        if not label_pattern.match(col):
            return pd.DataFrame()

    role = role.strip()

    if not re.match(r'^[A-Za-z_\s+\-\*]+$', role):
        return pd.DataFrame()

    identifiers = re.findall(r'\b[A-Za-z_]+\b', role)
    for ident in identifiers:
        if ident not in df.columns:
            return pd.DataFrame()

    print(role)
    try:
        result = df.eval(role)
    except Exception:
        return pd.DataFrame()

    new_df = df.copy()
    new_df[new_column] = result
    return new_df