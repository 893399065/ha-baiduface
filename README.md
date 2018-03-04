# Baidu Face for [Home Assistant](https://home-assistant.io)
TODO: add face binary sensor 



该插件使用简单方便,无需多余安装应用。
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
      secret_key: xxxxxxxxxxxxxxxxxxxxxxxxxx
      group_id: xxxxxx
      #homeassistant端口
      port: 8123
      #ha密码
      ha_passwd: xxxxxxxxxxx
      #摄像头entity_id
      entity_id: camera.mjpeg_camera
      #刷新频率(1~30s)
      scan_interval: 2
```
.. |Coverage Status| image:: https://img.shields.io/coveralls/home-assistant/home-assistant.svg
   :target: https://coveralls.io/r/home-assistant/home-assistant?branch=master
