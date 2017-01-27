#!/usr/bin/env python
#encoding: UTF-8

import hashlib
from neteaseApi import api

class MyNetease:
    def __init__(self):
        self.netease = api.NetEase()

    def get_music_list(self):
        #netease = api.NetEase()
        username = 'zhouyaphone@163.com'
        password = 'WO19891226'
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        #login_info = netease.login(username, password)
        #print login_info
        #print str(login_info.get('message')) + " " + login_info.get('captchaId')
        #userId = login_info.get('profile').get('userId') #用户歌单
        userId = 57542828
        playlist = self.netease.user_playlist(userId) #用户歌单
        #print playlist
        if playlist == -1:
            return
        datatype = 'top_playlists'
        datalist = self.netease.dig_info(playlist, datatype)
        #print datalist
        title =  username + ' 的歌单'
        #print title
        #for data in datalist:
        #    print str(data.get('playlist_id')) + " " + data.get('creator_name') + " " + data.get('playlists_name')
        songs = self.netease.playlist_detail(57542828)  # 歌单详情
        datalist = self.netease.dig_info(songs, 'songs')
        music_list = []
        for data in datalist:
            music_info = {}
            music_info.setdefault("song_name", data.get("song_name"))
            music_info.setdefault("artist", data.get("artist"))
            music_info.setdefault("album_name", data.get("album_name"))
            music_info.setdefault("mp3_url", data.get("mp3_url"))
            music_info.setdefault("playTime", data.get("playTime"))  #音乐时长
            music_info.setdefault("quality", data.get("quality"))
            music_list.append(music_info)
        return music_list

    def login(self, username, password):
        #netease = api.NetEase()
        password = hashlib.md5(password.encode('utf-8')).hexdigest()
        #login_info = self.netease.login(username, password)
        login_info = {u'profile': {u'followed': False, u'remarkName': None, u'expertTags': None, u'userId': 57542828, u'authority': 0, u'userType': 0, u'backgroundImgId': 2002210674180199, u'city': 500105, u'mutual': False, u'avatarUrl': u'http://p4.music.126.net/VnZiScyynLG7atLIZ2YPkw==/18686200114669622.jpg', u'avatarImgIdStr': u'18686200114669622', u'detailDescription': u'', u'province': 500000, u'description': u'', u'avatarImgId_str': u'18686200114669622', u'signature': u'', u'birthday': -2209017600000, u'nickname': u'\u8309\u82b7\u6c34', u'vipType': 0, u'avatarImgId': 18686200114669622, u'gender': 0, u'djStatus': 0, u'accountStatus': 0, u'backgroundImgIdStr': u'2002210674180199', u'backgroundUrl': u'http://p1.music.126.net/VTW4vsN08vwL3uSQqPyHqg==/2002210674180199.jpg', u'defaultAvatar': True, u'authStatus': 0}, u'account': {u'userName': u'0_zhouyaphone@163.com', u'status': 0, u'anonimousUser': False, u'whitelistAuthority': 0, u'baoyueVersion': 0, u'salt': u'', u'createTime': 0, u'tokenVersion': 0, u'vipType': 0, u'ban': 0, u'type': 0, u'id': 57542828, u'donateVersion': 0}, u'code': 200, u'effectTime': 2147483647, u'clientId': u'9505bf08c1e71d06255c860eb9b7dc399042ae3a54428d81b05af2aad65f9b9a2128fa7de6b09db4b64bf3324e151b2186a1ad5be63cc816', u'loginType': 0, u'bindings': [{u'expiresIn': 2147483647, u'tokenJsonStr': u'{"email":"zhouyaphone@163.com"}', u'url': u'', u'type': 0, u'userId': 57542828, u'refreshTime': 0, u'expired': False, u'id': 27817958}]}
        if login_info['code'] == 200:
            res = u"登陆成功"
            #登陆成功保存userId，作为获取用户歌单的依据，userId是唯一的，只要登陆成功，就会保存在userInfo文件中，所以不必每次都登陆
            userId = login_info.get('profile').get('userId')
            file = open("./userInfo", 'w')
            file.write(str(userId))
            file.close()
        else:
            res = u"登陆失败"
        return res

    def get_user_playlist(self, userId):  #获取用户歌单
        #netease = api.NetEase()
        playlist = self.netease.user_playlist(userId)  # 用户歌单
        if playlist == -1:
            datalist = -1
        else:
            datatype = 'top_playlists'
            datalist = self.netease.dig_info(playlist, datatype)
        return playlist


if __name__ == '__main__':
    myNetease = MyNetease()
    myNetease.get_music_list()