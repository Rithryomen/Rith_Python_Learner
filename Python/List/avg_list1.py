#Define the score using a list of tuples(subject,score)
scores=[("Math",46),("English",60),("C/C++",70),("Physic",80),("Fundamental",30)]

#Define a function to calculate the average score
def cal_avg(score_list):
    total=0
    for subject,score in score_list:
        total+=score
    avg=total/len(score_list)
    return avg

#Define a function to calculate the sum of scores
def cal_sum(score_list):
    total=sum(score for subject,score in score_list)
    return total

#Calculate and print the results
avg_score=cal_avg(scores)
sum_score=cal_sum(scores)
print(f"The Sum is: {sum_score}")
print(f"The Average Score is: {avg_score}")