# Baidu Face for [Home Assistant](https://home-assistant.io)
TODO: add face binary sensor 



该插件使用简单方便，无需多余安装应用，支持在线活体检测。由于大家不清楚活体检测阀值，所以我替大家写死了就使用了官方推荐值，如果有其他需要可以自己去代码改。
该 baidu_face 二进制传感器插件是利用百度人脸识别api进行人脸识别。插件会一直获取homeassistant中摄像头图片，然后进行识别。识别成功或者失败，传感器会做出相应的图标改变和状态的改变。
    
## 安装
1) 如果你是树莓派用户，那么需要先进入虚拟环境， 然后输入```pip3 install baidu-aip ```来安装百度AI库(如果你是其他用户，那么请在homeassistant的安装环境里执行相应的命令来安装库。)
2) 请在configuration.yaml的同一目录下新建文件夹 custom_components/binary_sensor                              
3) 下载插件, 并将 baidu_face.py 放置于 binary_sensor 文件夹下

## 配置示例 :
```bash
binary_sensor:
    - platform : baidu_face
      #从百度ai开放平台人脸识别应用中获取
      app_id : xxxxxxxxxx
      api_key : xxxxxxxxxxxxxxxxxxx
      secret_key: xxxxxxxxxxxxxxxx
      group_id: xxxxxx
      #homeassistant端口
      port: 8123
      #ha密码
      ha_passwd: xxxxxxxxxxx
      #摄像头entity_id
      entity_id: camera.mjpeg_camera
      #刷新间隔(1~30s)
      scan_interval: 2
      #人脸识别阀值(推荐80以上,分数越高误拒率越高. 默认80该项可以不填)
      pass_score: 80
```

![识别成功](https://github.com/893399065/ha-baiduface/blob/master/QQ%E6%88%AA%E5%9B%BE20180304105608.jpg)
![识别失败](https://github.com/893399065/ha-baiduface/blob/master/QQ%E6%88%AA%E5%9B%BE20180304105547.jpg)
![其他信息](https://github.com/893399065/ha-baiduface/blob/master/QQ%E6%88%AA%E5%9B%BE20180304144107.jpg)
