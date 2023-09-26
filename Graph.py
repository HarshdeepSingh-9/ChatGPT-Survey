"""
GRAPH CODE
"""
import pandas as pd
import matplotlib.pyplot as plt

# Function to read responses from a CSV file
def read_responses(file_path):
    try:
        responses_df = pd.read_csv(file_path)
        return responses_df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return None

# Function to plot responses for a specific question
def plot_question_responses(df, question_col):
    data = df[question_col].value_counts()
    
    plt.figure(figsize=(10, 5))
    
    # Determine the type of plot (bar or pie) based on the question
    if question_col in ["4. What is Current Level ?", "10. Will ChatGPT replace Google search engine ?"]:
        plt.bar(data.index, data.values, color='skyblue')
    else:
        plt.pie(data.values, labels=data.index, autopct='%1.1f%%', colors=['gold', 'lightcoral', 'lightskyblue'])
    
    # Add title and labels to the plot
    plt.title(f"Responses for {question_col}")
    plt.xlabel("Answers")
    plt.ylabel("Number of Responses")
    
    # Add legend for pie charts
    plt.legend(data.index, loc="best") if question_col not in ["4. What is Current Level ?", "10. Will ChatGPT replace Google search engine ?"] else None
    
    # Show the plot
    plt.show()

# Main function to execute the analysis
def main():
    file_path = r"What is ChatGPT ?.csv"
    responses_df = read_responses(file_path)

    if responses_df is not None:
        # List of questions to analyze
        question_cols = [
            '2. What is your Age group?',
            '3. What is your Gender?',
            '4. What is Current Level ?',
            '5. What is your Field of Study ?',
            '6. How much will you rate Artificial Intelligence comparing to Human Intelligence ',
            '7. Have you ever used ChatGPT ?',
            '9. Do you think the Development of ChatGPT is ',
            '10. Will ChatGPT replace Google search engine ?',
            '11. Should ChatGPT be allowed to the students to take help in assignments ?'
        ]
        
        for col in question_cols:
            print(f"\nQuestion: {col}")
            plot_question_responses(responses_df, col)

if __name__ == "__main__":
    main()

