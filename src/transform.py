def transform_data(df):
  df = df[['userId', 'id', 'title', 'body']]
  df.columns = ['user_id', 'post_id', 'title', 'content']
  df['title_length'] = df['title'].apply(len)
  return df
