# Decision-tree
code of ID3、CART 
  
ID3:main function introduce 

1. 计算经验熵：def calcShannonEnt(dataSet)
2. 计算信息增益

     def splitDataSet(dataSet, axis, value):按照给定特征划分数据集
     
     def chooseBestFeatureToSplit(dataSet):计算信息增益
3. 统计classList中出现此处最多的元素(类标签)： def majorityCnt(classList)

4. 建树：def majorityCnt(classList):def createTree(dataSet, labels, featLabels)


CART:main function introduce

1. 载入数据:def loadDataSet(self, fileName)

2. 切分数据集为两个子集: def binSplitDataSet(dataSet, feature, value)

3. 二元切分: def chooseBestSplit(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4))

4. 构建tree: def createTree(dataSet, leafType=regLeaf, errType=regErr, ops=(1,4))






