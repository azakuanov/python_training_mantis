from model.project import Project
import random, string

def test_create_new_project (app):
    if len(app.projects.get_project_list()) == 0:
        app.group.create_new_group(Project(projectname  = randomword(), description="description1"))
    app.session.login("administrator","root")
    old_list = app.soap.get_list_of_the_projects("administrator","root")
    app.projects.create_new_project(Project(projectname  = randomword(), description="description1"))
    new_list = app.soap.get_list_of_the_projects("administrator","root")
    assert len(old_list) + 1 == len(new_list)
    return print(len(old_list) + 1, len(new_list))


def randomword():
   return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

