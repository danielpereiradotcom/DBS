# Continuous Assessment
# Dublin Business School
# B8IT108 Data and Web Mining
# Lecturer: Bahman Honari (bahman.honari@dbs.ie)
# Student: Daniel Pereira (10391381@mydbs.ie)
# ##################################################

# The provided Dataset contains 16 variables. 
#   Response ids the target variable to be predicted using the other variables. 
#   X variables are the actual measurements. 
#   Y variables are the categorical form of the X variables based of the recommended cut-off points by the previous studies. 
#   Group is the variable that might moderate the predictability of response by Xs or Ys.  
# 
# The purpose of this study is to use “Decision Trees” to assess predictability 
# of Response by X, Y or combination of them. As mentioned in above, 
# this predictability might be affected by the Group variable, 
# and therefore the analysis should be performed for all cases, 
# as well as for each group separately to study the effect of variable Group. 
# ##################################################

# Start a fresh workspace environment
rm(list=ls())

# ##################################################
# Libraries that I am using
install.packages("rstudioapi")
library("rstudioapi")
install.packages("rpart.plot")
install.packages("rpart")
library(rpart)
library(rpart.plot)

install.packages("caret")
library(caret)

install.packages ("partykit")
library("partykit")
# ##################################################


# Define the working directory to the same as the code file
# I am using rstudioapi libray to set directory
setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

# Import the CSV file that we assume is in the same folder defined as working directory 
# The CA1_Dataset is format as below:
#     ID;Response;Group;Y1;Y2;Y3;Y4;Y5;Y6;Y7;X1;X2;X3;X4;X5;X6;X7
#     1;0;0;1;1;1;0;0;1;0;460;460;460;50.21;9.15;2.3;273.6
#     2;0;1;1;;;1;0;2;0;74;;;812.5;0.88;4.1;406.6
#     3;0;1;1;0;0;1;0;2;1;58;0;0;87.71;0.39;4.7;946.1
#     4;0;0;1;;;1;1;1;1;39;;;92.14;26.79;3.1;534.6
#     5;0;1;0;0;0;1;0;2;1;15;45;60;75.24;16.6;3.6;1019.4
MyDataset <- read.csv('CA1_Dataset.csv', header=TRUE, sep= ';') 

# Open the dataset to check if was imported ok
summary(MyDataset)
str(MyDataset)
# 'data.frame':	296 obs. of  17 variables:
#  $ ID      : int  1 2 3 4 5 6 7 8 9 10 ...
#  $ Response: int  0 0 0 0 0 0 0 0 0 0 ...
#  $ Group   : int  0 1 1 0 1 0 1 1 0 0 ...
#  $ Y1      : int  1 1 1 1 0 1 0 0 1 1 ...
#  $ Y2      : int  1 NA 0 NA 0 0 0 0 0 0 ...
#  $ Y3      : int  1 NA 0 NA 0 0 0 0 0 0 ...
#  $ Y4      : int  0 1 1 1 1 0 0 0 0 0 ...
#  $ Y5      : int  0 0 0 1 0 0 0 0 1 1 ...
#  $ Y6      : int  1 2 2 1 2 1 2 1 1 1 ...
#  $ Y7      : int  0 0 1 1 1 1 1 0 0 0 ...
#  $ X1      : int  460 74 58 39 15 47 23 14 56 40 ...
#  $ X2      : int  460 NA 0 NA 45 141 69 126 0 120 ...
#  $ X3      : int  460 NA 0 NA 60 188 92 224 0 160 ...
#  $ X4      : num  50.2 812.5 87.7 92.1 75.2 ...
#  $ X5      : num  9.15 0.88 0.39 26.79 16.6 ...
#  $ X6      : num  2.3 4.1 4.7 3.1 3.6 2.6 7.1 2.4 2.7 2.6 ...
#  $ X7      : num  274 407 946 535 1019 ...



# ##################################################
# CLEANING UP DATA SET


