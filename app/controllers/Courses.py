from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        
        self.load_model('Course')
        self.db = self._app.db
   
    def index(self):
        courses=self.models['Course'].get_all()
        return self.load_view('index.html', courses=courses)

    def add(self):

        return self.load_view('index.html')

    def add_process(self):
        print 'in add process', request.form
        courses=request.form
        self.models['Course'].insert_course(courses)
        return redirect('/')

    def delete(self,id):
        print 'in delete'
        courses=self.models['Course'].get_by_id(id)
        return self.load_view('delete.html', id=id, course=courses)

    def delete_process(self,id):
        
        self.models['Course'].delete_course(id)
        # course=self.models['Course'].get_by_id(id)
        # if course:
        #     self.models['Course'].delete_course(id)
        return redirect('/')

