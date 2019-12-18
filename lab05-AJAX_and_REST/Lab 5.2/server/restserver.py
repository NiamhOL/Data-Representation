'''
Note when this code is ran use the command python restserver.py it will create a running 
http://127.0.0.1:5000/ which you copy and paste into your web browser nothing will be found 
because we don't have something to deal with. 
Thus you will need to run this http://127.0.0.1:5000/cars -  it will show all the cars and 
by running this http://127.0.0.1:5000/cars/test it will get one car. 
We cannot test the POST UPDATE and DELETE with this hence here we will use curl 
see examples below. Note when running Curls keep the server running in the backround 
and open up a new command line copy and paste one of the curl into your cmd

'''
#!flask/bin/python
from flask import Flask, jsonify,  request, abort, make_response

app = Flask(__name__,
            static_url_path='',
            static_folder='../')


# This is where you save it in memory so as soon as the server is stopped all the data is lost
cars = [
    {
        "reg":"181 G 1234",
        "make":"Ford",
        "model":"Modeo",
        "price":18000
    },
    {
        "reg":"11 MO 1234",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    },
    {
        "reg":"test",
        "make":"Nissan",
        "model":"Almera",
        "price":8000
    }
]

'''
If the method is GET only it will return a JSON array for cars and contents of that cars list
'''

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify( {'cars':cars})
# curl -i http://localhost:5000/cars



'''
Slightly more complicated if you want to find the ID as we can see the root is cars with anything after it 
where anything will be interpreted as a string and the name of the string will be reg and will be passed 
into the GET car reg. It then searches through the list using a filter, lambda function which will go through 
each of the entries inside the list t and the condition is that if t reg is the same as the reg passed in the 
list cars then it goes into the new list called foundCars and if the len of found cars is equal to zero then 
it returns blank (status 204) says it is empty otherwise it returns the found car inside curly brackets.
If more then one car is found it will only return the first one  

'''


@app.route('/cars/<string:reg>', methods =['GET'])
def get_car(reg):
    foundCars = list(filter(lambda t : t['reg'] == reg , cars))
    if len(foundCars) == 0:
        return jsonify( { 'car' : '' }),204
    return jsonify( { 'car' : foundCars[0] })
# curl -i http://localhost:5000/cars/test



'''
Create is similar except the method is different (POST). We check does the request have JSON data if the request is in the normal url encoding then  
it will return a 400 error(bad request). No reg attribute inside the request then it  returns bad request.  It creates a new car object with the reg, 
make and model taking out from the request JSON the reg, make, model and price, this car is then appended to the list and the return car to user. 
Note this is useful when we will have ID’s controlled by the server. However, in this case we are using reg as ID which is controlled by the client.  

'''

@app.route('/cars', methods=['POST'])
def create_car():
    if not request.json:
        abort(400)
    if not 'reg' in request.json:
        abort(400)
    car={
        "reg":  request.json['reg'],
        "make": request.json['make'],
        "model":request.json['model'],
        "price":request.json['price']
    }
    cars.append(car)
    return jsonify( {'car':car }),201
# sample test
# Mac will accept the single quotes so will run fine 
# curl -i -H "Content-Type:application/json" -X POST -d '{"reg":"12 D 1234","make":"Fiat","model":"Punto","price":3000}' http://localhost:5000/cars
#  for windows use this one as windows does not accept the single quotes 
# curl -i -H "Content-Type:application/json" -X POST -d "{\"reg\":\"12 D 1234\",\"make\":\"Fiat\",\"model\":\"Punto\",\"price\":3000}" http://localhost:5000/cars

'''

Code for the update is similar the root is cars with anything after it the method is PUT sp the reg will be passed in. Again it will go through the list of cars 
using the lambda function and make an array of found cars. If no car is found it will return a 404 which indicates nothing was found; 400 if the request is not 
JSON, if make is in the request but is not in the type string then error is returned. The contents of found  car are then changed for element 0 this will change 
in the original list and make the make equal whatever make we get out of the JSON request. if there is nothing then it uses the original make from the list above. 
The same process is applied for model and price. The it will return the car found in its new updated form. 


'''


@app.route('/cars/<string:reg>', methods =['PUT'])
def update_car(reg):
    foundCars=list(filter(lambda t : t['reg'] ==reg, cars))
    if len(foundCars) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'make' in request.json and type(request.json['make']) != str:
        abort(400)
    if 'model' in request.json and type(request.json['model']) is not str:
        abort(400)
    if 'price' in request.json and type(request.json['price']) is not int:
        abort(400)
    foundCars[0]['make']  = request.json.get('make', foundCars[0]['make'])
    foundCars[0]['model'] =request.json.get('model', foundCars[0]['model'])
    foundCars[0]['price'] =request.json.get('price', foundCars[0]['price'])
    return jsonify( {'car':foundCars[0]})
# Mac will accept the single quotes so will run fine 
# curl -i -H "Content-Type:application/json" -X PUT -d '{"make":"Fiesta"}' http://localhost:5000/cars/181%20G%201234
# for windows use this one as windows does not accept the single quotes 
# curl -i -H "Content-Type:application/json" -X PUT -d "{\"make\":\"Fiesta\"}" http://localhost:5000/cars/181%20G%201234

'''
Delete is similar to previous methods. If car not found it will return a 404.  If car is found it will be deleted from the list and it will return Json(“result”:”true”}

'''
@app.route('/cars/<string:reg>', methods =['DELETE'])
def delete_car(reg):
    foundCars = list(filter (lambda t : t['reg'] == reg, cars))
    if len(foundCars) == 0:
        abort(404)
    cars.remove(foundCars[0])
    return  jsonify( { 'result':True })



'''
Error Handling: This is handy for production when put out to real users. In this case however it hides a lot of error so they should be commented out when debugging code. 


'''
@app.errorhandler(404)
def not_found404(error):
    return make_response( jsonify( {'error':'Not found' }), 404)

@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)


if __name__ == '__main__' :
    app.run(debug= True)
