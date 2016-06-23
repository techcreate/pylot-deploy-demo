from system.core.model import Model

class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_all(self):
        query="SELECT * FROM courses"
        return self.db.query_db(query)

    def get_by_id(self, id):
        query ="SELECT * FROM courses WHERE id=:id LIMIT 1"
        data = {'id':id}
        return self.db.get_one(query, data)

    def insert_course(self, courses):
        data={
            'course_name':courses['course_name'],
            'description':courses['description']
        }
        query="INSERT INTO courses (course_name, description, created_at) VALUES (:course_name, :description, NOW())"
        return self.db.query_db(query, data)

    def delete_course(self,id):
        
        query = "DELETE FROM courses WHERE id=:id"
        data  = {'id':id}
        
        self.db.query_db(query,data)
      
        return True