# the platform url
hostname = "http://xsscjd.sec.lit.edu.cn"

# the main api
endpoints = {
    "login": hostname + "/api/user/login",
    "current": hostname + "/api/student/user/current",
    "record": hostname + "/api/student/exampaper/answer/record",
    "paper": hostname + "/api/student/exam/paper/random/1",
    "submit": hostname + "/api/student/exampaper/answer/answerSubmit"
}