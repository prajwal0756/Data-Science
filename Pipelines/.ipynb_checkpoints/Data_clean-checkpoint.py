import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder, StandardScaler


class DataCleaner:
    def __init__(
        self,
        numeric_fill='median',
        categorical_fill='mode',
        date_columns=None,
        z_thresh=3,
        scaling=True,
        encoding=True
    ):

        self.numeric_fill = numeric_fill
        self.categorical_fill = categorical_fill
        self.date_columns = date_columns or []
        self.z_thresh = z_thresh
        self.scaling = scaling
        self.encoding = encoding

        self.scaler = StandardScaler()
        self.label_encoders = {}

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:

        df = self.handle_missing(df)
        df = self.convert_dates(df)
        df = self.remove_outliers(df)

        if self.encoding:
            df = self.encode_categories(df)

        if self.scaling:
            df = self.scale_features(df)

        return df

    def handle_missing(self, df: pd.DataFrame) -> pd.DataFrame:

        # Numerical columns
        for col in df.select_dtypes(include=np.number).columns:

            if self.numeric_fill == "mean":
                df[col] = df[col].fillna(df[col].mean())

            elif self.numeric_fill == "median":
                df[col] = df[col].fillna(df[col].median())

            elif isinstance(self.numeric_fill, (int, float)):
                df[col] = df[col].fillna(self.numeric_fill)

        # Categorical columns
        for col in df.select_dtypes(exclude=np.number).columns:

            if self.categorical_fill == "mode":
                df[col] = df[col].fillna(df[col].mode()[0])

            elif isinstance(self.categorical_fill, str):
                df[col] = df[col].fillna(self.categorical_fill)

        return df

    def convert_dates(self, df: pd.DataFrame) -> pd.DataFrame:

        for col in self.date_columns:

            if col in df.columns:
                df[col] = pd.to_datetime(df[col], errors='coerce')

        return df

    def remove_outliers(self, df: pd.DataFrame) -> pd.DataFrame:

        numeric_cols = df.select_dtypes(include=np.number).columns

        for col in numeric_cols:

            std = df[col].std()

            if std == 0:
                continue

            mean = df[col].mean()

            z_scores = (df[col] - mean) / std

            df = df[z_scores.abs() <= self.z_thresh]

        return df

    def encode_categories(self, df: pd.DataFrame) -> pd.DataFrame:

        categorical_cols = df.select_dtypes(
            include=['object', 'category']
        ).columns

        for col in categorical_cols:

            encoder = LabelEncoder()

            df[col] = encoder.fit_transform(df[col])

            self.label_encoders[col] = encoder

        return df

    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:

        numeric_cols = df.select_dtypes(include=np.number).columns

        df[numeric_cols] = self.scaler.fit_transform(df[numeric_cols])

        return df
    

if __name__ == "__main__":

    df = pd.read_csv("customer_churn.csv")

    cleaner = DataCleaner(
        numeric_fill='median',
        categorical_fill='mode',
        date_columns=['JoinDate'],
        z_thresh=3,
        scaling=True,
        encoding=True
    )

    clean_df = cleaner.clean(df)

    print(clean_df.head())