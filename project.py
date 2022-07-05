from flask import  Flask, render_template,request
from keras.models import  load_model
import numpy as np
from  joblib import load

app = Flask(__name__)

@app.route('/',methods = ['GET'])
def main():
    return  render_template('project/input.html')

@app.route('/result',methods = ['POST'])
def result():
    model = load_model('d:/data/project/')
    gender = request.form['gender']
    if gender == '0':
        male = 1
        female = 0
        sex = '남성'
    else:
        male = 0
        female = 1
        sex = '여성'
    region = request.form['region']
    if region == '0':
        region1 = 1
        region2 = 0
        region3 = 0
        region4 = 0
        region5 = 0
        region6 = 0
        region7 = 0
        reg = '서울'
    elif region == '1' :
        region1 = 0
        region2= 1
        region3 = 0
        region4 = 0
        region5 = 0
        region6 = 0
        region7  = 0
        reg = '경기'
    elif region == '2' :
        region1 = 0
        region2 = 0
        region3 = 1
        region4 = 0
        region5 = 0
        region6 = 0
        region7  = 0
        reg = '경남'
    elif region == '3' :
        region1 = 0
        region2= 0
        region3 = 0
        region4 = 1
        region5 = 0
        region6 = 0
        region7  = 0
        reg = '경북'
    elif region == '4' :
        region1 = 0
        region2= 0
        region3 = 0
        region4 = 0
        region5 = 1
        region6 = 0
        region7  = 0
        reg = '충남'
    elif region == '5' :
        region1 = 0
        region2= 0
        region3 = 0
        region4 = 0
        region5 = 0
        region6 = 1
        region7  = 0
        reg = '강원&충북'
    elif region == '6' :
        region1 = 0
        region2= 0
        region3 = 0
        region4 = 0
        region5 = 0
        region6 = 0
        region7 = 1
        reg = '전라&제주'
        #region == '6':
        # region = 3
    education = request.form['education']
    if education == '0':
        education_level1 = 1
        education_level2 = 0
        education_level3 = 0
        education_level4 = 0
        education_level5 = 0
        education_level6 = 0
        education_level7 = 0
        education_level8 = 0
        education_level9 = 0
        edu = '교육없음(7세미만)'
    elif education == '1':
        education_level1 = 0
        education_level2 = 1
        education_level3 = 0
        education_level4 = 0
        education_level5 = 0
        education_level6 = 0
        education_level7 = 0
        education_level8 = 0
        education_level9 = 0
        edu = '교육없음(7세이상)'
    elif education == '2':
        education_level1 = 0
        education_level2 = 0
        education_level3 = 1
        education_level4 = 0
        education_level5 = 0
        education_level6 = 0
        education_level7 = 0
        education_level8 = 0
        education_level9 = 0
        edu = '초등학교'
    elif education == '3':
        education_level1 = 0
        education_level2 = 0
        education_level3 = 0
        education_level4 = 1
        education_level5 = 0
        education_level6 = 0
        education_level7 = 0
        education_level8 = 0
        education_level9 = 0
        edu = '중학교'
    elif education == '4':
        education_level1 = 0
        education_level2 = 0
        education_level3 = 0
        education_level4 = 0
        education_level5 = 1
        education_level6 = 0
        education_level7 = 0
        education_level8 = 0
        education_level9 = 0
        edu = '고등학교'
    elif education == '5':
        education_level1 = 0
        education_level2 = 0
        education_level3 = 0
        education_level4 = 0
        education_level5 = 0
        education_level6 = 1
        education_level7 = 0
        education_level8 = 0
        education_level9 = 0
        edu = '전문대'
    elif education == '6':
        education_level1 = 0
        education_level2 = 0
        education_level3 = 0
        education_level4 = 0
        education_level5 = 0
        education_level6 = 0
        education_level7 = 1
        education_level8 = 0
        education_level9 = 0
        edu = '대학'
    elif education == '7':
        education_level1 = 0
        education_level2 = 0
        education_level3 = 0
        education_level4 = 0
        education_level5 = 0
        education_level6 = 0
        education_level7 = 0
        education_level8 = 1
        education_level9 = 0
        edu = '석사'
    elif education == '8':
        education_level1 = 0
        education_level2 = 0
        education_level3 = 0
        education_level4 = 0
        education_level5 = 0
        education_level6 = 0
        education_level7 = 0
        education_level8 = 0
        education_level9 = 1
        edu = '박사'
    marriage = request.form['marriage']
    if marriage == '0':
        marriage1 = 1
        marriage2 = 0
        marriage3 = 0
        marriage4 = 0
        marriage5 = 0
        marriage6 = 0
        mar = '해당 사항 없음(18세 미만)'
    elif marriage == '1':
        marriage1 = 0
        marriage2 = 1
        marriage3 = 0
        marriage4 = 0
        marriage5 = 0
        marriage6 = 0
        mar = '기혼'
    elif marriage == '2':
        marriage1 = 0
        marriage2 = 0
        marriage3 = 1
        marriage4 = 0
        marriage5 = 0
        marriage6 = 0
        mar = '사망으로 별거'
    elif marriage == '3':
        marriage1 = 0
        marriage2 = 0
        marriage3 = 0
        marriage4 = 1
        marriage5 = 0
        marriage6 = 0
        mar = '별거'
    elif marriage == '4':
        marriage1 = 0
        marriage2 = 0
        marriage3 = 0
        marriage4 = 0
        marriage5 = 1
        marriage6 = 0
        mar = '별거'
    elif marriage == '5':
        marriage1 = 0
        marriage2 = 0
        marriage3 = 0
        marriage4 = 0
        marriage5 = 0
        marriage6 = 1
        mar = '기타'
    religion = int(request.form['religion'])
    wave = int(request.form['wave'])
    family_member = int(request.form['family_member'])
    year_born = int(request.form['year_born'])
    company_size = int(request.form['company_size'])
    reason_none_worker = int(request.form['reason_none_worker'])
    income = int(request.form['income'])
    test_set = np.array([wave, region1, region2, region3, region4, region5,region6, region7, family_member, year_born, education_level1, education_level2, education_level3, education_level4, education_level5, education_level6, education_level7, education_level8, education_level9, marriage1, marriage2,marriage3, marriage4, marriage5, marriage6, religion,company_size, reason_none_worker, male, female,income]).reshape(1,31)

    scaler = load('d:/data/project/scaler.model')
    test_set = scaler.transform(test_set)

    rate= model.predict(test_set)



    if rate >=0.5:
        result = '평균이상'
    else:
        result = '평균이하'
    return  render_template('project/result.html',rate = '{:.2f}%'.format(rate[0][0]*100),result=result, gender=sex,wave=wave,region=reg,family_member=family_member,year_born=year_born,education=edu,marriage=mar,company_size=company_size,reason_none_worker=reason_none_worker,income=income,religion=religion)

if __name__ == '__main__':
    app.run(port=8003, threaded=False)