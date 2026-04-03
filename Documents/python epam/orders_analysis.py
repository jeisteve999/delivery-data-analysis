# brief practice 

orders = [
    {"order_id": 1, "city": "Bogota", "distance": 10, "delivery_time": 30, "cost": 100},
    {"order_id": 2, "city": "Medellin", "distance": 5, "delivery_time": 20, "cost": 80},
    {"order_id": 3, "city": "Bogota", "distance": 15, "delivery_time": 50, "cost": 150},
    {"order_id": 4, "city": "Cali", "distance": 7, "delivery_time": 25, "cost": 90},
    {"order_id": 5, "city": "Bogota", "distance": 3, "delivery_time": 15, "cost": 60}
]

def filter_distance(orders):
    result = []
    
    for order in orders:
        if order ["distance"] > 8:
            result.append(order)
    return result 

def total_cost_bogota(orders):
    total = 0
    
    for order in orders:
        if order["city"] == "Bogota":
            total += order["cost"]
    return total            

def average_delivery_bogota(orders):
    total_time = 0
    count= 0
    
    for order in orders:
        if order["city"] == "Bogota":
            total_time += order["delivery_time"]
            count += 1
    return total_time / count


def total_cost_by_city(orders):
    result = {}
    
    for order in orders:
        city = order["city"]
        cost = order["cost"]
        
        if city not in result:
            result[city] = 0
            
            result[city] += cost
    return result

def city_max_cost(costs):
    max_cost = float("-inf")
    best_city = ""
    
    for city, cost in costs.items():
        if cost > max_cost:
            max_cost = cost
            best_city = city
    return best_city

print("Filter distance > 8:")
print(filter_distance(orders))

print("\nTotal cost Bogotá:")
print(total_cost_bogota(orders))

print("\nAverage delivery Bogotá:")
print(average_delivery_bogota(orders))

print("\nCosts by city:")
costs = total_cost_by_city(orders)
print(costs)

print("\nCity with highest cost:")
print(city_max_cost(costs))