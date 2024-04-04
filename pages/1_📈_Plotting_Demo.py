import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Plotting Demo", page_icon="📈")  # 设置页面

st.markdown("# Plotting Demo") # 添加一级标题
st.sidebar.header("Plotting Demo")  # 在侧边栏添加一个标题
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

progress_bar = st.sidebar.progress(0)  # 创建了一个位于侧边栏的进度条组件，并初始化为0
status_text = st.sidebar.empty()  # 创建一个空的文本区域，用于显示处理进度的文本信息
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)  # 将新生成的数据添加到图表中，实现动他更新图表
    progress_bar.progress(i)  # 更新侧边栏的进度条，显示处理进度的百分比值
    last_rows = new_rows  # 更新last_rows为新的数据，在下次迭代中使用
    time.sleep(0.05) # 暂停0.05秒

progress_bar.empty()  # 最后清空进度条，表示任务完成

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")