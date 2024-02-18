car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#result: Mustang

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#result: "year": 2020

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#result: "color": "red"

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#result: we don't have key model

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#result: car = {}


