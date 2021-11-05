class DataArray:

    @classmethod
    def load_array(cls, name):
        with open("../Data/" + name, "r") as file:
            content = file.read()
            lines = content.split("\n")
            rows = []
            array = []
            for line in lines[1:]:
                values = line.split(" ")
                rows.append(values[0])
                array.append(values[1:])
            return DataArray(array, rows, lines[0].split(" ")[1:])

    def __init__(self, values, rows, columns):
        self.values, self.rows, self.columns = values, rows, columns

    def __getitem__(self, item):
        return self.values[self.rows.index(item[0])][self.columns.index(item[1])]
