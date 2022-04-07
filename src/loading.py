def s3_csv_path(bucket, data_key):
    '''
    This function returns the string that will be used to load the csv file inside the s3
    
    bucket (str): must be the bucket string name
    data_key (str): the string that comes after s3://XXX/{data_key} '''
    
    return 's3://{}/{}'.format(bucket, data_key)