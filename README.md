# PageRank on Google Cloud Platform using Pig and Spark

Malo GRALL

Alex MAINGUY

Mathis ROCHER

## Method

### Small dataset
![Pig vs Spark PageRank algorithm - Small dataset (in ms)](./images/vs-small.png)

![Pig vs Spark PageRank algorithm - Table Small dataset](./images/table-small.png)

### Big dataset
![Pig vs Spark PageRank algorithm - Big dataset (in ms)](./images/vs-big.png)

![Pig vs Spark PageRank algorithm - Table Big dataset](./images/table-big.png)

## Problems 

In order to get clearer results, we gathered Spark results and saved them in a separate file instead of printing them in the terminal with the Cloud Logging for python feature of GCP.

With pig we had trouble debugging with the logs because they were not easily accessible in GCP. The Logging menu had some logs but they were only logging the terminal outputs.