# The Response values is the column 2
# The Group values is the column 3
# The Y values are the columns 4 to 10
# The X values are the columns 11 to 17

# The first approach is predict using a full dataset Y and X
# Excluding the first column because is just a row count 
# Excluding the third column because is the Group

Dataset_XY <- MyDataset[c(-1,-3)]

# Now the columns numbers are aligned and we have
# Response as column 1
# Y from 2 to 8
# X from 9 to 16
# Changing Y responses as factor
cols <- c(1,3:9)
Dataset_XY[cols] <- lapply(Dataset_XY[cols], factor)

cols <- c(10:16)
Dataset_XY[cols] <- lapply(Dataset_XY[cols], as.numeric)



# just making sure data is ok
str(Dataset_XY)
names(Dataset_XY)


# ##################################################
# Now that data is ok, we can play around
attach(Dataset_XY)
head(Dataset_XY)
#   Response Y1   Y2   Y3 Y4 Y5 Y6 Y7  X1  X2  X3     X4    X5  X6     X7
# 1        0  1    1    1  0  0  1  0 460 460 460  50.21  9.15 2.3  273.6
# 2        0  1 <NA> <NA>  1  0  2  0  74  NA  NA 812.50  0.88 4.1  406.6
# 3        0  1    0    0  1  0  2  1  58   0   0  87.71  0.39 4.7  946.1
# 4        0  1 <NA> <NA>  1  1  1  1  39  NA  NA  92.14 26.79 3.1  534.6
# 5        0  0    0    0  1  0  2  1  15  45  60  75.24 16.60 3.6 1019.4
# 6        0  1    0    0  0  0  1  1  47 141 188  58.36 11.10 2.6  643.6






###########################################################
# Case 1: Basic Decision tree
# All Variables 
###########################################################

# Creating training and testing dataset 80% and 20%
intrain<-createDataPartition(y=Dataset_XY$Response,p=0.8,list=FALSE)
training<-Dataset_XY[intrain,]
testing<-Dataset_XY[-intrain,]


dim(Dataset_XY)
# [1] 296  15
dim(training)
# [1] 238  15
dim(testing)
# [1] 58 15


prop.table(table(training$Response))
#        0         1 
# 0.5238095 0.4761905 

prop.table(table(testing$Response))
#         0         1 
# 0.5210084 0.4789916 


################################################################
# All variables
################################################################

Model1 <- rpart(Response~.,data=training,method="class")
#Plot1
prp(Model1,type=2,extra="auto",nn = TRUE,branch=1,varlen=0,yesno=2)
#Plot2
rpart.plot(Model1, extra = 106)

prediction <- predict(Model1, testing, type = 'class')
confusion_matrix <- table(testing$Response, prediction)

accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
print(paste('Accuracy for the Model is', accuracy*100, 'Percent'))
# [1] "Accuracy for the Model is 68.9655172413793  Percent"










###########################################################
###########################################################
# Case 2: Basic Decision tree
# All Variables - Group 1 
###########################################################
###########################################################

# Creating training and testing dataset 80% and 20%
Dataset_XY_group1 <- Dataset_XY[MyDataset$Group==1,]
intrain<-createDataPartition(y=Dataset_XY_group1$Response,p=0.8,list=FALSE)
training<-Dataset_XY_group1[intrain,]
testing<-Dataset_XY_group1[-intrain,]

dim(Dataset_XY_group1)
# [1] 200  15
dim(training)
# [1] 161  15
dim(testing)
# [1] 39  15

prop.table(table(training$Response))
prop.table(table(testing$Response))


################################################################
# All variables
################################################################

Model2all <- rpart(Response~.,data=training,method="class")
#Plot1
prp(Model2all,type=2,extra="auto",nn = TRUE,branch=1,varlen=0,yesno=2)
#Plot2
rpart.plot(Model2all, extra = 106)

prediction <- predict(Model2all, testing, type = 'class')
confusion_matrix <- table(testing$Response, prediction)

accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
print(paste('Accuracy for the Model is', accuracy*100, 'Percent'))
# [1] "Accuracy for the Model is 53.8461538461538 Percent"


################################################################
# Y variables
################################################################

Model2y <- rpart(Response ~ Y1 + Y2 + Y3 + Y4 + Y5 + Y6 + Y7, data=training, method="class")
#Plot1
prp(Model2y,type=2,extra="auto",nn = TRUE,branch=1,varlen=0,yesno=2)
#Plot2
rpart.plot(Model2y, extra = 106)

prediction <- predict(Model2y, testing, type = 'class')
confusion_matrix <- table(testing$Response, prediction)

accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
print(paste('Accuracy for the Model is', accuracy*100, 'Percent'))
# [1] "Accuracy for the Model is 69.2307692307692 Percent"


################################################################
# X variables
################################################################

Model2x <- rpart(Response ~ X1 + X2 + X3 + X4 + X5 + X6 + X7, data=training, method="class")
#Plot1
prp(Model2x,type=2,extra="auto",nn = TRUE,branch=1,varlen=0,yesno=2)
#Plot2
rpart.plot(Model2x, extra = 106)

prediction <- predict(Model2x, testing, type = 'class')
confusion_matrix <- table(testing$Response, prediction)

accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
print(paste('Accuracy for the Model is', accuracy*100, 'Percent'))
# [1] "Accuracy for the Model is 53.8461538461538 Percent"










###########################################################
###########################################################
# Case 2: Basic Decision tree
# All Variables - Group 0
###########################################################
###########################################################

# Creating training and testing dataset 80% and 20%
Dataset_XY_group0 <- Dataset_XY[MyDataset$Group==0,]
intrain<-createDataPartition(y=Dataset_XY_group0$Response,p=0.8,list=FALSE)
training<-Dataset_XY_group0[intrain,]
testing<-Dataset_XY_group0[-intrain,]

dim(Dataset_XY_group0)
# [1] 96  15
dim(training)
# [1] 78  15
dim(testing)
# [1] 18  15

prop.table(table(training$Response))
prop.table(table(testing$Response))


################################################################
# All variables
################################################################

Model3all <- rpart(Response~.,data=training,method="class")
#Plot1
prp(Model3all,type=2,extra="auto",nn = TRUE,branch=1,varlen=0,yesno=2)
#Plot2
rpart.plot(Model3all, extra = 106)

prediction <- predict(Model3all, testing, type = 'class')
confusion_matrix <- table(testing$Response, prediction)

accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
print(paste('Accuracy for the Model is', accuracy*100, 'Percent'))
# [1] "Accuracy for the Model is 72.2222222222222 Percent"


################################################################
# Y variables
################################################################

Model3y <- rpart(Response ~ Y1 + Y2 + Y3 + Y4 + Y5 + Y6 + Y7, data=training, method="class")
#Plots
prp(Model3y,type=2,extra="auto",nn = TRUE,branch=1,varlen=0,yesno=2)
#Plot2
rpart.plot(Model3y, extra = 106)

prediction <- predict(Model3y, testing, type = 'class')
confusion_matrix <- table(testing$Response, prediction)

accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
print(paste('Accuracy for the Model is', accuracy*100, 'Percent'))
# [1] "Accuracy for the Model is 77.7777777777778 Percent"


################################################################
# X variables
################################################################

Model3x <- rpart(Response ~ X1 + X2 + X3 + X4 + X5 + X6 + X7, data=training, method="class")
#Plot1
prp(Model3x,type=2,extra="auto",nn = TRUE,branch=1,varlen=0,yesno=2)
#Plot2
rpart.plot(Model3x, extra = 106)

prediction <- predict(Model3x, testing, type = 'class')
confusion_matrix <- table(testing$Response, prediction)

accuracy <- sum(diag(confusion_matrix)) / sum(confusion_matrix)
print(paste('Accuracy for the Model is', accuracy*100, 'Percent'))
# [1] "Accuracy for the Model is 72.2222222222222 Percent"




