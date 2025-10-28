import numpy as np

data_type = [(' Name', 'S15'), ('Age', int), ('Height', float)]
Boys_details = [('Nnamdi', 8, 12.4), ('Matthew', 10, 18.6),('Benjamin', 9, 15.5), ('Ekene', 4, 7.3), ('Jesse', 8, 12.4)]

Boys = np.array(Boys_details, dtype=data_type)
print("Original array:")
print(Boys)
print("Sort by Name")
print(np.sort(Boys_details, order='name'))
print("Sort by Class")
print(np.sort(Boys, order='class'))
print("Sort by Height")
print(np.sort(Boys, order='height'))