import pandas as pd

fb1 = pd.read_excel(r"C:\Users\leben\Downloads\Fantasy Basketball 2020 - 2024.xlsx", sheet_name="2020 - 2021")
print(fb1.head())
print()

fb2 = pd.read_excel(r"C:\Users\leben\Downloads\Fantasy Basketball 2020 - 2024.xlsx", sheet_name="2021 - 2022")
print(fb2.head())
print()

fb3 = pd.read_excel(r"C:\Users\leben\Downloads\Fantasy Basketball 2020 - 2024.xlsx", sheet_name="2022 - 2023")
print(fb3.head())
print()

fb4 = pd.read_excel(r"C:\Users\leben\Downloads\Fantasy Basketball 2020 - 2024.xlsx", sheet_name="2023 - 2024")
print(fb4.head())
print()