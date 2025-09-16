import seaborn as sns
import matplotlib.pyplot as plt 

sns.set_style("whitegrid")
sns.set_context("notebook", font_scale = 1.0)

tips = sns.load_dataset("tips")

#-------------------------#
# Violin plot
#-------------------------#

# plt.figure(figsize = (10, 5))
# sns.violinplot(data = tips, x = "day", y = "total_bill", hue = "sex")
# plt.title("Violin Plot of total bill by day and sex")
# plt.show()


#-------------------------#
# Count plot
#-------------------------#
# plt.figure(figsize = (8, 5))
# sns.countplot(data = tips, x = "day", hue = "sex")
# plt.title("Count Plot of records by day and sex")
# plt.show()


#-------------------------#
# Facet Grid
#-------------------------#
# plt.figure(figsize = (8, 5))
# g = sns.FacetGrid(tips, row = "time", col = "sex")
# # g.map(sns.histplot, "total_bill", bins = 10)
# g.map(sns.scatterplot, "total_bill", "tip")
# plt.show()


#-------------------------#
# Regression plot
#-------------------------#

plt.figure(figsize = (8, 5))
sns.lmplot(data = tips, x = "total_bill", y = "tip", hue = "smoker", col = "day", order = 2) # order = 2 -> represent curved line 
plt.title("Linear Regression of total bill and tip by Smoker")
plt.show()