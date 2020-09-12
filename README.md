# todoist_CLI
Python program for creating and adding new tasks to Todoist projects from the command line

```
todoist.py "TASK PRIORITY PROJECT_NAME DUE_DATE"

todoist.py "New Task Added from Command Line p1 #Back_Burner by Monday night!"
```
    The priority flag is preceded by the p character eg. p1 = Priority 1

    The project name is preceded by the # character eg. #Project1 = Project1

    The due date is preceded by the by keyword eg. by Tuesday = Due by Tuesday

    Everything else in the input string is added as the Task Name

![Command Line Input Example](CLI_example.png)
