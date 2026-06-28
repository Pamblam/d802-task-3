import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('cifar-10/trainLabels.csv')
print(f"Total images: {len(df)}")

train_df, val_df = train_test_split(
    df,
    test_size=0.2,
    random_state=42,
    stratify=df['label']
)

train_df.to_csv('cifar-10/train_split.csv', index=False)
val_df.to_csv('cifar-10/val_split.csv', index=False)

print(f"Training images: {len(train_df)}")
print(f"Validation images: {len(val_df)}")

print("\nTraining class distribution:")
print(train_df['label'].value_counts().sort_index())
print("\nValidation class distribution:")
print(val_df['label'].value_counts().sort_index())
