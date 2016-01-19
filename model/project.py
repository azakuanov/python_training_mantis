class Project:

    def __init__ (self, projectname = None, description = None):
        self.projectname = projectname
        self.description = description

    def __repr__(self):
        return "%s" % (self.projectname)