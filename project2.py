from flask import Flask, render_template, request
from keras.models import load_model
import numpy as np
from joblib import load

app = Flask(__name__)

model = load_model('d:/data/project/')
scaler = load('d:/data/project/scaler.model')

@app.route('/', methods=['GET'])
def main():
    return render_template('project/input.html')

@app.route('/result', methods=['POST'])
def result():
    gender = request.form['gender']
    male, female, sex = get_gender_info(gender)

    region = request.form['region']
    region1, region2, region3, region4, region5, region6, region7, reg = get_region_info(region)

    education = request.form['education']
    education_level1, education_level2, education_level3, education_level4, education_level5, education_level6, education_level7, education_level8, education_level9, edu = get_education_info(education)

    # 나머지 필드에 대한 처리도 유사하게 작성합니다.

    test_set = np.array([wave, region1, region2, region3, region4, region5, region6, region7, family_member, year_born, education_level1, education_level2, education_level3, education_level4, education_level5, education_level6, education_level7, education_level8, education_level9, marriage1, marriage2, marriage3, marriage4, marriage5, marriage6, religion, company_size, reason_none_worker, male, female, income]).reshape(1, 31)
    test_set = scaler.transform(test_set)

    rate = model.predict(test_set)

    if rate >= 0.5:
        result = '평균이상'
    else:
        result = '평균이하'

    return render_template('project/result.html', rate='%.2f%%' % (rate[0][0] * 100), result=result, gender=sex, wave=wave, region=reg, family_member=family_member, year_born=year_born, education=edu, marriage=mar, company_size=company_size, reason_none_worker=reason_none_worker, income=income, religion=religion)

def get_gender_info(gender):
    if gender == '0':
        return 1, 0, '남성'
    else:
        return 0, 1, '여성'

def get_region_info(region):
    regions = {
        '0': (1, 0, 0, 0, 0, 0, 0, '서울'),
        '1': (0, 1, 0, 0, 0, 0, 0, '경기'),
        '2': (0, 0, 1, 0, 0, 0, 0, '경남'),
        '3': (0, 0, 0, 1, 0, 0, 0, '경북'),
        '4': (0, 0, 0, 0, 1, 0, 0, '충남'),
        '5': (0, 0, 0, 0, 0, 1, 0, '강원&충북'),
        '6': (0, 0, 0, 0, 0, 0, 1, '전라&제주')
    }
    return regions.get(region, (0, 0, 0, 0, 0, 0, 0, ''))

def get_education_info(education):
    educations = {
        '0': (1, 0, 0, 0, 0, 0, 0, 0, 0, '교육없음(7세미만)'),
        '1': (0, 1, 0, 0, 0, 0, 0, 0, 0, '교육없음(7세이상)'),
        '2': (0, 0, 1, 0, 0, 0, 0, 0, 0, '초등학교'),
        '3': (0, 0, 0, 1, 0, 0, 0, 0, 0, '중학교'),
        '4': (0, 0, 0, 0, 1, 0, 0, 0, 0, '고등학교'),
        '5': (0, 0, 0, 0, 0, 1, 0, 0, 0, '전문대'),
        '6': (0, 0, 0, 0, 0, 0, 1, 0, 0, '대학'),
        '7': (0, 0, 0, 0, 0, 0, 0, 1, 0, '석사'),
        '8': (0, 0, 0, 0, 0, 0, 0, 0, 1, '박사')
    }
    return educations.get(education, (0, 0, 0, 0, 0, 0, 0, 0, 0, ''))

# 나머지 함수도 유사하게 작성합니다.

if __name__ == '__main__':
    app.run(port=8003, threaded=False)
