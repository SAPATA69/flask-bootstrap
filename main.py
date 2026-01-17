from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.config["SECRET_KEY"] = b'eieieiei;eiwwia'

cars = [
    {'id': 1, 'brand': 'Toyota', 'model': 'Yaris Ativ', 'year': 2024, 'price': 560000},
    {'id': 2, 'brand': 'Toyota', 'model': 'Yaris Cross', 'year': 2025, 'price': 790000},
    {'id': 3, 'brand': 'Nissan', 'model': 'Kicks', 'year': 2024, 'price': 850000},
    {'id': 4, 'brand': 'Mercedes-Benz', 'model': 'C-Class', 'year': 2025, 'price': 2590000},
    {'id': 5, 'brand': 'Mercedes-Benz', 'model': 'E-Class', 'year': 2025, 'price': 3490000},
    {'id': 6, 'brand': 'BMW', 'model': '3 Series', 'year': 2025, 'price': 2590000},
    {'id': 7, 'brand': 'BMW', 'model': '5 Series', 'year': 2025, 'price': 3790000}
]

@app.route('/')
def index():
    return render_template('index.html', title='Home Page')

@app.route('/cars', methods=['GET', 'POST'])
def show_cars():
    search_query = ''
    filtered_cars = cars
    
    if request.method == 'POST':
        search_query = request.form.get('brand', '').strip()
        
        if search_query:
            # ค้นหาโดยไม่สนใจตัวพิมพ์เล็ก-ใหญ่
            filtered_cars = [
                car for car in cars 
                if search_query.lower() in car['brand'].lower()
            ]
            
            if not filtered_cars:
                flash(f'ไม่พบรถยี่ห้อ "{search_query}"', 'warning')
            else:
                flash(f'พบรถยี่ห้อ "{search_query}" จำนวน {len(filtered_cars)} คัน', 'info')
    
    return render_template('cars/cars.html',
                         title='Show All Cars Page',
                         cars=filtered_cars,
                         search_query=search_query)

@app.route('/cars/new', methods=['GET', 'POST'])
def new_car():
    if request.method == 'POST':
        brand = request.form['brand']
        model = request.form['model']
        year = int(request.form['year'])
        price = int(request.form['price'])

        if len(cars) > 0:
            new_id = cars[-1]['id'] + 1
        else:
            new_id = 1
            
        car = {'id': new_id, 'brand': brand, 'model': model, 'year': year, 'price': price}

        cars.append(car)
        flash('เพิ่มรถใหม่สำเร็จ!', 'success')
        return redirect(url_for('show_cars'))
    
    return render_template('cars/new_car.html',
                         title='New Car Page')

@app.route('/cars/<int:id>/delete')
def delete_car(id):
    for car in cars:
        if id == car['id']:
            cars.remove(car)
            flash('ลบรถสำเร็จ!', 'success')
            break
    
    return redirect(url_for('show_cars'))

@app.route('/cars/<int:id>/edit', methods=['GET', 'POST'])
def edit_car(id):
    car = None
    for c in cars:
        if c['id'] == id:
            car = c
            break
    
    if car is None:
        flash('ไม่พบรถที่ต้องการแก้ไข', 'danger')
        return redirect(url_for('show_cars'))
    
    if request.method == 'POST':
        car['brand'] = request.form['brand']
        car['model'] = request.form['model']
        car['year'] = int(request.form['year'])
        car['price'] = int(request.form['price'])
        
        flash('แก้ไขข้อมูลรถสำเร็จ!', 'success')
        return redirect(url_for('show_cars'))
    
    return render_template('cars/edit_car.html',
                         title='Edit Car Page',
                         car=car)

if __name__ == '__main__':
    app.run(debug=True)