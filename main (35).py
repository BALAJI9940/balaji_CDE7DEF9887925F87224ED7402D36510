def LinearSearchproduct(product, target):
  indices = []
  for index, product in enumerate(product):
    if product == target:
      indices.append(index)
  return indices

#example indices
product = ["shoes", "boots", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result = LinearSearchproduct(product, target)
print(result)