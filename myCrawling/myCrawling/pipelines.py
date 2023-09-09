from itemadapter import ItemAdapter
import pymysql
import re

# Connect to the database
class MycrawlingPipeline:
    def open_spider(self, spider):
        self.connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     database='crawling',
                                     cursorclass=pymysql.cursors.DictCursor)
        self.cursor=self.connection.cursor()
    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()


    def process_item(self, item, spider):
        # 工作
        item["job"]=re.findall("\w+",item.get("job",""))[0]
        # 城市
        item["city"] = re.findall("\w+", item.get("city"))[0]
        # 工作经验
        result = re.findall("\d+\.{0,1}\d*", item["workage"])
        item["workage"]=(float(result[0])+float(result[1]))/2 if len(result)>0 else 0
        #  学历
        eduType = {"大专": 1, "本科": 2, "硕士": 3, "博士": 4}
        item["education"] = eduType.get(item["education"]) or "其他"
        # 技术
        item["skill"] = ",".join(item["skill"])
        # 薪资
        salaryType = re.findall("(千|万)", item["salary"])
        if (len(salaryType)>0):
            gap = re.findall("\w+\.{0,1}\w*", item["salary"])

            unit1 = float(gap[0].split("千")[0]) * 1000 if len(re.findall("千", gap[0])) > 0 else float(
                gap[0].split("万")[0]) * 10000

            unit2 = float(gap[1].split("千")[0]) * 1000 if len(re.findall("千", gap[1])) > 0 else float(
                gap[1].split("万")[0]) * 10000

            item["salary"] = (unit1 + unit2) / 2
        else:
            item["salary"]=0
        print(item)

        sql = "INSERT INTO `crawling` (`job`, `city`,`workage`,`skill`,`education`,`salary`) VALUES (%s, %s,%s, %s,%s, %s)"
        self.cursor.execute(sql, (
        item["job"], item["city"], item["workage"], item["skill"], item["education"], item["salary"]))
        return item

class MycrawlingPipeline2:
    def open_spider(self, spider):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='123456',
                                          database='crawling',
                                          cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):
        # 工作
        item["job"] = re.findall("\w+", item.get("job", ""))[0]
        # 城市
        item["city"] = re.findall("\w+", item.get("city"))[0]
        # 工作经验
        result = re.findall("\d+\.{0,1}\d*", item["workage"])
        item["workage"] = (float(result[0]) + float(result[1])) / 2 if len(result) > 0 else 0
        #  学历
        eduType = {"大专": 1, "本科": 2, "硕士": 3, "博士": 4}
        item["education"] = eduType.get(item["education"]) or "其他"
        # 技术
        item["skill"] = ",".join(item["skill"])
        # 薪资
        salaryType = re.findall("(千|万)", item["salary"])
        if (len(salaryType) > 0):
            gap = re.findall("\w+\.{0,1}\w*", item["salary"])

            unit1 = float(gap[0].split("千")[0]) * 1000 if len(re.findall("千", gap[0])) > 0 else float(
                gap[0].split("万")[0]) * 10000

            unit2 = float(gap[1].split("千")[0]) * 1000 if len(re.findall("千", gap[1])) > 0 else float(
                gap[1].split("万")[0]) * 10000

            item["salary"] = (unit1 + unit2) / 2
        else:
            item["salary"] = 0
        print(item)

        sql = "INSERT INTO `crawling1` (`job`, `city`,`workage`,`skill`,`education`,`salary`) VALUES (%s, %s,%s, %s,%s, %s)"
        self.cursor.execute(sql, (
            item["job"], item["city"], item["workage"], item["skill"], item["education"], item["salary"]))
        return item