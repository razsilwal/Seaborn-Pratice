import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd 


sns.set_style("darkgrid")
sns.set_context("notebook", font_scale = 1.0)

tips = sns.load_dataset("tips")

#------------------------#
#-Plot Histogram and KDE-#
#------------------------#

# plt.figure(figsize = (8, 3))
# sns.histplot(tips["total_bill"])
# sns.kdeplot(data=tips, x="total_bill", color = "green", linewidth = 2)
# plt.title("Histogram and KDE Plot of Total Bill")
# plt.tight_layout()
# plt.show()


#------------------------#
#-Scatter Plot with hue and size-#
#------------------------#


# plt.figure(figsize = (10,5))
# sns.scatterplot(data = tips, x = "total_bill", y = "tip", hue = "day", size = "size", sizes = (20, 500))
# plt.title("Scatter Plot of Total-Bill and Tip (Hue = Day, Size = Order size)")
# plt.tight_layout()
# plt.show()


#------------------------#
#-Box + Swarm Plots -#
#------------------------#

plt.figure(figsize = (10, 5))
sns.boxplot(data = tips, x = "day", y = "total_bill")
sns.swarmplot(data = tips, x = "day", y = "total_bill", color = "k", alpha = 0.4)
plt.title("Box + Swarm plot")
plt.tight_layout()
plt.show()