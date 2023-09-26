"""
Group 52
Khushkaran Singh Brar: 501147343
Zeeshan Khan: 501138213
Basim Khan: 501202574
Harshdeep Singh: 501174746
"""
import pandas as pd    # Import pandas library
import matplotlib.pyplot as plt    # Import matplotlib library

responses_df = pd.read_csv(r"What is ChatGPT ?.csv")    # Assign data to responses_df

question_cols = ['2. What is your Age group?', '3. What is your Gender?', '4. What is Current Level ?', '5. What is your Field of Study ? ', '6. How much will you rate Artificial Intelligence comparing to Human Intelligence ', '7. Have you ever used ChatGPT ?', '9. Do you think the Development of ChatGPT is ', '10. Will ChatGPT replace Google search engine ?', '11. Should chatGPT be allowed to the students to take help in assignments ?']    # List of questions
for col in question_cols:    # Iterate over the list of questions
    data = responses_df[col].value_counts()    # Get counts of each question
    print(f"\nQuestion: {col}")    # Print the question
    print(data)    # Print the counts of each question

    plt.figure(figsize=(10,5))    # Create plot area of size(10,5)

    if col=="4. What is Current Level ?" or col=="10. Will ChatGPT replace Google search engine ?":    # Check the if condition
        plt.bar(data.index, data.values)    # Plot bar chart
    else:    # else body
        plt.pie(data.values, labels=data.index, autopct='%1.1f%%')    # Plot pie chart

    plt.title(f"Responses for {col}")    # Set title of the plot
    plt.xlabel("Answers")    # Set x axis label
    plt.ylabel("Number of Responses")    # Set y axis label
    plt.show()    # Show the plot
