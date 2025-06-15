import pybaseball as pyb
import pandas as pd
 
def fetch_statcast_data(first_name: str, last_name: str,
                        start_date: str, end_date: str) -> pd.DataFrame:
    """Lookup pitcher ID and retrieve Statcast data for the given date range."""
    # Find the MLBAM ID for the pitcher
    player = pyb.playerid_lookup(last_name, first_name)
    pitcher_id = player['key_mlbam'][0]
    # Fetch pitch-by-pitch data
    df = pyb.statcast_pitcher(start_date, end_date, pitcher_id)
    return df
 
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows missing key pitch info and prepare derived metrics."""
    df = df.dropna(subset=['pitch_type', 'plate_x', 'plate_z'])
    # (Add any other cleaning steps here, e.g. renaming or filtering)
    return df
 
def process_data(first_name: str, last_name: str,
                 start_date: str, end_date: str) -> pd.DataFrame:
    """Fetch and clean data end-to-end."""
    raw = fetch_statcast_data(first_name, last_name, start_date, end_date)
    return clean_data(raw)