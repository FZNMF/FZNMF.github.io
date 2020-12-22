import requests
import datetime
import re
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def mailsend(result):
    smtpserver = 'smtp.qq.com'
    username = '1797901195@qq.com'
    password = 'frkgnvgztgiadjai'
    sendername = username
    receiver = 'lymsfk@qq.com'
    subject = '打卡通知'
    msg = MIMEText("<html><h1>{}</h1></html>".format(result), 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sendername, receiver, msg.as_string())
    smtp.quit()
    return result


def postform(posturl, headers, data):
    print('开始发送'.encode("utf8").decode("utf8"))
    res = requests.post(posturl, headers=headers, data=data)
    return res


if __name__ == '__main__':
    posturl = 'http://form.hhu.edu.cn/pdc/formDesignApi/dataFormSave?wid=A335B048C8456F75E0538101600A6A04&userId=1908080125'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '804',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':
        'JSESSIONID=7D692BB32FA558B270554482239C1000; amlbcookie=02; iPlanetDirectoryPro=AQIC5wM2LY4SfczxVkjdqp64reWS1R9nGTBpWSQjAVnF%2FOg%3D%40AAJTSQACMDI%3D%23',
        'Host': 'form.hhu.edu.cn',
        'Origin': 'http://form.hhu.edu.cn',
        'Pragma': 'no-cache',
        'Referer': 'http://form.hhu.edu.cn/pdc/formDesignApi/S/gUTwwojq',
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    # print(headers)
    data = {
        'DATETIME_CYCLE':
        '{}'.format(
            re.sub(r'-', '/',
                   datetime.datetime.now().strftime('%Y-%m-%d'))),
        'XGH_336526':
        '1908080125',
        'XM_1474':
        '林叶',
        'SFZJH_859173':
        '450923200102054311',
        'SELECT_941320':
        '商学院',
        'SELECT_459666':
        '2019级',
        'SELECT_814855':
        '信息',
        'SELECT_525884':
        '信息19_1',
        'SELECT_125597':
        '江宁校区教学区25舍',
        'TEXT_950231':
        '935',
        'TEXT_937296':
        '18378830278',
        'RADIO_853789':
        '否',
        'RADIO_43840':
        '否',
        'RADIO_579935':
        '健康',
        'RADIO_138407':
        '否',
        'RADIO_546905':
        '否',
        'RADIO_314799':
        '否',
        'RADIO_209256':
        '否',
        'RADIO_836972':
        '否',
        'RADIO_302717':
        '否',
        'RADIO_701131':
        '否',
        'RADIO_438985':
        '否',
        'RADIO_467360':
        '是',
        'PICKER_956186':
        '江苏省,南京市,江宁区',
        'TEXT_434598':
        '',
        'TEXT_515297':
        '',
        'TEXT_752063':
        '',
    }
    res = postform(posturl, headers, data)
    if res.status_code == 200:
        print(mailsend('表单发送成功').encode("utf8").decode("utf8"))
    else:
        print(
            mailsend('请求无法正常响应{}'.format(
                res.status_code)).encode("utf8").decode("utf8"))
