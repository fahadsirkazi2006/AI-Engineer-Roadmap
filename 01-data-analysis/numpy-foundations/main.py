import numpy as np
salaries = np.array([45000,70000,25000,90000,55000,22000,20000,1000000])
print(f"salaries : {salaries}")
print(f"Average salary : {np.mean(salaries)}")
print(f"Highest salary : {np.max(salaries)}")
print(f"Lowest salary : {np.min(salaries)}")

new_salary=np.array(salaries*1.10)
print(new_salary)

average=0
n=len(salaries)
for salary in salaries:
    average+=salary
avg_sal=average/n

print(avg_sal)

#calculating the difference between salary and avg salary
print("--------------DIFFERENCE BETWEEN SALARIES AND AVERAGE SALARY")
diff_sal=np.array(salaries-np.mean(salaries))
print(f"differences: {diff_sal}")

#Above average salaries
print("------------ABOVE AVERAGE SALARIES--------")
average_salary=np.mean(salaries)
above_average=average_salary<salaries
print(salaries[above_average])

#salaries above 40,000 but below 80,000
print("-----------SALARIES BETWEEN 40,000 AND 80,000")
salary = (salaries>40000) & (salaries<80000)
print(f"salaries: {salaries[salary]}")

#percentage of above average
print("----------PERCENTAGE OF ABOVE AVERAGE SALARIES------")
average_salary=np.mean(salaries)
above_average=average_salary<salaries
percentage=(np.sum(above_average)/len(salaries))*100
print(f"salary above avg: {percentage : .2f} %")

#MEAN VS MEDIAN
print("---------MEAN VS MEDIAN----------")
sal_avg= np.mean(salaries)
sal_mid = np.median(salaries)
print(f"mean : {sal_avg}  median: {sal_mid}")
#calculate the std diviation
print("-------STANDARD DEVIATION-------")
std_sal=np.std(salaries)
print(f"standard diviation :{std_sal}")

#numpy array shapes
print("------ARRAY info--------")
print(f"array: {salaries}")
print(f"Array shape: {salaries.shape}")
print(f"array dimensions : {salaries.ndim}")
print(f"total no. of elements: {salaries.size}")

#2D array
print("=======2D ARRAY=========")
data=np.array([
    [45000,2],
    [70000,4],
    [25000,1],
    [90000,10]
])
print(f"array: {data}")
print(f"Array shape: {data.shape}")
print(f"array dimensions : {data.ndim}")
print(f"total no. of elements: {data.size}")
#indexing and slicing of 2D array
print("========INDEXING AND SLICING==========")
print(data[0])
print(data[1,0])
print(data[:,0])
print(data[:,1])
print(data[1:3])
print(data[0:3,0])
#statistics on 2D array
print("===========STATISTICS ON 2D ARRAY======")
average_salry=np.mean(data[:,0])
average_experience=np.mean(data[:,1])
print(f"average salary :{average_salry} rs")
print(f"average years of experience : {average_experience} yrs")
#AXIS IN NUMPY
print("=========AXIS IN NUMPY============")
print(np.mean(data,axis=0))
print(np.mean(data, axis=1))


#normalizing function
print("=============NORMALIZING SALARY AND YRS OF EXPERIENCE==========")
def min_max_scale(values):
    x=values
    x_min=np.min(values)
    x_max=np.max(values)
    if x_min>=x_max:
        print("invalid ")
        return np.zeros_like(values,dtype=float)
    else: 
        scaled_values=(x-x_min)/(x_max-x_min)
        return scaled_values

print(f"normalized salaries: {min_max_scale(data[:,0])}")
print(f"normalized years of experience: {min_max_scale(data[:,1])}")