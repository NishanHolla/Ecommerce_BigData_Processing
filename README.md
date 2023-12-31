# Ecommerce_BigData_Processing

### Objective

This Hadoop MapReduce solution aims to analyze a massive dataset from a leading e-commerce platform. The dataset consists of two tables: customer orders and product reviews. The goal is to perform a join operation, filter out low-rated reviews, and aggregate the results to identify products with the most negative reviews and the quantity of those products sold.

### Workflow Explanation

#### **Mapper 1:**

- Reads each line from the input.
- Separates fields based on tab ('\t') and identifies whether the record is from the "order" or "review" table.
- For "order" records, emits the product ID, record type ("order"), customer ID, and quantity.
- For "review" records, emits the product ID, record type ("review"), customer ID, and rating.

#### **Mapper 2:**

- Reads the output of Mapper 1.
- Filters out low-rated reviews (ratings less than 3) and emits records for both "review" and "order" types.

#### **Mapper 3:**

- Reads the output of Mapper 2.
- Aggregates the quantity of products sold for each product ID.

#### **Reducer 1:**

- Reads the output of Mapper 1.
- Emits the product ID, record type, customer ID, and quantity.

#### **Reducer 2:**

- Reads the output of Mapper 2.
- Combines the information from "review" and "order" types using a key (product ID, customer ID).
- Emits the product ID, customer ID, and quantity for each entry.

#### **Reducer 3:**

- Reads the output of Mapper 3.
- Emits the product ID and the aggregated quantity of products sold.

### Testing Script

To test this multi-stage MapReduce solution, use the provided testing script. The script initiates each stage of the MapReduce job and cleans up intermediate and output directories before starting a new run.

```bash
#!/usr/bin/env bash

# Clean up intermediate HDFS directories
hdfs dfs -ls /intermediate-1
if [[ $? == 0 ]]; then
    echo "Deleting Intermediate-1 HDFS directory before starting job.." 
    hdfs dfs -rm -r /intermediate-1
fi

hdfs dfs -ls /intermediate-2
if [[ $? == 0 ]]; then 
    echo "Deleting Intermediate-2 HDFS directory before starting job.." 
    hdfs dfs -rm -r /intermediate-2
fi

# Clean up the previously used output directory
hdfs dfs -ls /task2/output
if [[ $? == 0 ]]; then
    echo "Deleting previous output directory"
    hdfs dfs -rm -r /task2/output
fi

echo "Initiating stage-1"
echo "==========================================================="

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-mapper "$PWD/mapper_1.py" \
-reducer "$PWD/reducer_1.py" \
-input /task2/dataset.txt \
-output /intermediate-1

echo "==========================================================="
echo "Stage-1 done" 
echo "Initiating stage-2"
echo "==========================================================="
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-mapper "$PWD/mapper_2.py" \
-reducer "$PWD/reducer_2.py" \
-input /intermediate-1/part-00000 \
-output /intermediate-2
echo "==========================================================="
echo "Stage-2 done" 
echo "Initializing stage-3"
echo "==========================================================="

hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.3.6.jar \
-mapper "$PWD/mapper_3.py" \
-reducer "$PWD/reducer_3.py" \
-input /intermediate-2/part-00000 \
-output /task2/output

echo "==========================================================="
echo "Stage-3 done"
```

### Execution

1. Make sure your Hadoop environment is set up correctly.
2. Run the testing script to execute the MapReduce job.

### Output

The final output will be stored in the `/task2/output` directory, containing the aggregated information about products with negative reviews and the quantity of those products sold.
