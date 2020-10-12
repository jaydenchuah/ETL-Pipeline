# ETL-Pipeline
Hadoop ETL Pipeline Examples

**Hive:**

This examples shows how to write Hive UDF to perform ETL on data into a new table. The input data is available at:

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/SSBM1/part.tbl

Step 1: Create Hive UDF script (codes provided)

Step 2: Create tables, load data, perform transformation into new table on Hive Beeline CLI:

**Create and load table:**

Create table part (
p_partkey     int,
p_name        varchar(22),
p_mfgr        varchar(6),
p_category    varchar(7),
p_brand1      varchar(9),
p_color       varchar(11),
p_type        varchar(25),
p_size        int,
p_container   varchar(10))
row format delimited fields
terminated by '|' stored as textfile;

LOAD DATA LOCAL INPATH '/home/ec2-user/part.tbl '
OVERWRITE INTO TABLE part;

Create table part_new (
p_partkey     int,
p_name        varchar(22),
p_mfgr        varchar(6),
p_category    varchar(7),
p_brand1      varchar(9),
p_color       varchar(11),
p_type        varchar(25),
p_size        int,
p_container   varchar(10))
row format delimited fields
terminated by '\t' stored as textfile;

**Hive Query:**

ADD FILE /home/ec2-user/hive_udf.py; 
INSERT OVERWRITE TABLE part_new SELECT TRANSFORM (p_partkey,p_name,p_mfgr,p_category,p_brand1,p_color,p_type,p_size,p_container) 
USING 'python hive_udf.py' AS (p_partkey,p_name,p_mfgr,p_category,p_brand1,p_color,p_type,p_size,p_container) FROM part;


**Hadoop Streaming:**

This examples shows how to run a MapReduce job that implements a solution for the following query:

For Employee(EID, EFirst, ELast, Phone) and Customer(CID, CFirst, CLast, Address), find everyone with the same name using MapReduce:

SELECT EFirst, ELast, COUNT(*)
FROM Employee, Customer
WHERE EFirst = CFirst AND ELast = CLast;

Using the input data:

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/employee.txt

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/customer.txt

Step 1: Run on Hadoop Command line

cat employee.txt customer.txt > combined.txt

Step 2: Create Mapper and Reducer file (codes provided)

Step 3: Run Hadoop Streaming on Hadoop Command Line

hadoop jar hadoop-streaming-2.6.4.jar -input /user/ec2-user/combined.txt -output /data/output -mapper hs_mapper.py -reducer hs_reducer.py -file hs_mapper.py -file hs_reducer.py

Step 4: Check Result on Hadoop Command Line

hadoop fs -ls /data/output

hadoop fs -cat /data/output/part-00000

**Credits to Prof. Rasin for Input Data**
