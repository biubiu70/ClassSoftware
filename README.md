# 课程设计

### 01、划分数据集

使用anaconda软件，创建labelme环境，下载labelme的tools，给数据集打标签



### 02、搭建python环境

创建mmlab环境，下载算法所要求的requiremen.txt中所有支持的包，一步一步修改报错，解决问题



### 03、训练模型

在给定的附件中，使用命令训练自己的模型，工具有限，只用cpu

训练出模型后进行检测，检测IOU等结果



### 04、设计自己的软件

QTdesigner 设计UI文件，生成main.ui，然后将UI文件转换为py文件继续添加自己的功能：

```bash
pyuic5 -x main.ui -o main.py
```











### 05、开源软件修改



1. 修改apprcc.qrc为py























> 小白上手改的方法：
>
> 1、在conda终端输入Designer打开QT设计师界面，
>
> 2、打开后点击右下角铅笔符号，打开apprcc.qrc文件。修改想修改的地方后保存。
>
> 3、在conda终端，打开apprcc.qrc所在的文件路径，然后输入`pyrcc5 apprcc.qrc -o apprcc.py`，会把qrc资源文件，转换成py文件。
>
> 4、在qt设计师界面保存win.UI,然后通过代码转换成py文件







#### 学习网站

1. [PyQt-Chinese-tutorial](https://github.com/maicss/PyQt-Chinese-tutorial)
2. [PyQt5-YOLOv5](https://github.com/Javacr/PyQt5-YOLOv5)