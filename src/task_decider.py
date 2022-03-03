

def get_preferred_option(task_1, task_2):
    
    if task_1.name in task_2.preferred_jobs:
        return task_1.name
    elif task_2.name in task_1.preferred_jobs:
        return task_2.name