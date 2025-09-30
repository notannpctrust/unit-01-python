# Hint: Manufacturing batches have standardized sizes for quality control



inspector_id = int(input("ID number please: "))#Inputting Inspector ID

batch_id = input("Enter batch ID: ")#Getting batch ID
batch_size = int(input("Enter batch size: "))#Getting batch size for each item batch

total_quality_score = 0#This will be used to store every item batch's quality score 
defect_categories = {
    "none" : 0,
    "minor" : 0,
    "major" : 0
}

for i in range(batch_size):#This loop is used to loop the exact number of times for each item batch 
    print(i)

    score = float(input("What is the quality score?:"))
    total_quality_score += score
    
print(total_quality_score / batch_size)#Dividing by the the number of items to get the EXPECTED quality score














# Think: How do you ensure every item in the batch gets inspected?
# Your inspection approach here



