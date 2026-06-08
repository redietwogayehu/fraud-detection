
def create_time_features(df):
    df["hour_of_day"] = df["purchase_time"].dt.hour
    df["day_of_week"] = df["purchase_time"].dt.dayofweek
    return df


def engineer_time_features(df):
    try:
        df["purchase_time"] = pd.to_datetime(df["purchase_time"])
        df["signup_time"] = pd.to_datetime(df["signup_time"])

        df["time_since_signup"] = (
            df["purchase_time"] - df["signup_time"]
        ).dt.total_seconds() / 3600

        df["hour_of_day"] = df["purchase_time"].dt.hour
        df["day_of_week"] = df["purchase_time"].dt.dayofweek

        return df

    except Exception as e:
        print(f"Feature engineering error: {e}")
        return df