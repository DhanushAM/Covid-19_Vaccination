
#This Program Created By Dhanush A M Using Machine Learning (Python)
"""

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
import seaborn as sns
import plotly
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
#plt.rcParams['figure.figsize']=17,8
import cufflinks as cf
import plotly.offline as pyo
from plotly.offline import init_notebook_mode,plot,iplot
import folium 
from folium import plugins
plt.rcParams['figure.figsize'] = 10, 12
import warnings
warnings.filterwarnings('ignore')

pyo.init_notebook_mode(connected=True)
cf.go_offline()

df = pd.read_csv('covid_vaccine_statewise.csv')

df.head(5327)

df.isnull().sum()

"""#Total Individuals Vaccinated"""

f, ax = plt.subplots(figsize=(28, 28))
data = df[['State','Total Individuals Vaccinated']]   
data.sort_values('Total Individuals Vaccinated',ascending=False,inplace=True)
sns.set_color_codes("pastel")
sns.barplot(x="Total Individuals Vaccinated", y="State", data=data,label="Total Individuals Vaccinated", color="gray")
sns.set_color_codes("muted")


ax.set(xlim=(0, 500000), ylabel="",xlabel="Total Individuals Vaccinated")

"""# First Dose Administered & Second Dose Administered"""

f, ax = plt.subplots(figsize=(28, 28))
data = df[['State','First Dose Administered','Second Dose Administered']]   
data.sort_values('First Dose Administered',ascending=False,inplace=True)
sns.set_color_codes("pastel")
sns.barplot(x="First Dose Administered", y="State", data=data,label="First Dose Administered", color="red")
sns.set_color_codes("muted")
sns.barplot(x="Second Dose Administered", y="State", data=data, label="Second Dose Administered", color="green")
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 700000), ylabel="",xlabel="First Dose Administered & Second Dose Administered")
sns.despine(left=True, bottom=True)

"""# Male(Individuals Vaccinated) & Female(Individuals Vaccinated)"""

f, ax = plt.subplots(figsize=(28, 28))
data = df[['State','Male(Individuals Vaccinated)','Female(Individuals Vaccinated)']]   
data.sort_values('Female(Individuals Vaccinated)',ascending=False,inplace=True)
sns.set_color_codes("pastel")
sns.barplot(x="Male(Individuals Vaccinated)", y="State", data=data,label="Male", color="skyblue")
sns.set_color_codes("muted")
sns.barplot(x="Female(Individuals Vaccinated)", y="State", data=data, label="Female", color="pink")
ax.legend(ncol=2, loc="lower right", frameon=True)
ax.set(xlim=(0, 700000), ylabel="",xlabel="Male(Individuals Vaccinated) & Female(Individuals Vaccinated)")
sns.despine(left=True, bottom=True)

"""# Total Covaxin Administered """

f, ax = plt.subplots(figsize=(28, 28))
data = df[['State','Total Covaxin Administered']]   
data.sort_values('Total Covaxin Administered',ascending=False,inplace=True)
sns.set_color_codes("pastel")
sns.barplot(x="Total Covaxin Administered", y="State", data=data,label="Total Covaxin Administered", color="skyblue")
sns.set_color_codes("muted")

ax.set(xlim=(0, 500000), ylabel="",xlabel="Total Covaxin Administered")

"""# Total CoviShield Administered"""

f, ax = plt.subplots(figsize=(28, 28))
data = df[['State','Total CoviShield Administered']]   
data.sort_values('Total CoviShield Administered',ascending=False,inplace=True)
sns.set_color_codes("pastel")
sns.barplot(x="Total CoviShield Administered", y="State", data=data,label="Total CoviShield Administered", color="lightgreen")
sns.set_color_codes("muted")

ax.set(xlim=(0, 500000), ylabel="",xlabel="Total CoviShield Administered")

"""#Vaccinated For 18-45 years (Age),45-60 years (Age),60+ years (Age)"""

labels=np.array(['18-45 years (Age)', '45-60 years (Age)', '60+ years (Age)'])
stats=df.loc[386,labels].values

angles=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles,[angles[0]]))



fig=plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
ax.set_thetagrids(angles * 180/np.pi, labels)

ax.grid(True)

"""18-45 years (Age)	45-60 years (Age)	60+ years (Age)

#Total Doses Administered
"""

f, ax = plt.subplots(figsize=(28, 28))
data = df[['State','Total Doses Administered']]   
data.sort_values('Total Doses Administered',ascending=False,inplace=True)
sns.set_color_codes("pastel")
sns.barplot(x="Total Doses Administered", y="State", data=data,label="Total Doses Administered", color="orange")
sns.set_color_codes("muted")

ax.set(xlim=(0, 500000), ylabel="",xlabel="Total Doses Administered")


