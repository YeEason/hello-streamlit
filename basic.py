############## 文本组件  ########################
import streamlit as st
print(st.__version__)  # 查看版本：1.32.1

st.title(':tongue:👅文本组件text')  # 网页标题
st.header(':ghost:一级标题')  # 一级标题
st.subheader('二级标题')  # 二级标题
st.write('hello')  # 文本内容1
st.text('''
    可以写很多东西，这些东西都是随便写，随意的复制都是可以的
    你想写都可以
''')     # 文本内容2
st.markdown('''
    这里的内容喝markdown是一样的
    - 比如
''')    # markdown

st.code('print("hello world")')  # 代码格式
st.latex('y = w*x + b')   # 数学公式


############## 数据组件  ########################
st.title('数据组件')

import pandas as pd
data = pd.read_csv('data/titanic_data.csv')
st.dataframe(data)   # 交互表格
# st.table(data)       # 静态表格

st.metric('温度','23°C',delta='-2°C')  # 温度上升下降显示

col1,col2 = st.columns(2) # 分为两列显示
with col1:
    st.metric('温度','23°C',delta='-2°C')
with col2:
    st.metric('温度','23°C',delta='2°C')


############## 图表组件  ########################
# 自带
import numpy as np
data = np.random.random((30,4))
st.line_chart(data)   # 折线图（功能参数较少）
st.area_chart(data)   # 面积图
st.map(pd.DataFrame([[23,113]],columns=['lat','lon']))  # 标记地图，纬度和经度
# 第三方库
import matplotlib.pyplot as plt
fig, [ax1,ax2] = plt.subplots(2)  # 定义画布（两个子图）
ax1.plot(data[:,0])
ax1.set_title('test1')
ax2.plot(data[:,1])
ax2.set_title('test2')
plt.subplots_adjust(hspace=0.5)  # 子图间距调整

st.pyplot(fig)

############## 多媒体组件  ########################
# 图片（本地图片或网页图片）
img = plt.imread('pic/aixin.jpg')
st.image(img)

st.image('https://ts1.cn.mm.bing.net/th/id/R-C.6b5df1bfe0e4778a44dba0753cd169c8?rik=QRQIMqvjWRCO5Q&riu=http%3a%2f%2fpic39.nipic.com%2f20140321%2f8857347_232251363165_2.jpg&ehk=7oAaMo6LCHJc%2bqpQ0IPvcH7v69jGRQhb2vDz%2fOd5720%3d&risl=&pid=ImgRaw&r=0')

# 音频
with open('music/稻香-周杰伦.mp3','rb') as f:  # rb以二进制形式读取文件
    au = f.read()
st.audio(au)

# 视频
with open('video/开不了口-广告曲.mp4','rb') as f:
    a = f.read()
st.video(a)

############## 其他输入组件  ########################
# 1 可选择上传的图像
st.title('输入组件')
img = st.file_uploader('上传图像')  # 文件上传
st.image(img)  # 需要上传图像之后，才能去除报错

# 2 可使用电脑摄像头拍照
st.camera_input('调用电脑摄像头')

# 3 侧边栏
st.sidebar.write('welcome')  # 添加侧边栏

if st.sidebar.button('打招呼'):  # 添加按钮
    st.write('hello')
if st.sidebar.button('告别'):
    st.write('bye')

with open('video/最长的电影-广告曲.mp4','rb') as f:
    au = f.read()
st.video(au)