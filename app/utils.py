import modin.pandas as pd
from io import BytesIO


async def read_csv_data(file_bytes) -> pd.DataFrame:
    """
     Identify records that are present in the source but missing in the target,
     received the file data (n bytes) in a variable called.
      
     Create an in-memory file-like object
     """

    file_object = BytesIO(file_bytes)

    # Read the CSV data into a pandas DataFrame
    df = pd.read_csv(file_object)

    #  Set first column as the  Index 
    df.set_index(df.columns[0])

    return df

async def get_missing_records(source, target):
    missing_records = set()


async def identify_discrepancy(source_df, target_df):
    """Compare each field in both datasets to identify discrepancies.""" 

    merged_df = source_df.merge(target_df, on='id', how='inner')
    discrepancies = merged_df[(merged_df != merged_df.shift())].dropna(how='all')
    
    return discrepancies




def reconcile_csv(source_file, target_file):
  """
  This function reconciles two CSV files and generates a report.

  Args:
      source_file (str): Path to the source CSV file.
      target_file (str): Path to the target CSV file.

  Returns:
      dict: A dictionary containing the reconciliation report with sections
          for missing records and discrepancies.
  """
  # Read the CSV files into DataFrames
  source_df = pd.read_csv(source_file)
  target_df = pd.read_csv(target_file)

  # Standardize data
  # You can add functions here to handle:
  # - Date formats (e.g., using pd.to_datetime)
  # - Case sensitivity (e.g., using str.lower())
  # - Leading/trailing spaces (e.g., using str.strip())

  # Identify missing records
  source_missing = source_df.merge(target_df[['id']], how='left', indicator=True)
  source_missing = source_missing[source_missing['_merge'] == 'left_only']
  source_missing = source_missing.drop('_merge', axis=1)

  target_missing = target_df.merge(source_df[['id']], how='left', indicator=True)
  target_missing = target_missing[target_missing['_merge'] == 'left_only']
  target_missing = target_missing.drop('_merge', axis=1)

  # Build the reconciliation report
  report = {}
  report['Source Records Missing in Target'] = source_missing.to_dict('records')
  report['Target Records Missing in Source'] = target_missing.to_dict('records')
  report['Records with Field Discrepancies'] = discrepancies.to_dict('records')

  return report

# Example usage
report = reconcile_csv('source.csv', 'target.csv')

# Access and process the report sections
source_missing = report['Source Records Missing in Target']
# ... and so on for other sections
