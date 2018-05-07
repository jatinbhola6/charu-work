import pandas as pd
from Algorithm import kkmean_jatin
df = pd.read_csv('Datasets/motors.csv',index_col=0)
print kkmean_jatin.main(df,5)