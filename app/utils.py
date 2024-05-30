import modin.pandas as pd
from io import BytesIO


async def read_csv_data(file_bytes) -> pd.DataFrame:

    #  received the file data (n bytes) in a variable called 

    # Create an in-memory file-like object
    file_object = BytesIO(file_bytes)

    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(file_object)
    return df