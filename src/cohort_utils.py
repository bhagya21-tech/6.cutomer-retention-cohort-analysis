import pandas as pd 

def build_cohort_columns(df):
    """
    Adds order_month, cohort_month, and cohort_index columns to a retail dataset.
    Assumes df already has a datetime column named 'invoicedate'.
    
    """
    
    # Create order month from invoice date
    df['order_month'] = df['invoicedate'].dt.to_period('M').dt.to_timestamp()
    
    # Find first purchase month for each customer
    first_purchase = (
        df.groupby('customerid')['order_month']
          .min()
          .reset_index()
          
    )
    first_purchase.columns = ['customerid', 'cohort_month']
    
    # Merge back 
    
    df = df.merge(first_purchase, on='customerid', how='left')
    
    # Force datetime
    df['order_month'] = pd.to_datetime(df['order_month'])
    df['cohort_month'] = pd.to_datetime(df['cohort_month'])
    
    # Create cohort index
    df['cohort_index'] = (
        (df['order_month'].dt.year - df['cohort_month'].dt.year) * 12 +
        (df['order_month'].dt.month - df['cohort_month'].dt.month) + 1
        
    )
    
    return df

def cohort_retention(df):
    """ 
    Build a cohort retention matrix.
    Rows = cohort_month
    Columns = cohort_index 
    Values = unique customers 
    
    """
    
    cohort_data = (
        df.groupby(['cohort_month', 'cohort_index'])['customerid']
          .nunique()
          .reset_index()
    )
    
    if cohort_data.empty:
        return None
    cohort_pivot = cohort_data.pivot(
        index='cohort_month', 
        columns='cohort_index',
        values='customerid'
    )
    
    if cohort_pivot.shape[1] == 0:
        return None
    
    cohort_size = cohort_pivot.iloc[:, 0]
    retention = cohort_pivot.divide(cohort_size, axis=0)
    
    return retention