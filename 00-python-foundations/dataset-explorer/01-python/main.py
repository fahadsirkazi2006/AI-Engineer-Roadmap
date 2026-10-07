import csv
#pass1
with open('data/customers.csv','r') as csv_file1:
    csv_reader=csv.reader(csv_file1)
    next(csv_reader)
    total_sal=n=0
    for line in csv_reader:
        
        if line[2]!="":
            total_sal=total_sal+int(line[2])
            n=n+1
        else:
            continue
average = total_sal/n
#pass 2
with open('data/customers.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    header=next(csv_reader)
    customers=[]
    if not csv_reader:
            print("dataset is empty")
    else:  
        
        
        for line in csv_reader:
            customers_dict={}
            for i in range(len(header)):
                value=line[i]
                if value == "":
                    value=None
                
                else:
                    try:
                        value=int(line[i])
                    except ValueError:
                        try:
                             value=float(line[i])
                        except ValueError:
                             pass
                             
                customers_dict[header[i]]=value
            customers.append(customers_dict)
        print(customers)   
        
            
            
            
        
        print("=======DATA SUMMARY======")
        missing_count= {}
        for column in header:
                missing_count[column]=0
        for customer in customers:

            for column in header:
                if customer[column] == "":
                        missing_count[column] = missing_count[column]+1
            
                else:
                        continue
        print(f"rows : {len(customers)}")
        print(f"columns: {len(header)}")
        print("column information:")
        for column in header:
                print(f"{column}-->{type(customers[0][column]).__name__}-->missing : {missing_count[column] }")
                
        expected_types = {
            "name": str,
            "age": int,
            "salary": (int, float),
            "experience": int,
            "purchased": int
        }
        print("VALIDATION REPORT")
        invalid_count = 0
        invalid=[]
        invalid_by_column={}
        for column in header:
             invalid_by_column[column]=0
        for customer in customers:

            for column in header:

                if isinstance(customer[column], expected_types[column]):
                    print(f"{customer['name']}-->{column}-->valid")
                else:
                    print(f"{customer['name']} {column}-->invalid")
                    invalid_count+=1
                    invalid_dict={"customer":customer["name"],"column":column,"value":customer[column]}
                    invalid.append(invalid_dict)
                    invalid_by_column[column]+=1

        
        print(invalid)            
        print(f"total invalid values: {invalid_count}")
        print("invalid values by column")
        for column in header:
             percentage=round((invalid_by_column[column]/len(customers))*100,2)
             print(f"{column}: {invalid_by_column[column]} percentage ({percentage}%)")
        
        cleaned_customers = []
        cleaning_report={
                     "missing_replaced":0,
                     "invalid_replaced":0,
                     "purchased_converted":0
                }

        for customer in customers:

            cleaned_customer = {}

            for column in header:

                value = customer[column]

                if value in ("", "unknown", "N/A"):
                     value=None
                     cleaning_report["missing_replaced"]+=1
                if column=="purchased":
                    if value=="yes":
                          value=1
                          cleaning_report["purchased_converted"]+=1
                    elif value=="no":
                         value=0 
                         cleaning_report["purchased_converted"]+=1
                if not isinstance(value,expected_types[column]):
                  
                     value=None
                     cleaning_report["invalid_replaced"]+=1
            
                
            
                     

                cleaned_customer[column] = value

            cleaned_customers.append(cleaned_customer)
        print(cleaned_customers)
        print("CLEANING REPORT")
        for report in cleaning_report:
             print(f"{report}: {cleaning_report[report]}")
             
        #valid customer
        
        valid_customers = []

        for customer in cleaned_customers:
            
            if  customer["age"] != None and \
                customer["salary"] != None and \
                customer["experience"] != None and \
                customer["purchased"] != None:
                
                valid_customers.append(customer)

        print(valid_customers)
        print(f"Total customers: {len(cleaned_customers)}")
        print(f"Usable customers: {len(valid_customers)}")
        print(f"Removed customers: {len(cleaned_customers) - len(valid_customers)}")
                  




    
               

                

            




