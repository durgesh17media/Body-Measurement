import pandas as pd
from sklearn import tree
from sklearn import preprocessing
le = preprocessing.LabelEncoder()

changi = pd.read_csv("gender-height-weight.csv")

# print(changi['temperature'].dtypes)
# print(changi['wind'].dtypes)
# print(changi['label'].dtypes)
changi = changi.values
feature_data = changi[:, :2]
target_data = le.fit_transform(changi[:,2])


#name of label and feature
changi_label_names = ['Rain', 'NOT_Rain']
changi_feature_names = ['temperature', 'wind']

# iris = datasets.load_iris()
#

print (changi)
