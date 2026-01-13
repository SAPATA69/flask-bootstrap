from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] =b'eieieiei;eiwwia'

cars = [
  {'id':1, 'brand':'Toyota', 'model':'Yaris Ativ', 'year':2024, 'price': 560000},
  {'id':2, 'brand':'Toyota', 'model':'Yaris Cross', 'year':2025, 'price': 790000},
  {'id':3, 'brand':'Nissan', 'model':'Kicks', 'year':2024, 'price': 850000}
]

@app.route('/')
def index():
  return render_template('index.html', title='Home Page')

@app.route('/cars')
def show_cars():
  return render_template('cars/cars.html',
                         title='Show All Cars Page',
                         cars=cars)

@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
  if request.method == 'POST':
    brand = request.form['brand']
    model = request.form['model']
    year = int(request.form['year'])
    price = int(request.form['price'])

    length = len(cars)
    id = cars[length-1]['id'] + 1
    car = {'id':id, 'brand':brand, 'model':model, 'year':year, 'price': price}

    cars.append(car)
    Flask('add new car successfully' 'success')
    return redirect(url_for('show_cars'))
  
  

  return render_template('cars/new_car.html',
                         title='New Car Page')

@app.route('/cars/<int:id>/delete')
def delete_car(id):
  for car in cars:
    if id == car[car]:
      cars.remove(car)
      break
    
 flash('delete car successfully', 'success')   
 return redirect(url_for('show_cars'))
  
 @app.route('/cars/<int:id>/edit')
 def edit_car(id):
  pass
  