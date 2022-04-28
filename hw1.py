
# converting csv to json
class CsvToJson:
    def __init__(self, file):
        self.file = file

    def __repr__(self, file):
        with open(self.file, 'r+') as cf:
            self.file = cf.read().split('\n')
            return (''.join(('"', self.file.__repr__()[1:-1], "'")))

    def conversion(self):
        with open(self.file, 'r+') as cf:
            self.file = cf.read().split('\n')
            file_length = len(self.file)-1 # number of rows without header

            key = self.file[0]

            if file_length==1:
                json = {}
                value = self.file[1]
                json[key] = value
                
            else:
                json_arr = []
                for i in range(1,file_length):
                    json = {}
                    value = self.file[i]
                    json[key] = value
                    json_arr.append(json)
                with open('index.json', 'w+') as jload:
                    jload.write(str(json_arr))



# converting json to csv
class JsonToCsv:
    def __init__(self, file):
        self.file = file
        
    def conversion(self):
        with open(self.file, 'r') as f:
            uploaded = eval(f.read())

            with open('new.csv', 'a') as f2:
                if isinstance(uploaded, list):
                    for i in range(len(uploaded)):
                        for j in uploaded[i]:
                            if i==0:
                                f2.write(j)
                            f2.write(uploaded[i][j]+"\n")

                elif isinstance(uploaded, dict):
                    for i in uploaded :
                        f2.write(i+"\n")
                        f2.write(uploaded[i])


# obj1 = CsvToJson('index.csv')
# # print(obj.__repr__('index.csv'))
# obj1.conversion()

obj2 = JsonToCsv('index.json')
obj2.conversion()