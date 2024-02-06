grade = ["10","11","12"]
subject = ["mathematics", "englishhl","afrikaansfal","mathematicalliteracy","lifeorientation","physicalsciences","history","lifesciences","computerapplicationstechnology","informationtechnology","accounting","business","geography"]
province = ["gauteng","easterncape","kwazulunatal","westerncape","northwest","northerncape","limpopo","mpumalanga","freestate"]
year = ["2010", "2011","2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
month = ["june","november"]
paper = ["paper1","memo1","paper2","memo2"]

for g in grade:
  for s in subject:
    for v in province:
      for y in year:
          for m in month:
              for p in paper:
                  print(g + "/" + s + "/" + v + "/" + y + "/" + m + "/" + p)
