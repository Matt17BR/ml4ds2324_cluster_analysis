1. Is there some sort of variation in the variables that depends on the time of year?
    - We can answer this question either by looking at the timeline plots in `cluster_analysis.ipynb`, or the individual variable plots in the `exploratory_data_analysis.ipynb`. In both cases, we concluded that the variation depends on the deactivation of the third transformer and the activation of the second transformer in late March of 2022.

2. Can days be clustered together using k-means/DBSCAN?
    - Yes, they can. It seems that since the clusters come from two different data generating processes, regarding the activation of the second transformer and the deactivation of the third transformer, the clusters have been formed that way. We chose parameters for DBSCAN in such a way that it generates 2 clusters and one group for the anomalies/spikes, and k-means generates 3 clusters, one of which can be interpreted as one for outliers as well.

3. Can we detect any anomalies or unusual patterns in the data that might indicate potential issues or inefficiencies?
    - Yes, as discussed before, the activation of the second transformer and the deactivation of the third transformer results in a spike. Apart from that since DBSCAN is made in a way that it allocates a group to anomalies specifically and we observe a few anomalies through DBSCAN clustering, we can understand which those are exactly by overlaying the `Timeline_DBSCAN.png` plot with the `standardized_plot.png`. Those anomalies could be a result of usual power outages, etc.

4.  How can we accurately label clusters returned by the implementation of k-means and DBSCAN clustering?
    - Starting by performing two-dimensional Principal Component Analysis and analyzing its loadings to comprehend the characteristics of each component. This understanding was then used to plot and effectively label clusters in the two-dimensional space for both clustering techniques. We noted that PC1 and PC2 gave an accurate representation of the subdivision of clusters of data.

5. How can the two cluster techniques be compared?
    - DBSCAN appears to be more adaptable to the actual structure of the data and capable of handling noise, whereas K-Means provides a more rigid, centroid-based clustering that requires the number of clusters to be known beforehand and does not account for outliers, but separates the outliers in a separate cluster.

6. For the case of variables with missing values, how can the analysis be conducted?
    - In this case, imputation can be applied. We chose sklearn's iterative imputer in order to carry out the task, which makes use of a k-nearest neighbors-based approach, after building a dataset which would accurately represent the patterns found in the missing data with regard to 2 transformers always being active at the same time. The results turned out to be satisfactory, as the UPS data seems to accurately reflect the patterns observed with respect to other variables.

7. What can be inferred from the median analysis?
    - We decided to do use violin plots for the median comparison and plotted each variable separately. Violin plots show the full distribution of the data, apart from just the median and the IQR range. We note that some medians are positioned at the center of the violins, suggesting symmetric data distributions, such as for TR1_Corr_2 and TR2_Corr_1. Others appear skewed, with medians located towards one end, as seen in TR3_Corr_N and POT_TR_SOMMA, indicating asymmetric distributions. The width of the violins also varies, showing different levels of variability.

8. Does it make sense to aggregate the raw data for analysis' purposes?
    - Since the measurements for each variable are taken at different minutes, it makes sense to aggregate data hourly or daily. We aggregated the data both ways and used the resulting datasets for different purposes. The daily data is more smoothed out, so we used it to find patterns when plotting. The hourly data provides more data points, which is useful for purely numerical/analytical tasks.

9. Can correlation heatmaps provide any insight in the variables' structure?
    - Yes, the correlation heatmaps helped us confirm that some variables showed high collinearity, which meant that we were best off aggregating them in a sensible way, or removing them altogether. If a variable is also not highly correlated with others, that provides insight in which of the variables account for more variance in the dataset and which of them are candidates for finding anomalies in the dataset. However, correlation heatmaps in our case can also be misleading because of the role of overlap in function between the TR2 and TR3 transformers.

10. How can we pick the number of clusters to use for cluster analysis?
    - The way we decided to perform cluster analysis was to pick the most optimal clusters number for the k-means method, and to find the 2 main hyper-parameters of the DBSCAN method in such a way that the Average Silhouette Width would be maximized for the number of clusters resulting from the choice of parameters. This may not be optimal, as the result that is produced is such that the cluster allocations for k-means (with 3 clusters) and DBSCAN (with 2 clusters and 1 unallocated cluster) are really similar and do not provide a very deep insight in the different mechanisms that allow k-means and DBSCAN to work.