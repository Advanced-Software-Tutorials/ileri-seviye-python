class MySpecialClass:
    my_list = [22, 33, 11, 44]

    def __len__(self):
        return 5

    def __getitem__(self, position):
        return self.my_list[position]


my_special_numbers = MySpecialClass()

print(len(my_special_numbers))  # MySpecialClass.__len__
print(my_special_numbers[2])  # MySpecialClass.__getitem__
print(my_special_numbers[1:-1])

print("\nIteration")
for special_number in my_special_numbers:
    print(special_number)

print("\nIteration sorted")
for special_number in sorted(my_special_numbers):
    print(special_number)
