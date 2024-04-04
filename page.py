import streamlit as st

# 创建侧边栏菜单
menu = ['首页','页面1','页面2']

# 在侧边栏中添加下拉菜单
choice = st.sidebar.selectbox('选择一个页面',menu)

# 根据用户选择的页面，显示相应的内容
if choice == '首页':
    st.write('这是首页')
elif choice == '页面1':
    st.write('这是页面1')
else:
    st.write('这是页面2')

import webbrowser

# # 创建一个按钮和链接
if st.button('打开新页面'):
     url = 'http://www.baidu.com'
     webbrowser.open_new(url)