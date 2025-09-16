import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_context("notebook", font_scale = 1.0)

tips = sns.load_dataset("tips")
flights = sns.load_dataset("flights")
# iris = sns.load_dataset(" iris")


#-------------------------#
#-----Point Plot----------#
#-------------------------#

# sns.pointplot(data = tips, x = "day", y = "total_bill", hue = "sex", dodge = 0.2, markers = ["x", "s"], capsize = 0.08)
# plt.title("Point plot of Average Total Bill by Day")
# plt.show()


#--------------------------#
#-Correlation Heatmap Plot-#
#--------------------------#

# cor = tips.corr(numeric_only = True) # tip, total_bill and size 

# sns.heatmap(cor, annot = True, fmt = ".2f", cmap = "coolwarm")
# plt.title("Correlation Heatmap of tips dataset")
# plt.show()



#--------------------------#
#---Pivot Heatmap Plot----#
#--------------------------#

x = flights.pivot_table(index = "year", columns = "month", values = "passengers")
sns.heatmap(x, fmt= ".0f", cmap = "coolwarm", annot = True)
plt.title("Pivot of passenger")
plt.show()