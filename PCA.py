import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
df=np.array([[1,2,3],[4,5,6]])
print(df)
print(df.shape) # printing dimension of matrix shape[0] --> rows,shape[1]--> columns

standard_scaler=StandardScaler() # It treats all the features equally before applying the PCA because model goes into the features which having the maximum value
standard_scaler.fit_transform(df)

pca=PCA(n_components=1) #Applying the PCA
result=pca.fit_transform(df)
print(result)