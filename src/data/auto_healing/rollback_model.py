import shutil
import os

MODEL_PATH = "models/churn_model.pkl"
BACKUP_PATH = "models/churn_model_backup.pkl"


def backup_model():

    if os.path.exists(MODEL_PATH):

        shutil.copy(MODEL_PATH, BACKUP_PATH)

        print("Previous model backed up.")


def rollback_model():

    if os.path.exists(BACKUP_PATH):

        shutil.copy(BACKUP_PATH, MODEL_PATH)

        print("Model rollback completed.")

    else:

        print("No backup model found.")


if __name__ == "__main__":

    rollback_model()