import pandas as pd
import numpy as np
#pd.set_option("display.colheader_justify", )

#Reading the CSV file
df = pd.read_csv("raw_ipc_data.csv")
print(df)
#df.info()

#Standardizing dates to follow a consistent approch
df["submission_date"] = pd.to_datetime(df["submission_date"], format="mixed", errors="coerce").dt.strftime("%D-%M-%Y")
print(df["submission_date"])

#Capitalizing first letter of the all names of the collecter
df["collector_id"] = df["collector_id"].str.title()
print(df["collector_id"])

#Capitalizing first letter of all Departments
df["department"] = df["department"].str.strip().str.title()
print(df["department"])

#Converting columndata type to number and ininytelligible to NAN
print("New part")
arabic_to_number = {
    "واحد": 1,
    "خمسة": 5,
    "غير متوفر": np.nan}
# 2. إزالة المسافات الزائدة ثم الاستبدال
df["staff_count"] = (
    df["staff_count"].astype(str).str.strip().replace(arabic_to_number)
)

# 3. التحويل إلى أرقام (وتحويل أي نص متبقي إلى NaN)
df["staff_count"] = pd.to_numeric(df["staff_count"], errors="coerce")

# 4. (لمسة مشرف البيانات) استبعاد القيم غير المنطقية (أقل من 1 أو أكبر من 100)
df.loc[
    (df["staff_count"] <= 0) | (df["staff_count"] > 100), "staff_count"
] = np.nan
print(df["staff_count"])

#Capitalizing and remove indentation from "hand_hyg" column
df["hand_hygiene_available"] = df["hand_hygiene_available"].str.strip().str.title()
print(df["hand_hygiene_available"])

#Capitalizing and remove indentation from "ppe_avail" column
df["ppe_available"] = df["ppe_available"].str.strip().str.title()
print(df["ppe_available"])
#Capitalizing and remove indentation from "waste_segregation_ok" column
df["waste_segregation_ok"] = df["waste_segregation_ok"].str.strip().str.title()
print(df["waste_segregation_ok"])

#Equal number of digit
df["gps_latitude"] = df["gps_latitude"].fillna(0).round(5)
df["gps_longitude"] = df["gps_longitude"].fillna(0).round(5)
df.to_csv("clean_ipc_data.csv")
print(df)

