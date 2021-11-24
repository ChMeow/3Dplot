from mpl_toolkits.mplot3d.axes3d import Axes3D
import matplotlib.pyplot as plt
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})

#Font
##plt.rcParams["font.family"] = "serif"


#change / add / modify the color here:
#colors refer:  https://matplotlib.org/stable/_images/sphx_glr_named_colors_003.png
color = ["red",
         "blue",
         "green",
         "black",
         "purple",
         "cyan",
         "hotpink",
         "darkorange",
         "slategrey"]

# change the axis label here:
axis_X_text = "X-label here"
axis_Y_text = "Y-label here"   
axis_Z_text = "Z-label here"

# Change to False if every Z has its own X values.
constantX = True

dataMax = input("Number of graphs: ")
axis_X_text = input("X-axis Label: ")
axis_Y_text = input("Y-axis Label: ")
axis_Z_text = input("Z-axis Label: ")
font_size = int(input("Font Size: "))
font_name = "Times New Roman"
N = int(dataMax)
i = 1
while(i <= N):
    x=[]
    y=[]
    z=[]
    
    #ReadX
    if(constantX):
        filename = "X.txt"
    else:
        filename = str(i) + "X.txt"
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        count += 1
        x.append(float(line))
    file1.close()

    #Populate Y #the value will be 1,2,3,4,5 according to the files
    if(constantX):
        filename = "X.txt"
    else:
        filename = str(i) + "X.txt"
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        count += 1
        y.append(float(i))
    file1.close()

    #ReadZ
    filename = str(i) + "Z.txt"
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines:
        count += 1
        z.append(float(line))
    file1.close()

    datasets = [{"x":x, "y":y, "z":z, "colour": color[i-1]} for _ in range(6)]

    for dataset in datasets:
        ax.plot(dataset["x"], dataset["y"], dataset["z"], color=dataset["colour"])
    i = i + 1
ax.xaxis.set_tick_params(labelsize=int(font_size*0.8))
ax.yaxis.set_tick_params(labelsize=int(font_size*0.8))
ax.zaxis.set_tick_params(labelsize=int(font_size*0.8))

ax.set_xlabel(axis_X_text, fontname=font_name, fontsize=font_size)
ax.set_ylabel(axis_Y_text, fontname=font_name, fontsize=font_size)
ax.set_zlabel(axis_Z_text, fontname=font_name, fontsize=font_size)

plt.show()
