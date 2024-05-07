import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 
#This sets seed to 0 which means everytime I run the program, the sequence of random numbers generated will be the same
np.random.seed(0)

# Generating random data of 100 students, score and weekly study time(in minutes)
score = np.random.randint(10,100,100)
study_time = np.random.randint(120,600,100)

mean_scores = np.mean(score)
median_scores = np.median(score)
std_dev_scores = np.std(score)

mean_study_time = np.mean(study_time)
median_study_time = np.median(study_time)
std_study_time = np.std(study_time)



print("Mean scores and study time:", mean_scores, mean_study_time)
print("Median scores and study time:", median_scores, median_study_time)
print("Standard deviation of scores and study time:", std_dev_scores, std_study_time)

# Plotting the data
sns.scatterplot(x=score, y=study_time)
plt.xlabel("Score")
plt.ylabel("Study Time")
plt.title("Score vs Study Time")
plt.show()