# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 10:01:10 2018

@author: lxl
"""

import operator
from math import log

def createDataSet():
	dataSet  = [[5, 1, 1, 1, 2, 1, 3, 1, 1, 2],
                [5, 4, 4, 5, 7, 10, 3, 2, 1, 2],
                [3, 1, 1, 1, 2, 2, 3, 1, 1, 2],
                [6, 8, 8, 1, 3, 4, 3, 7, 1, 2],
                [4, 1, 1, 3, 2, 1, 3, 1, 1, 2],
                [8, 10, 10, 8, 7, 10, 9, 7, 1, 4],
                [1, 1, 1, 1, 2, 10, 3, 1, 1, 2],
                [2, 1, 2, 1, 2, 1, 3, 1, 1, 2],
                [2, 1, 1, 1, 2, 1, 1, 1, 5, 2],
                [4, 2, 1, 1, 2, 1, 2, 1, 1, 2],
                [1, 1, 1, 1, 1, 1, 3, 1, 1, 2],
                [2, 1, 1, 1, 2, 1, 2, 1, 1, 2],
                [5, 3, 3, 3, 2, 3, 4, 4, 1, 4],
                [1, 1, 1, 1, 2, 3, 3, 1, 1, 2],
                [8, 7, 5, 10, 7, 9, 5, 5, 4, 4],
                [7, 4, 6, 4, 6, 1, 4, 3, 1, 4],
                [4, 1, 1, 1, 2, 1, 2, 1, 1, 2],
                [4, 1, 1, 1, 2, 1, 3, 1, 1, 2],
                [10, 7, 7, 6, 4, 10, 4, 1, 2, 4],
                [6, 1, 1, 1, 2, 1, 3, 1, 1, 2],
                [7, 3, 2, 10, 5, 10, 5, 4, 4, 4],
                [10, 5, 5, 3, 6, 7, 7, 10, 1, 4],
                [3, 1, 1, 1, 2, 1, 2, 1, 1, 2]]


	labels = ['CI.thickness', 'Cell.size', 'Cell.shape','Marg.adhesion','Epith.c.size','Bare.nuclei','BI.cromatin','Normal.nucleioli','Mitoses']  #特征标签
	return dataSet, labels 							#返回数据集和分类属性

#计算经验熵
def calcShannonEnt(dataSet):
	numEntires = len(dataSet)						#返回数据集的行数
	labelCounts = {}								#保存每个标签(Label)出现次数的字典
	for featVec in dataSet:							#对每组特征向量进行统计
		currentLabel = featVec[-1]					#提取标签(Label)信息
		if currentLabel not in labelCounts.keys():	#如果标签(Label)没有放入统计次数的字典,添加进去
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1				#Label计数
	shannonEnt = 0.0								#经验熵(香农熵)
	for key in labelCounts:							#计算香农熵
		prob = float(labelCounts[key]) / numEntires	#选择该标签(Label)的概率
		shannonEnt -= prob * log(prob, 2)			#利用公式计算
	return shannonEnt


# if __name__ == '__main__':
#     dataSet,deatures = createDataSet()
#     print(dataSet)
#     print(calcShannonEnt(dataSet))




#按照给定特征划分数据集
def splitDataSet(dataSet, axis, value):
	retDataSet = []										#创建返回的数据集列表
	for featVec in dataSet: 							#遍历数据集
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]				#去掉axis特征
			reducedFeatVec.extend(featVec[axis+1:]) 	#将符合条件的添加到返回的数据集
			retDataSet.append(reducedFeatVec)
	return retDataSet

#选择最优特征
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1					#特征数量
	baseEntropy = calcShannonEnt(dataSet) 				#计算数据集的香农熵
	bestInfoGain = 0.0  								#信息增益
	bestFeature = -1									#最优特征的索引值
	for i in range(numFeatures): 						#遍历所有特征
		#获取dataSet的第i个所有特征
		featList = [example[i] for example in dataSet]
		uniqueVals = set(featList)     					#创建set集合{},元素不可重复
		newEntropy = 0.0  								#经验条件熵
		for value in uniqueVals: 						#计算信息增益
			subDataSet = splitDataSet(dataSet, i, value) 		#subDataSet划分后的子集
			prob = len(subDataSet) / float(len(dataSet))   		#计算子集的概率
			newEntropy += prob * calcShannonEnt(subDataSet) 	#根据公式计算经验条件熵
		infoGain = baseEntropy - newEntropy 					#信息增益
		# print("第%d个特征的增益为%.3f" % (i, infoGain))			#打印每个特征的信息增益
		if (infoGain > bestInfoGain): 							#计算信息增益
			bestInfoGain = infoGain 							#更新信息增益，找到最大的信息增益
			bestFeature = i 									#记录信息增益最大的特征的索引值
	return bestFeature

# if __name__ == '__main__':
#     dataSet,features = createDataSet()
#     print("最有特征索引：" + str(chooseBestFeatureToSplit(dataSet)))

# 统计classList中出现此处最多的元素(类标签)
def majorityCnt(classList):
    classCount = {}      #{2: 16, 4: 7}
    for vote in classList:                                        #统计classList中每个元素出现的次数
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)        #根据字典的值降序排序   [(2, 16), (4, 7)]
    return sortedClassCount[0][0]                                #返回classList中出现次数最多的元素   2

# 建树
def createTree(dataSet, labels, featLabels):
	classList = [example[-1] for example in dataSet]			#取分类标签(是否放贷:yes or no)  #{2: 16, 4: 7}
	if classList.count(classList[0]) == len(classList):			#如果类别完全相同则停止继续划分
		return classList[0]
	if len(dataSet[0]) == 1:									#遍历完所有特征时返回出现次数最多的类标签
		return majorityCnt(classList)     #2
	bestFeat = chooseBestFeatureToSplit(dataSet)				#选择最优特征   6
	bestFeatLabel = labels[bestFeat]#最优特征的标签   'BI.cromatin'
	featLabels.append(bestFeatLabel)
	myTree = {bestFeatLabel:{}}									#根据最优特征的标签生成树
	del(labels[bestFeat])										#删除已经使用特征标签
	featValues = [example[bestFeat] for example in dataSet]		#得到训练集中所有最优特征的属性值
	uniqueVals = set(featValues)								#去掉重复的属性值
	for value in uniqueVals:									#遍历特征，创建决策树。
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), labels, featLabels)
	return myTree

if __name__ == '__main__':
    dataSet,labels = createDataSet()
    featlabels = []
    myTree = createTree(dataSet,labels,featlabels)
    print(myTree)



















