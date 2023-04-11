class Person: 
    
    def __init__(self, eyesColor) -> None:
        self.eyesColor = eyesColor

    def method1():
        pass




person = Person(2)
person.method1()



def route(reply, handler):
    pass

import Request

def handler(request, reply):
    request.query
    pass

def userHandler(request, reply):
    request.query
    reply.code(200).send( {status: ok})

    reply.code(404).send()
    pass

route('/auth', handler)
route('/user', userHandler)