import pandas as pd

def prepare_data(dataset_path):
    data_dict = {}
    def convert(obj):
        data_dict['n'+str(obj.name)] = obj.values.tolist()
    df = pd.read_csv(dataset_path,index_col=0)
    df.apply(convert,axis=1)
    return data_dict
