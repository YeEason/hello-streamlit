import streamlit as st
import pandas as pd

# 通过不同的输入组件获取用户的个人信息
st.set_page_config(page_title='获取用户的个人信息',page_icon='🍦')  # 修改网页信息
st.title('收集用户的个人信息')    # 添加标题
st.subheader("所有字段均为必填字段，填完才能提交哦！")

with st.form('report'):  # 构建为表单（例如：登录）,后面连接提交按钮
    name = st.text_input('姓名:')
    age = st.number_input('年龄:',min_value=0,max_value=120,format='%d')
    gender = st.selectbox('性别:',["男","女"])
    # 所有城市选项
    cities = ["北京", "上海", "广州", "深圳", "杭州", "成都", "重庆", "武汉", "南京", "其他"]
    city = st.selectbox("现居住城市:", cities)
    if city == "其他":
        city = st.text_input('请输入其他城市:')
    email = st.text_input('邮箱:')
    phone = st.text_input('手机号:',max_chars=11)
    # 检查手机号码是否为11位数
    if len(phone) != 11:
        st.error('请输入11位数的手机号')

    res = [[name,age,gender,city,email,phone]]  # 将填写的内容进行保存

    if st.form_submit_button('提交问卷'):  # 添加提交按钮（一般添加判断）
        if not all([name,email,city,phone]):
            st.error("请填写所有必填字段")
        else:
            data = pd.DataFrame(res,columns=['姓名','年龄','性别','现居住城市','邮箱','手机号'])
            data.to_csv('report.csv',encoding='utf-8-sig',mode='a')
            st.write('感谢您的参与！')  # 点击提交按钮后，输出此内容
            st.balloons()  # 飘起气球

            with st.expander('是否查看数据'):  # 数据展开组件：是否展开数据
                st.dataframe(data)
