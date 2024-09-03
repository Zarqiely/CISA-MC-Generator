import random

def main():
    #domain 1- Steps of Risk Assessment
    questions = [
        (" Which of the following factors an IS auditor should primarily consider when determining the acceptable level of risk:\nA.Risk acceptance is the responsibility of senior management.\nB.All risks do not need to be eliminated for a business to be profitable.\nC.Risks must be identified and documented in order to perform proper analysis on them.\nD.Line management should be involved in the risk analysis because management sees risks daily that others would not recognize.\n", 'C'),
        (" Benefit of development of organizational policies by bottom-up approach is that they:\nA.covers whole organization.\nB.are derived as a result of a risk assessment.\nC.will be in line with overall corporate policy.\nD.ensures consistency across the organization.\n", 'B'),
        (" An IS auditor is reviewing payroll application. He identified some vulnerabilities in the system. What would be the next task?\nA.Report the vulnerabilities to the management immediately.\nB. Examine application development process.\nC. Identify threats and likelihood of occurrence.\nD. Recommend for new application.","C"),
        (" Risk assessment process is :\nA. subjective.\nB. objective.\nC. mathematical.\nD. statistical.","A"),
        (" In planning an audit, the MOST critical step is the identification of the:\nA. areas of high risk.\nB. skill sets of the audit staff.\nC. test steps in the audit.\nD. time allotted for the audit.","A"),
        (" IS Auditor identified certain threats and vulnerabilities in a business process. Next, an IS auditor should:\nA. identify stakeholder for that business process.\nB. identify information assets and the underlying systems.\nC. disclose the threats and impacts to management.\nD. identify and evaluate the existing controls.","D")
    ]

    print("Domain 1 - Steps of Risk Assessment")
    random_indices = random.sample(range(len(questions)), len(questions))

    score = 0
    correct_count = 0
    user_answers = []

    for i, idx in enumerate(random_indices):
        question, correct_answer = questions[idx]
        user_input = input(f"No. {i + 1}:{question}Pls input ur answer and press enter:\n").strip()

        if user_input and (user_input.upper() == correct_answer or user_input.lower() == correct_answer.lower()):
            print("Correct")
            correct_count += 1
        else:
            print(f"Wrong answer, the correct answer is: {correct_answer}")

        current_accuracy = (correct_count / (i + 1)) * 100
        print(f"You have answered {correct_count} questions correctly out of {i + 1}.")



if __name__ == "__main__":
    main()