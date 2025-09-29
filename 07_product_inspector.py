# Hint: Manufacturing batches have standardized sizes for quality control



inspector_id = int(input("ID number please: "))

batch_id = input("Enter batch ID: ")
batch_size = int(input("Enter batch size: "))

total_quality_score = 0
defect_categories = {
    "none" : 0,
    "minor" : 0,
    "major" : 0
}

for i in range(batch_size):
    print(i)

    score = float(input("What is the quality score?:"))
    total_quality_score += score
    
print(total_quality_score / batch_size)














# Think: How do you ensure every item in the batch gets inspected?
# Your inspection approach here



