def display_grid(size):
    for row in range(size):

        print("+" + "---+" * size)

        print("|   " * (size + 1))  
    
    print("+" + "---+" * size)

grid_size = int(input("Enter Grid Size : "))
display_grid(grid_size)


