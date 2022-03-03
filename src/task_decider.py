

def get_preferred_option(task_1, task_2):
    preferred_task_list = {
        #on right is task, on left is it's correspoding preferred task
        "Cook Dinner":"Wash Dishes",
        "Clean Windows": "Cook Dinner",
        "Wash Dishes":"Clean Windows"
    }

    preferred_task = preferred_task_list[task_1.name]
    if preferred_task == task_2.name:
        return preferred_task
    else:
        return preferred_task_list[task_2.name]