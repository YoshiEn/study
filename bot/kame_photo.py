

# coding: utf-8

from slacker import Slacker
import slackbot_settings

if __name__ == "__main__":
	slack = Slacker(slackbot_settings.API_TOKEN)import requests
import json
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use('Agg') # CUI環境でmatplotlib使いたい場合、指定する
import matplotlib.pyplot as plt

TOKEN = # 取得したトークン
CHANNEL = # チャンネルID

#####################################
# 画像を生成する例、アップロードするだけなら不要
#####################################

# データ読み込む
data = pd.read_table(
    "/path/to/data/input.tsv", #なんかtsv/csv読み込むサンプル
    header=-1, 
    names=("date","value")
)
# 軸の基準になるとこ
data.index = pd.to_datetime(data.iloc[:,0])
data.plot()
# 保存するよ
plt.savefig('figure.png')

###############
# 画像送信ここから
###############
files = {'file': open("figure.png", 'rb')}
param = {
    'token':TOKEN, 
    'channels':CHANNEL,
    'filename':"filename",
    'initial_comment': "initial_comment",
    'title': "title"
}
requests.post(url="https://slack.com/api/files.upload",params=param, files=files)