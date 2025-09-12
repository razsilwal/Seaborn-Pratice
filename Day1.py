import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np 

sns.set_style("whitegrid") # plt.style.use("fivethiryeight")-> it uses in matplotlib
sns.set_context("notebook", font_scale = 1.0)

tips = sns.load_dataset("tips") # this is already defined dataset in seaborn for praticing 
flights = sns.load_dataset("flights")
iris = sns.load_dataset("iris")


##-------------------------------------------------##
#- 1-> Histogram + KDE(Kernel Density Estimate) Plot
##-------------------------------------------------##

# plt.figure(figsize = (8, 3))
# sns.histplot(tips["total_bill"], kde = True)
# plt.title("Histogram + KDE from tips -> total bills")

# plt.tight_layout()
# plt.show()


##-----------------------------------##
#- 2-> Scatter Plot with hue and size
##-----------------------------------##

# plt.figure(figsize = (8, 3))
# sns.scatterplot(data = tips, x = "total_bill", y = "tip", hue = "day", size = "size", sizes = (20, 200))

# plt.title("Scatter Plot of Tips vs Total Bills")
# plt.tight_layout()
# plt.show()


##-------------------------------------##
#- 3-> Box + Swarm Plot Combined
##-------------------------------------##

# plt.figure(figsize = (10, 5))
# sns.boxplot(data = tips, x = "day", y = "total_bill")
# sns.swarmplot(data = tips, x = "day", y = "total_bill", alpha = 0.6)

# plt.title("Box Plot with Swarm overlay of tips")
# plt.show()

##-----------------------------------------##
#- 4-> Regression per smoker status (lmplot)
##-----------------------------------------##

# sns.lmplot(data = tips, x = "total_bill", y = "tip", hue = "smoker", height = 6, aspect = 1.8)
# plt.title("Linear Regression by Smoker status")
# plt.show()

##------------------------------##
#- 5-> Correlation Heatmap Plot
##------------------------------##

# plt.figure(figsize = (10, 5))
# cor = tips.select_dtypes(include = [np.number]).corr()
# sns.heatmap(cor, annot = True, cmap = "coolwarm")
# plt.title("Correlation Heatmap")
# plt.show()


##--------------------------------------------------##
#- 6-> FacetGrid Scatter by time (Lunch / Dinner) Plot
##--------------------------------------------------##

# plt.figure(figsize = (10, 5))
# g = sns.FacetGrid(tips, col = "time", height = 4)
# g.map(sns.scatterplot, "total_bill", "tip")
# g.add_legend()
# plt.show()


##-------------------------------------------##
#- 7-> Violin Plot
##-------------------------------------------##
# plt.figure(figsize = (10, 5))
# sns.violinplot(data = tips, x = "day", y = "total_bill", hue = "sex", split = True)
# plt.title("Volin Plot of total bill by day and gender")
# plt.show()


##------------------------------##
#- 8-> Pair Plot
##------------------------------##

# plt.figure(figsize = (10, 5))
# sns.pairplot(iris, hue = "species", diag_kind = "hist")
# plt.suptitle("Pairplot of Iris dataset", y = 1.02)
# plt.show()


# -----------------------------
# 13. Residual plot (residuals from linear regression)
# -----------------------------
plt.figure(figsize=(7,4))
sns.residplot(data=tips, x="total_bill", y="tip", lowess=True)
plt.title("Residual plot: tip ~ total_bill")
plt.show()