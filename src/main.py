from src.DataArray import DataArray
import os

if __name__ == '__main__':
    array = DataArray.load_array("Integrate_gauss")
    print(array["1.7", "1"])
