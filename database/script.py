from pymongo import MongoClient
import csv


def ingest_from_csv(filename, collection_name):
    try:
            with open(filename, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                entry = {}
                for idx, row in enumerate(reader):
                    if idx == 0:
                        continue
                    try:
                        entry = {
                            "Reference Area" : row[0],
                            "Time Period" : row[1],
                            "Observation Value" : row[2],
                        }

                        collection_name.insert_one(entry)
                        print(f'Successfully inserted {idx}th row! out of 687')

                    except:
                        return

    except FileNotFoundError:
            print('File does not exist')

def get_database():
    CONNECTION_STRING = "mongodb+srv://johnd:lifevision@cluster0.28vgr.mongodb.net/test?retryWrites=true&w=majority"
    client = MongoClient(CONNECTION_STRING)
    return client['gdp_country']


def print_collection(collection_name):   
    for item in collection_name.find():
        print(item)



if __name__ == "__main__":    
    dbname = get_database()
    collection_name = dbname['gdp_country']
    ingest_from_csv('data2.csv', collection_name)
    print_collection(collection_name)

