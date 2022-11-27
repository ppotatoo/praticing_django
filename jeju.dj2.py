from urllib.parse import urlencode
from urllib.request import urlopen
import json
import csv

url = 'http://apis.data.go.kr/B551939/jejuwaterdata1/rain1'

f = open("./data.csv", 'w', newline='')
csv_writer = csv.writer(f, delimiter=',')
csv_writer.writerow(['위치','년도','평균기온'])

for pageNo in range(1,5):
    input_json = {'pageSize' : '10',
                      'pageNo' : pageNo,
                      'returnType' : 'json',
                      'searchObservatory' : '대정',
                      'searchColleteType' : '',
                      'searchDataDate' : ''
        }


    queryParams = '?' + urlencode(input_json)
    response_body = urlopen(url + queryParams + '&ServiceKey=0Fu9Z5Pqs1ZE7dRq092g6CvbEBIgLeu6AU9%2FtJy0ETZN4CXiLIKZQB53zT0C%2B2r3zMbPFJ14t8VyF3XV0RlL3Q%3D%3D').read().decode('utf-8')
    print(response_body)
    json_data = json.loads(response_body)
    items = json_data['response']['body']['items']['item']

    f = open("./data.csv", 'a', newline='')
    csv_writer = csv.writer(f, delimiter=',')



    for item in items:
        onerow = []
        onerow.append(item['observatory'])
        onerow.append(item['dataDate'])
        onerow.append(item['val'])
        csv_writer.writerow(onerow)
    f.close()
