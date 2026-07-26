import pandas as pd

data = {
    "Name": ["Rakshith", "Kiran"],
    "Age": [16, 25]
}

df = pd.DataFrame(data)

df.to_excel("students.xlsx", index=False)

print("Excel file created")
