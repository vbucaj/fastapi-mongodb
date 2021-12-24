from pymongo import MongoClient



if __name__ == '__main__':
        
    client = MongoClient('mongodb+srv://vbucaj:Daors%40$$$2021@cluster0.zeg1h.mongodb.net/?retryWrites=true&w=majority')
    db = client.gettingStartedNow
    people = db.people

    import datetime
    personDocument = {
    "name": { "first": "Alan", "last": "Turing" },
    "birth": datetime.datetime(1912, 6, 23),
    "death": datetime.datetime(1954, 6, 7),
    "contribs": [ "Turing machine", "Turing test", "Turingery" ],
    "views": 1250000
    }

    people.insert_one(personDocument)