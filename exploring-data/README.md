# Drawing graphs

Using the example of someone investigating whether there is any relation between a records start date or duration and the length of its description, this pair of notebooks takes you through the process of:

1. Gathering the appropriate data from Discovery API
2. Data manipulation using `panads`
    - Converting the data to a dataframe
    - Saving the dataframe to a CSV file
    - Loading data from a CSV file
    - Ensuring that data in columns is in the correct format/of the correct type
3. Drawing graphs using `matplotlib`
    - Bar graphs are used to illustrate the time periods covered by different records, using their covering dates. 
    - Scatter graphs are used to investigate whether start date or record duration relates to the length of a record description. 
4. Basic statistical analysis to explore the the ship records data and the chase data in more depth
    - Hierarchical clustering is used to investigate whether the clusters observed in the bar graph are distinct.
    - Linear regressions are used to establish whether the ship speed data changes reliably over the times in the logs. 
    - Principal component analysis is introduced as a way to plot all the data in a single graph, to show how the different records relate to each other.
Both notebooks are available in this repository. While they can be run stand-alone, it is recommended you work through both in order as the second uses a CSV file created by the first.