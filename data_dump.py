import pymongo
import pandas as pd
import json
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

data_file_path = "/config/workspace/aps_failure_training_set1.csv"
database_name = "APS"
collection_name = "sensor_training_dataset"


if __name__ == "__main__":
    df = pd.read_csv(data_file_path)
    print(f"Rows and Columns: {df.shape}")

    ## convert Dataframe to json so that we can dump these record in mongoDB
    df.reset_index(drop =True, inplace = True)

    # convert Dataframe into json format
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    # insert converted json record to mongoDB
    client[database_name][collection_name].insert_many(json_record)
    print("sahiljosan edited")
