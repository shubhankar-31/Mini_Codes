import os


def file(x, y):
    os.chdir(f"{x}")
    for num in range(1, y + 1):
        os.makedirs(f"New Folder {num}")


# checking the directory location
print("Current Working Directory == \n"+os.getcwd())
print("\nEnter new path")

x = input("")
y = int(input("Enter the number of new folders that you want to create "))
file(x , y)


