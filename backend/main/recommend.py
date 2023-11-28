import pandas as pd
import tabulate
import os
import pathlib


PATH = pathlib.Path(__file__).parent.parent

df = pd.read_csv(os.path.join(PATH, '음식분류.csv'),encoding='UTF-8') # csv 파일 읽어오기

data = df[['분류', '음 식 명', '나트륨']] # 필요한 데이터만 가져오기

from sklearn.feature_extraction.text import CountVectorizer

data['분류'].fillna('', inplace=True)
cv = CountVectorizer(ngram_range=(1,1))
cv_category = cv.fit_transform(data['분류'])
cv.vocabulary_ # 카테고리별 인덱스 번호

from sklearn.metrics.pairwise import cosine_similarity
similarity_category = cosine_similarity(cv_category, cv_category).argsort()[:,::-1]
print(similarity_category)
similarity_category.shape

def recommend_menu(df, menu_name, top=10):
	target_menu_idx = df[df['음 식 명'] == menu_name].index.values

	sim_idx = similarity_category[target_menu_idx, :top].reshape(-1)
	sim_idx = sim_idx[sim_idx != target_menu_idx]

	result = df.iloc[sim_idx]
	result = result.sort_values(by='나트륨', ascending=True)

	return result

for i in range(len(data)): # ,가 포함되거나 한 글자인 카테고리명 변경 / 문자가 있거나 한 글자인 음식명 변경
    if pd.notnull(data['분류'][i]):
        if (',' in data['분류'][i]):
            data.loc[i, "분류"] = data['분류'][i].replace(',', '_')

        if (len(data['분류'][i]) == 1):
            data.loc[i, "분류"] = data['분류'][i] + "_"

    if pd.notnull(data['음 식 명'][i]):
        if (len(data['음 식 명'][i]) == 1):
            data.loc[i, "음 식 명"] = data['음 식 명'][i] + "_"

        if (" / " in data['음 식 명'][i]):
            data.loc[i, "음 식 명"] = data['음 식 명'][i].replace(" / ", '_')

        if ("/" in data['음 식 명'][i]):
            data.loc[i, "음 식 명"] = data['음 식 명'][i].replace("/", '_')

from tabulate import tabulate

# recommend_menu 함수를 사용하여 데이터프레임을 가져옵니다.
recommended = recommend_menu(data, '치킨가스', top=10)

# '나트륨'을 기준으로 데이터프레임을 정렬합니다.
sorted_recommended = recommended[['음 식 명', '나트륨']].sort_values(by='나트륨')

# tabulate를 사용하여 표 형식으로 출력합니다.
table = tabulate(sorted_recommended, headers='keys', tablefmt='pretty')
print(table)