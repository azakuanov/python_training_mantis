import time
from model.project import Project

class Project_helper:

    def __init__(self, app):
        self.app = app

    def go_to_create_project_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()

    def go_to_project_list_page(self):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.2.19/manage_proj_page.php")

    def go_back_to_projects_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//span/a").click()


    def fill_group_fields(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create_new_project(self, project):
        wd = self.app.wd
        self.go_to_project_list_page()
        self.go_to_create_project_page()
        # fill group firm
        self.fill_group_fields(project)
        # submit group creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.go_back_to_projects_page()

    def get_project_list(self):
        wd = self.app.wd
        self.go_to_project_list_page()
        self.group_cache = []
        for element in (wd.find_elements_by_css_selector("tr.row-2")):
            cells = element.find_elements_by_tag_name('td')
            projectname = cells[1].text
            self.group_cache.append(Project(projectname = projectname))
        return list(self.group_cache)

    def delete_project(self, index):
        wd = self.app.wd
        self.go_to_project_list_page()
        self.select_project(index)
        wd.find_element_by_name("delete").click()
        self.go_back_to_projects_page()

    def select_project(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

