import random

def main():
    #domain 1- Steps of Risk Assessment
    questions_domain1 = [
        (" Which of the following factors an IS auditor should primarily consider when determining the acceptable level of risk:\nA.Risk acceptance is the responsibility of senior management.\nB.All risks do not need to be eliminated for a business to be profitable.\nC.Risks must be identified and documented in order to perform proper analysis on them.\nD.Line management should be involved in the risk analysis because management sees risks daily that others would not recognize.\n", 'C'),
        (" Benefit of development of organizational policies by bottom-up approach is that they:\nA.covers whole organization.\nB.are derived as a result of a risk assessment.\nC.will be in line with overall corporate policy.\nD.ensures consistency across the organization.\n", 'B'),
        (" An IS auditor is reviewing payroll application. He identified some vulnerabilities in the system. What would be the next task?\nA.Report the vulnerabilities to the management immediately.\nB. Examine application development process.\nC. Identify threats and likelihood of occurrence.\nD. Recommend for new application.","C"),
        (" Risk assessment process is :\nA. subjective.\nB. objective.\nC. mathematical.\nD. statistical.","A"),
        (" In planning an audit, the MOST critical step is the identification of the:\nA. areas of high risk.\nB. skill sets of the audit staff.\nC. test steps in the audit.\nD. time allotted for the audit.","A"),
        (" IS Auditor identified certain threats and vulnerabilities in a business process. Next, an IS auditor should:\nA. identify stakeholder for that business process.\nB. identify information assets and the underlying systems.\nC. disclose the threats and impacts to management.\nD. identify and evaluate the existing controls.","D"),
        (" The susceptibility of a business or process to make an error that is material in nature, assuming there were no internal controls.\nA. Inherent risk\nB. Control risk\nC. Detection risk\nD. Correction risk","A"),
        (" The decisions and actions of an IS auditor are MOST likely to affect which of the following risks?\nA. Inherent\nB. Detection\nC. Control\nD. Business","B"),
        (" Audit Charter should include:\nA. Yearly audit resource planning.\nB. audit function’s reporting structure.\nC. audit report drafting guidelines.\nD. Yearly audit calender.","B"),
        (" The result of risk management process is used for making:\nA. business strategy plans.\nB. audit charters.\nC. security policy decisions.\nD. decisions related to outsourcing.","C"),
        (" An IS auditor is using a statistical sample to inventory the tape library. What type of test would this be considered?\nA. Substantive\nB. Compliance\nC. Integrated\nD. Continuous audit","A"),
        (" When an IS auditor performs a test to ensure that only active users have access to a, the IS auditor is performing a:\nA. compliance test.\nB. substantive test.\nC. statistical sample.\nD. Judgment Sampling.","A"),
        (" Which of the following tests is an IS auditor performing when a sample of programs is selected to determine if the source and object versions are the same?\nA. A substantive test of program library controls\nB. A compliance test of program library controls\nC. A compliance test of the program compiler controls\nD. A substantive test of the program compiler controls","B"),
        (" A PRIMARY advantage of control self-assessment (CSA) techniques is that:\nA. it ascertains high-risk areas that might need a detailed review later\nB. risk can be assessed independently by IS auditors\nC. it replaces audit activities\nD. it allows management to delegate responsibility for control","A"),
        (" Which of the following sampling methods would be the MOST effective to determine whether access rights to staffs have been authorized as per the authorization matrix?\nA. stratified mean per unit\nB. attribute sampling\nC. discovery sampling\nD. stop or go sampling","B"),
        (" Use of statistical sampling will be more relevant as compared to judgment (non-statistical) sampling when:\nA. it is required to mitigate sampling risk\nB. auditor is inexperienced\nC. the probability of error must be objectively quantified\nD. it is required to mitigate audit risk","C"),
        (" Which of the following should an IS auditor use to detect duplicate invoice records within an invoice master file?\nA. Attribute sampling\nB. Generalized audit software (GAS)\nC. Test data\nD. Integrated test facility (ITF)","B"),
        (" An IS auditor is performing an audit of a remotely managed server backup. The IS auditor reviews the logs for one day and finds one case where logging on a server has failed with the result that backup restarts cannot be confirmed. What should the auditor do?\nA. Issue an audit finding\nB. Seek an explanation from IS management\nC. Review the classifications of data held on the server\nD. Expand the sample of logs reviewed","D"),
        (" Which of the following would be the BEST population to take a sample from when testing program changes?\nA. Test library listings\nB. Source program listings\nC. Program change requests\nD. Production library listings","D"),
        (" Auditee has taken corrective action immediately after the identification of a reportable finding. The auditor should:\nA. exclude the finding in final report without verifying corrective action.\nB. include the finding in the final report\nC. verify corrective action and if appropriately closed, same to be excluded from the report.\nD. call of inclusion/exclusion to be taken after discussion of finding with auditee management.","B"),
        (" Auditor should hold the closure meeting with the objective of:\nA. discussion on audit observations.\nB. correction of deficiencies.\nC. assessing audit staff performance.\nD. presenting the final audit report.","A"),
        (" Auditor should hold the closure meeting with the objective of:\nA. Allowing auditees to implementing recommendations as soon as possible\nB. Allowing auditors to explain complicated findings before a written report is issued\nC. Allowing auditors to buy confidence of management.\nD. To ensure that there have been no misunderstandings or misinterpretations of facts","D"),
        (" IS auditor finds that critical disaster recovery plan (DRP) does not cover all of the systems. IS Auditor should:\nA. inform the management and evaluate the impact of not covering all the systems.\nB. postpone the audit.\nC. continue audit of existing disaster recovery plan (DRP)\nD. call for explanation from management for not covering all the systems.","A"),
        (" While reviewing an application, IS auditor observed minor weakness in database which is out of the scope for the audit. IS auditor should:\nA. include that database in the scope.\nB. note down the weakness for future review.\nC. work with database administrator to correct the weakness.\nD. report the weakness in the audit report.","D"),
        (" While reviewing a finance application, IS auditor observed major weakness in change management application supporting the finance application. IS auditor should:\nA. continue review of finance application and report deficiency of change management application to IT manager.\nB. complete review of finance application and ignore deficiency as it is not part of the audit scope.\nC. formally report deficiency in audit report.\nD. cease audit activity until deficiency is corrected.","C"),
        ("  IS auditor observed inadequate controls for remote access for a critical application. Management disagrees stating that intrusion detection system (IDS) and firewall controls are in place. Which of the following is the BEST option for the IS auditor?\nA. Revised the finding considering management views.\nB. Withdraw the finding because the IDS controls are in place.\nC. Withdraw the finding because firewall rules are monitored\nD. Document audit findings in the audit report.","D"),
        (" In cases where there is disagreement regarding the impact of a finding, an IS auditor should:\nA. take a statement from auditee accepting full legal responsibility.\nB. explain impact of the findings and risk of not correcting it.\nC. inform disagreement to the audit committee for resolution.\nD. exclude the finding considering auditee’s view.","B"),
        (" An organization has agreed to perform remediation related to high-risk audit findings. However, remediation may not be completed within the next audit cycle. Which of the following is the BEST way for an IS auditor to follow up on the activities?\nA. Provide management with a remediation timeline and verify adherence.\nB. Conduct a review of the controls after the projected remediation date\nC. Continue to audit the failed controls according to the audit schedule\nD. Review the progress of remediation on a regular basis","B"),
        (" To review adequacy of management’s remediation action plan, which of the following should be the MOST important consideration?\nA. Approval of remediation action by senior management.\nB. Man-days required for future audit work\nC. Potential cost savings\nD. Criticality of audit findings","D")
    ]
        
    questions = questions_domain1
    # questions = questions_domain2
    # questions = questions_domain3
    # questions = questions_domain4
    # questions = questions_domain5
    
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
