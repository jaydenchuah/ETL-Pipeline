# ETL-Pipeline
Hadoop ETL Pipeline Examples

This examples shows how to run a MapReduce job that implements a solution for the following query:


For Employee(EID, EFirst, ELast, Phone) and Customer(CID, CFirst, CLast, Address), find everyone with the same name using MapReduce:

SELECT EFirst, ELast, COUNT(*)
FROM Employee, Customer
WHERE EFirst = CFirst AND ELast = CLast;

Using the input data:

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/employee.txt

http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/customer.txt

Step 1: Run on Command line

cat employee.txt customer.txt > combined.txt

Step 2: Create Mapper and Reducer file (codes provided)

Step 3: Run Hadoop Streaming on Command Line

hadoop jar hadoop-streaming-2.6.4.jar -input /user/ec2-user/combined.txt -output /data/output -mapper mapper.py -reducer reducer.py -file mapper.py -file reducer.py

Step 4: Check Result on Command Line

hadoop fs -ls /data/A4P4_output

hadoop fs -cat /data/A4P4_output/part-00000

