# ETL-Pipeline
Hadoop ETL Pipeline Examples

This examples shows how to run a MapReduce job that implements a solution for the following query:


For Employee(EID, EFirst, ELast, Phone) and Customer(CID, CFirst, CLast, Address), find everyone with the same name using MapReduce:

SELECT EFirst, ELast, COUNT(*)
FROM Employee, Customer
WHERE EFirst = CFirst AND ELast = CLast;

Using the imput data:
http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/employee.txt
http://rasinsrv07.cstcis.cti.depaul.edu/CSC555/customer.txt
