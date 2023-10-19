"""
    CS5001_5003 Fall 2023 San Jose
    Midterm Exam
    Question 1. Debugging a WordPress Plug-in

    Please refer the following diagram (also on Canvas)
    https://carriedils.com/learning-to-troubleshoot/

    A. This diagram, designed to help debug Word Press plug-ins, does not fully
    comply with our CS5001 conventions, although the meaning is still mostly
    clear. Please use your favorite flowchart tool to fix the diagram to comply
    with our standard flowchart format -- and correct any other errors.

    One flaw is that the questions appearing in diamonds should first appear
    in a parallelogram,representing "prompt output" to the user, as well as
    the user's input. Results, here shown as ovals, should actually appear
    as print statements in parallelograms, followed by a shape that indicates
    program completion. There are 2 additional known errors in the diagram.
    Fix and submit your revised diagram as a .png, .jpeg, or similar.

    B. Implement this corrected flowchart in Python. Validate all user input,
    but use string methods and logic to allow for common variants such
    "y" or "yes" or "Yes" or "YES" (minimizing user frustration). (Besides
    validating user input, a loop is needed for one other reason.)
    Avoid repetitive code, such as using nearly identical code to validate
    user inputs for every yes/no question.

    C. Run your solution multiple times. Capture a transcript from IDLE,
    ideally verifying the behavior of each pathway through the flowchart.
    Submit the transcript of your test results as a .txt file. (You may use
    another IDE iff you can capture a session transcript to a .txt file.)
"""


def main():
    # Student solution should replace the following "pass" statement.
    user_input = input("Are you using the latest version of plugin X")
    if user_input = "yes":
        for plugin in system:
            if plugin == 'X':
                continue
        deactivate(plugin[i])
        if trouble_shooting:
            default_theme()
            if trouble_shooting():
                print("it is a bug in plugin X")
            else:
                print("it si a conflict with your theme")
        else:
            for plugin in system:
                activate(plugin[i])
            
        
def trouble_shooting():
     print("is the problem still there?")
     answer = input("enter your answer")
     if answer == 'yes':
         return True


def default_theme():
    print("switch to default theme")
    # switch to default theme
    else:
        return False


if __name__ == '__main__':
    main()
