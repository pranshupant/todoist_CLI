#!/home/pranshu/anaconda3/bin/python3

#Change the Shebang above to match your python binary location

def searchProjectID(project_name):
    #Searches ProjectID from Project Name

    projects = requests.get("https://api.todoist.com/rest/v1/projects", headers={"Authorization": "Bearer %s" % your_token}).json()

    found = False

    for project in projects:

        if project_name == project['name']:
            project_id = project['id']
            found = True

    if not found:
        raise Exception("Project Doesn't Exist")

    return project_id

def createNewTask(your_token, task):
    #Creates New task on Todoist using their REST API
    response = None
    try:
        response = requests.post(
        "https://api.todoist.com/rest/v1/tasks",
        data=json.dumps({
            "project_id": task[0],
            "content": task[1],
            "due_string": task[2],
            "due_lang": "en",
            "priority": task[3]
        }),
        headers={
            "Content-Type": "application/json",
            "X-Request-Id": str(uuid.uuid4()),
            "Authorization": "Bearer %s" % your_token
        }).json()
    except Exception as e:
        print("Task Couldn't be created. Incorrect Parameters")
        raise Exception("Task Couldn't be created. Incorrect Parameters")               

    if bool(response) == True:
        print("Task Succesfully Added!")
    else:
        raise Exception("Task Couldn't be created. Incorrect Parameters")

if __name__ == "__main__":

    import uuid, requests, json, sys, re, pdb

    #Enter Unique User Token available on the todoist website
    your_token = "###:ENTER API TOKEN HERE:###"

    #Default Arguments
    priority = 1
    project_name = "Back_Burner"
    due_string = ""
    
    cmd_line = sys.argv[1]

    #Parsing arguments
    try:
        priority = int(re.findall("p(\d)", cmd_line)[0])
        priority = 5 - priority
        cmd_line = re.sub("p(\d)\s", "", cmd_line)
    except Exception as e:
        pass

    try:
        project_name = re.findall("#([\w]+)", cmd_line)[0]
        cmd_line = re.sub("#([\w]+)", "", cmd_line)
    except Exception as e:
        pass

    try:
        due_string = re.findall("by\s([\w\s]+)!", cmd_line)[0]
        cmd_line = re.sub("by\s[\w\s]+!", "", cmd_line)
    except Exception as e:
        pass

    try:
        content = re.findall("[\w\s]+", cmd_line)[0].strip(" ")
    except Exception as e:
        raise Exception("No Content")

    print("Task: ", content)
    print("Project Name: ", project_name)
    print("Due Date: ", "N/A" if due_string == "" else due_string)
    print("Priority: ", 5 - priority) 

    project_id = searchProjectID(project_name)

    task = (project_id, content, due_string, priority)

    createNewTask(your_token, task)
    