import numpy as np
import matplotlib.pyplot as plt


def update_grid(grid: np.ndarray) -> np.ndarray:
    grid_copy = grid
    rows, cols = grid.shape
    for col in range(cols):
        for row in range(rows):
            live_neighbors = (
                grid[row, (col-1)%cols] + grid[row, (col+1)%cols] +
                grid[(row-1)%rows, col] + grid[(row+1)%rows, col] +
                grid[(row-1)%rows, (col-1)%cols] + grid[(row-1)%rows, (col+1)%cols] + 
                grid[(row+1)%rows, (col-1)%cols] + grid[(row+1)%rows, (col+1)%cols]                
            )

            if grid[row, col] == 1:
                if ((live_neighbors < 2) or (live_neighbors > 3)):
                    grid_copy[row, col] = 0
                    continue
            
            if live_neighbors == 3:
                grid_copy[row, col] = 1

    return grid_copy


def main():
    grid_size = 100
    grid = np.random.choice([0, 1], size=(grid_size, grid_size))
    plt.ion()

    for _ in range(100):
        plt.imshow(grid, cmap='binary')
        plt.draw()
        plt.pause(0.1)
        grid = update_grid(grid)

    plt.ioff()
    plt.show()


if __name__ == "__main__":
    main()