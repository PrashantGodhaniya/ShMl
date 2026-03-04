import pandas as pd
import json
import os

LOG_FILE = "logs/prediction_log.json"


def log_prediction(prediction, probability):

    os.makedirs("logs", exist_ok=True)

    entry = {

        "prediction": int(prediction),
        "probability": float(probability)

    }

    if os.path.exists(LOG_FILE):

        with open(LOG_FILE) as f:

            data = json.load(f)

    else:

        data = []

    data.append(entry)

    with open(LOG_FILE, "w") as f:

        json.dump(data, f, indent=4)


def analyze_predictions():

    if not os.path.exists(LOG_FILE):

        print("No prediction logs found.")
        return

    with open(LOG_FILE) as f:

        data = json.load(f)

    df = pd.DataFrame(data)

    print("\nPrediction Distribution")

    print(df["prediction"].value_counts())

    print("\nAverage Confidence")

    print(df["probability"].mean())


if __name__ == "__main__":

    analyze_predictions()