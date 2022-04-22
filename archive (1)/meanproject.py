import pandas as pd
import statistics as st
data=pd.read_csv("SOCR-HeoghtWeight.csv")
height=data["Height(Inches)"]
weight=data["Weight(Pounds)"]
heightmean=st.mean(height)
heightmode=st.mode(height)
heightmedian=st.median(height)
weightmean=st.mean(weight)
weightmode=st.mode(weight)
weightmedian=st.median(weight)
print(heightmean)
print(heightmode)
print(heightmedian)
print(weightmean)
print(weightmode)
print(weightmedian)