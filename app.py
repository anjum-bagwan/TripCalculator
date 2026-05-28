from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/Calculate', methods=['POST'])
def Calculate():
    try:
        # User Details
        travel_per = int(request.form.get('travel_per', 0))
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        phone = request.form.get('phone', '')

        # Travel
        vehicle = int(request.form.get('vehicle', 1))
        km = float(request.form.get('km', 0))

        if vehicle == 1:
            cost_km = 5
            vehicle_name = "Bike"

        elif vehicle == 2:
            cost_km = 8
            vehicle_name = "Bus"

        elif vehicle == 3:
            cost_km = 12
            vehicle_name = "Car"

        else:
            cost_km = 25
            vehicle_name = "Aeroplane"

        travel_cost = cost_km * km

        # Stay
        stay = int(request.form.get('stay', 1))
        days = int(request.form.get('days', 0))

        if stay == 1:
            stay_cost = 0
            stay_type = "No Stay"

        elif stay == 2:
            stay_cost = 800
            stay_type = "Basic Hotel"

        elif stay == 3:
            stay_cost = 1500
            stay_type = "Standard Hotel"

        else:
            stay_cost = 3000
            stay_type = "Luxury Hotel"

        stay_total = stay_cost * days

        # Food
        food = int(request.form.get('food', 1))

        if food == 1:
            food_cost = 0
            food_type = "No Food"

        elif food == 2:
            food_cost = 300
            food_type = "Basic Veg"

        elif food == 3:
            food_cost = 500
            food_type = "Standard Veg / Non-Veg"

        else:
            food_cost = 800
            food_type = "Premium"

        food_total = food_cost * days * 3

        # Extra
        extra = int(request.form.get('extra', 0))

        # Total
        total_per_person = travel_cost + stay_total + food_total + extra
        total_all = total_per_person * travel_per

        return render_template(
            'result.html',
            name=name,
            email=email,
            phone=phone,
            travel_per=travel_per,
            vehicle_name=vehicle_name,
            km=km,
            stay_type=stay_type,
            food_type=food_type,
            days=days,
            travel_cost=travel_cost,
            stay_total=stay_total,
            food_total=food_total,
            extra=extra,
            total_per_person=total_per_person,
            total_all=total_all
        )

    except Exception as e:
        return f"Error occurred: {e}"


if __name__ == '__main__':
    app.run(debug=True)