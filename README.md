# PageRank on Google Cloud Platform using Pig and Spark

## Method

## Small dataset
![Pig vs Spark PageRank algorithm - Small dataset (in ms)](./images/vs-small.png)

|Dataset|Workers|Method|Time (s) |Results                                                                                                                                                                                                                                                                                                                                                          |
|-------|-------|------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Small  |2      |Pig   |136.588  |<http://dbpedia.org/resource/Anatolia>	0.2983564212780039 <http://dbpedia.org/resource/Anglican_Communion>	0.29340226518834245 |
|Small  |4      |Pig   |148.161  |<http://dbpedia.org/resource/Anatolia>	0.2983564212780039 <http://dbpedia.org/resource/Anglican_Communion>	0.29340226518834245 |
|Small  |5      |Pig   |130.215  |<http://dbpedia.org/resource/Anatolia>	0.2983564212780039 <http://dbpedia.org/resource/Anglican_Communion>	0.29340226518834245 |
|Small  |2      |Spark |27.436877|<http://dbpedia.org/resource/Attention-deficit_hyperactivity_disorder> 0.30051150556157313 <http://dbpedia.org/resource/Anatolia> 0.29838121010127533 |
|Small  |4      |Spark |23.578745|<http://dbpedia.org/resource/Attention-deficit_hyperactivity_disorder> 0.30051150556157313 <http://dbpedia.org/resource/Anatolia> 0.29838121010127533 |
|Small  |5      |Spark |24.976407|<http://dbpedia.org/resource/Attention-deficit_hyperactivity_disorder> 0.30051150556157313 <http://dbpedia.org/resource/Anatolia> 0.29838121010127533 |


## Big dataset
![Pig vs Spark PageRank algorithm - Big dataset (in ms)](./images/vs-big.png)

|Dataset|Workers|Method|Time (s) |Results                                                                                                                                                                                                                                                                                                                                                          |
|-------|-------|------|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|BIIIIIGGG|2  |Pig  |4061.065 |<http://dbpedia.org/resource/Living_people>	33320.50837900091 <http://dbpedia.org/resource/United_States>	15212.1441258204 |
|BIIIIIGGG|4  |Pig  |3539.795 |<http://dbpedia.org/resource/Living_people>	33320.50837900091 <http://dbpedia.org/resource/United_States>	15212.1441258204 |
|BIIIIIGGG|5  |Pig  |1847.758 |<http://dbpedia.org/resource/Living_people>	33320.50837900091 <http://dbpedia.org/resource/United_States>	15212.1441258204 |
|BIIIIIGGG|2  |Spark|2455.566646|<http://dbpedia.org/resource/Living_people> 36794.33146754478 <http://dbpedia.org/resource/United_States> 13201.340151981203 |
|BIIIIIGGG|4  |Spark|1853.443464|<http://dbpedia.org/resource/Living_people> 36794.33146754478 <http://dbpedia.org/resource/United_States> 13201.340151981203 |
|BIIIIIGGG|5  |Spark|1770.289685|<http://dbpedia.org/resource/Living_people> 36794.33146754478 <http://dbpedia.org/resource/United_States> 13201.340151981203 |