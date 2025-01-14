import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.patches as mpatches
from sklearn.decomposition import PCA
import numpy as np
import git

#get the Git root location
git_repo = git.Repo('.', search_parent_directories=True)

#Load the data
df = pd.read_csv(f"{git_repo.working_tree_dir}\\Data\\data.csv")
df.drop('Unnamed: 0', axis=1, inplace=True)

start_index = df.columns.get_loc('A')
end_index = df.columns.get_loc('T')
ELEMENTS = np.array(df.iloc[:, start_index:end_index + 1].columns)

#PCA
pca = PCA().fit(df.iloc[:, start_index:end_index+1])

num_pc = pca.n_features_in_ #Number of PC's

labels = ['PC' + str(x) for x in range(1, num_pc+1)] #Create labels for te scree plot. 

pca_data = pca.transform(df.iloc[:, start_index:end_index+1]) #PC's coordinates
pca_df = pd.DataFrame(pca_data, columns=labels)

#Creating an dataframe with labels and PC's
df_complete = df[['CLASS']]
df_complete = pd.concat([df_complete, pca_df], axis=1)

#Igenvalues
per_var_eigen = np.round(pca.explained_variance_, decimals=2)
per_var_eigen_df = pd.DataFrame(per_var_eigen, columns=['Eigenvalues'], index=labels)

per_var = np.round(pca.explained_variance_ratio_*100, decimals=2) 
per_var_df = pd.DataFrame(per_var, columns=['Explained Variance (%)'], index=labels)

var_sum = np.cumsum(pca.explained_variance_ratio_*100).round(decimals=2) 
var_sum_df = pd.DataFrame(var_sum, columns=['Accumulated Variance'], index=labels)

loadings = pca.components_ 

df_loadings = pd.DataFrame() 
for i in range(num_pc):
    loading_iterate = pd.Series(loadings[i], index=ELEMENTS, name=f'PC{i+1}') 
    df_loadings_provedor = pd.DataFrame(data=loading_iterate) 
    df_loadings = pd.concat([df_loadings, df_loadings_provedor], axis=1) 