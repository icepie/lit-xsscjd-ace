import requests
import json
from litxsscjd import endpoints
from litxsscjd import util
from urllib.parse import quote


class litUesr:
    """lit uesr object"""
    def __init__(self, username: str, password: str):
        self.session=requests.Session()
        self.username = username
        self.password = util.get_sha256(password)

        self.__headers = {
            'Proxy-Connection': 'keep-alive',
            'Accept': 'application/json, text/plain, */*',
            'DNT': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            'request-ajax': 'true',
            'Content-Type': 'application/json',
            'Origin': 'http://xsscjd.sec.lit.edu.cn',
            'Referer': 'http://xsscjd.sec.lit.edu.cn/student/index.html',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        }

        # login the acconut
        try:
            self.login = self.__login()
        except:
            self.info = None

        # get the user info
        try:
            if self.login["code"] == 1:
                self.info = self.login["response"]
                self.is_logged=True
            else:
                self.info = None
                self.is_logged=False
        except:
            self.info = None
            self.is_logged=False


    def __login(self):
        data = {"userName": self.username, "password": self.password,"remember":False,"clientId":0}
        # login func
        try:
            response = self.session.post(
                url=endpoints["login"], data=json.dumps(data), headers=self.__headers, verify=False
            )
        except:
            return None

        res = response.json()

        #self.__cookies['SESSION'] = self.session.cookies.get("SESSION")

        self.session.cookies.set("studentUserName", quote(res['response']['userName'], 'utf-8'))

        return res

    def get_record(self):

        try:
            response = self.session.post(
                url=endpoints["record"], headers=self.__headers, verify=False
            )
        except:
            return None

        res = response.json()

        return res

    def get_exam_paper(self):

        try:
            response = self.session.post(
                url=endpoints["paper"], headers=self.__headers, verify=False
            )
        except:
            return None

        res = response.json()

        return res
    
    def submit_exam_answer(self,data: dict):

        try:
            response = self.session.post(
                url=endpoints["submit"],data=json.dumps(data) ,headers=self.__headers, verify=False
            )
        except:
            return None

        res = response.json()

        return res
