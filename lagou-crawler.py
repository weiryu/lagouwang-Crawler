# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:32:54 2018

@author: weir
"""

import requests
import re
import time
import pandas as pd
import random
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt # 绘图
import jieba # 分词
from wordcloud import WordCloud # 词云可视化
import matplotlib as mpl  
from pyecharts import Geo # 地理图
mpl.rcParams["font.sans-serif"] = ["SimHei"] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 配置绘图风格
plt.rcParams["axes.labelsize"] = 16.   
plt.rcParams["xtick.labelsize"] = 14.
plt.rcParams["ytick.labelsize"] = 14.
plt.rcParams["legend.fontsize"] = 12.
plt.rcParams["figure.figsize"] = [15., 15.]


def get_url_data(url,file_path):
    # 反爬措施
    # 需根据网址改变的header项目：host，referer，cookie
    header = {'Host': 'www.lagou.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,en-US;q=0.7,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.lagou.com/jobs/list_Python?labelWords=&fromSearch=true&suginput=',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Anit-Forge-Token': 'None',
    'X-Anit-Forge-Code': '0',
    'Content-Length': '26',
    'Cookie': 'user_trace_token=20180306224759-5d29331b-214d-11e8-b12d-5254005c3644; _ga=GA1.2.1102801823.1520347681; LGUID=20180306224759-5d293805-214d-11e8-b12d-5254005c3644; JSESSIONID=ABAAABAACBHABBIBB9765B18C9281605588F2C5D5FC89CF; _gat=1; LGSID=20171228225143-9edb51dd-ebde-11e7-b670-525400f775ce; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DKkJPgBHAnny1nUKaLpx2oDfUXv9ItIF3kBAWM2-fDNu%26ck%3D3065.1.126.376.140.374.139.129%26shh%3Dwww.baidu.com%26sht%3Dmonline_3_dg%26wd%3D%26eqid%3Db0ec59d100013c7f000000055a4504f6; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; LGRID=20171228225224-b6cc7abd-ebde-11e7-9f67-5254005c3644; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; SEARCH_ID=3ec21cea985a4a5fa2ab279d868560c8',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'}
    
    for n in range(1,30):    
        # 要提交的数据，需根据F12获得的参数中表单的值变化
        print("正在爬取第%d页"%(n))
        form = {'first':'false',
                'kd':'Python',
                'pn':str(n)}    
        # 每次提交时休眠，限制爬取速度，应对反爬虫
        time.sleep(random.randint(2,5))
        
        # 提交数据
        html = requests.post(url,data=form,headers = header)    
        print(html.text)
        html_texts = html.text.split("result")[1:]
        for texts in html_texts:        
            # 提取数据
            company_id_data = re.findall('{"companyId":(.*?),',texts)
            company_number = len(company_id_data)
            
            if company_number > 0:                
                company_shortName_data = re.findall('"companyShortName":"(.*?)",',texts)
                temp_number = len(company_shortName_data)
                if temp_number != company_number:
                    print("There is a problem in company shortName data")
                
                company_industryField_data = re.findall('"industryField":"(.*?)",',texts)
                temp_number = len(company_industryField_data)
                if temp_number != company_number:
                    print("There is a problem in company industryField data")
            
                company_workYear_data = re.findall('"workYear":"(.*?)",',texts)
                temp_number = len(company_workYear_data)
                if temp_number != company_number:
                    print("There is a problem in company workYear data")
            
                company_education_data = re.findall('"education":"(.*?)",',texts)
                temp_number = len(company_education_data)
                if temp_number != company_number:
                    print("There is a problem in company education data")
            
                company_city_data = re.findall('"city":"(.*?)",',texts)
                temp_number = len(company_city_data)
                if temp_number != company_number:
                    print("There is a problem in company city data")
            
                company_salary_data = re.findall('"salary":"(.*?)",',texts)
                temp_number = len(company_salary_data)
                if temp_number != company_number:
                    print("There is a problem in company salary data")
            
                company_financeStage_data = re.findall('"financeStage":"(.*?)",',texts)
                temp_number = len(company_financeStage_data)
                if temp_number != company_number:
                    print("There is a problem in company financeStage data")      
                
                company_positionName_data = re.findall('"positionName":"(.*?)",',texts)
                temp_number = len(company_positionName_data)
                if temp_number != company_number:
                    print("There is a problem in company positionName data")
                
                company_jobNature_data = re.findall('"jobNature":"(.*?)",',texts)
                temp_number = len(company_jobNature_data)
                if temp_number != company_number:
                    print("There is a problem in company jobNature data")
                    
                company_size_data = re.findall('"companySize":"(.*?)",',texts)
                temp_number = len(company_size_data)
                if temp_number != company_number:
                    print("There is a problem in company size data")                 
    
                company_LabelList_data = re.findall('"companyLabelList":[[](.*?)[]],',texts)
                temp_number = len(company_LabelList_data)
                if temp_number != company_number:
                    print("There is a problem in company LabelList data") 
                    
                """
                ### 测试使用
                print(company_id_data) 
                print(company_shortName_data)
                print(company_industryField_data)
                print(company_workYear_data)
                print(company_education_data)
                print(company_city_data)
                print(company_salary_data)
                print(company_financeStage_data)
                print(company_positionName_data)
                print(company_jobNature_data)
                print(company_size_data)
                print(company_LabelList_data)
                """                
                
                # 转换成数据框    
                company_id_dataframe = pd.DataFrame(company_id_data)
                company_shortName_dataframe = pd.DataFrame(company_shortName_data)
                company_industryField_dataframe = pd.DataFrame(company_industryField_data)
                company_workYear_dataframe = pd.DataFrame(company_workYear_data)
                company_education_dataframe = pd.DataFrame(company_education_data)
                company_city_dataframe = pd.DataFrame(company_city_data)
                company_salary_dataframe = pd.DataFrame(company_salary_data)
                company_financeStage_dataframe = pd.DataFrame(company_financeStage_data)
                company_positionName_dataframe = pd.DataFrame(company_positionName_data)
                company_jobNature_dataframe = pd.DataFrame(company_jobNature_data)
                company_size_dataframe = pd.DataFrame(company_size_data)
                company_LabelList_dataframe = pd.DataFrame(company_LabelList_data)
            
                temp_result = pd.concat([company_id_dataframe, company_shortName_dataframe,company_industryField_dataframe,\
                        company_workYear_dataframe,company_education_dataframe,company_city_dataframe,company_salary_dataframe,\
                        company_financeStage_dataframe,company_positionName_dataframe,company_jobNature_dataframe,company_size_dataframe,\
                        company_LabelList_dataframe], axis=1)
                # print(temp_result) 
                if n==1:
                    result = temp_result
                else:
                    result = pd.concat([result,temp_result],axis=0)
            else:
                pass
        
    header_name = ["id","公司名称","公司领域","工作经验","学历要求","工作城市","工资","融资阶段","职位","工作类型","公司规模","工作福利"]
    # 保存在本地
    result.to_csv(file_path,header = header_name, index = False, mode = 'w+')

def data_wordcloud(file_path):
    data = pd.read_csv(file_path,encoding='gbk')  # 导入数据
    """
    ### 测试代码
    print(data.head())
    print(data.tail())
    print(type(data['工作城市'].value_counts()))
    print(data['工作城市'].value_counts().size)
    ###
    """
    print(data.head())
    data['学历要求'].value_counts().plot(kind='bar',rot=0)
    plt.show()
    data['工作经验'].value_counts().plot(kind='bar',rot=0,color='b')
    plt.show()
    data['工作城市'].value_counts().plot(kind='pie',autopct='%1.2f%%',explode = np.linspace(0,0.5,data['工作城市'].value_counts().size))
    plt.show()

    # eval(re.split('k|K',data['工资'][x])[0]）*1000 获得最低工资。
    # lambda x:(data['工作城市'][x],eval(re.split('k|K',data['工资'][x])[0])*1000) 对于每个获得的x都这么做，获得所有项的最低工资。
    # map(lambda x:(data['工作城市'][x],eval(re.split('k|K',data['工资'][x])[0])*1000),range(len(data))) 。
    # eval函数负责将括号中的东西转化成为可以计算的数值。
    # lambda x：y 输入x输出y 
    # map（f，x）表示将函数f应用到所有的x（x为list）上，获得新list
    data2 = list(map(lambda x:(data['工作城市'][x],eval(re.split('k|K',data['工资'][x])[0])*1000),range(len(data))))
    # 提取价格信息
    print(data2)
    data3 = pd.DataFrame(data2)
    print(data3.groupby(0).mean())
    # 转化成Geo需要的格式
    data4 = list(map(lambda x:(data3.groupby(0).mean()[1].index[x],data3.groupby(0).mean()[1].values[x]),range(len(data3.groupby(0)))))
    # 地理位置展示
    geo = Geo("全国Python最低工资布局", "制作人:weirryu", title_color="#fff", title_pos="left", width=1200, height=600,
    background_color='#404a59')
    attr, value = geo.cast(data4)
    geo.add("", attr, value, type="heatmap", is_visualmap=True, visual_range=[0, 300], visual_text_color='#fff')
    # 中国地图Python工资，此分布是最低薪资
    # geo.show_config()
    geo.render(r"C:\\Users\\weir\\Desktop\\result.html")

if __name__=="__main__":
    # 搜索请求post的网址
    url = "https://www.lagou.com/jobs/positionAjax.json?needAdd=tionalResult=false&isSchoolJob=0"
    file_path = r'C:\\Users\\weir\\Desktop\\LaGouDataMatlab.csv'
    get_url_data(url,file_path)
    data_wordcloud(file_path)

    
    