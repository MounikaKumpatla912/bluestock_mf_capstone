import pandas as pd
import requests
from pathlib import Path

scheme_codes = [
    125497,  # HDFC Top 100 Direct
    119551,  # SBI Bluechip
    120503,  # ICICI Bluechip
    118632,  # Nippon Large Cap
    119092,  # Axis Bluechip
    120841   # Kotak Bluechip
]

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

for code in scheme_codes:

    url = f"https://api.mfapi.in/mf/{code}"

    try:
        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(data["data"])

            file_name = f"live_nav_{code}.csv"

            df.to_csv(output_dir / file_name, index=False)

            print(f"Saved: {file_name}")

        else:
            print(f"Failed for {code}")

    except Exception as e:
        print(f"Error for {code}: {e}")