# Principal Component Analysis (PCA)

Principal Component Analysis (PCA) is an effective tool in reducing the noisy and the dimensionality of the data.

## About the data
The __['data.csv'](https://github.com/CassSouza/Principal-Component-Analysis/tree/main/Data)__ dataframe consist of real world data that has been subjected to a clr (centered log-ratio) transformation. Labels and features have had their names changed to generic names in order to preserve the source of the data.

The code necessary for the hierarchical clustering analysis and plot are available in the __['PCA Code.py'](https://github.com/CassSouza/Principal-Component-Analysis/blob/main/PCA%20Code.py)__ file. The code will generate five different __[outputs](https://github.com/CassSouza/Principal-Component-Analysis/tree/main/Outputs)__:

+ **PCA_Result.csv:** The new principal dataframe. Has the same dimension that the input dataframe (__['data.csv'](https://github.com/CassSouza/Principal-Component-Analysis/tree/main/Data)__), but with the values transformed to PC.

+ **PCA_Result_Loadings.csv:** Dataframe containing the information about how much each element contributed to each PC.

+ **PC_eigenvalues.csv:** Dataframe containing the information about the eigenvalues (amount of variance captured along its direction).

+ **PC_variance_percent.csv.csv:** A transformation of the 'PC_eigenvalues.csv', showing the percentage of the variance captured for each PC.

+ **PC_variance_accumulation.csv:** Cumulative percentage of variance for each PC.

The scree plot and the PC1xPC2 plot can be seen below: 
<p float="left">
  <img src="https://github.com/CassSouza/Principal-Component-Analysis/blob/main/Outputs/Images/scree_plot.jpeg?raw=true" width="400" />
  <img src="https://github.com/CassSouza/Principal-Component-Analysis/blob/main/Outputs/Images/PC1xPC2.jpeg?raw=true" width="394" /> 
</p>