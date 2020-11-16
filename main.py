import pandas as pd

squirelData = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = 0
black = 0
Cinnamon = 0
color_dic = {}

# print()
grasy = squirelData["Primary Fur Color"].tolist()

for color in grasy:
    if (color == 'Gray'):
        gray = gray + 1

    if (color == 'Cinnamon'):
        Cinnamon = Cinnamon + 1

    if (color == 'Black'):
        black = black + 1

color_dic['Gray'] = [str(gray), str(gray)]
color_dic['Cinnamon'] = [str(Cinnamon), str(Cinnamon)]
color_dic['Black'] = [str(black), str(Cinnamon)]
str(color_dic)
data = pd.DataFrame(color_dic)
print(color_dic)
data.to_csv("Squirel_Count.csv")

data = pd.read_csv("Squirel_Count.csv")
print(data)