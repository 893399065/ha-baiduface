        /**************************************************************************************
        *           写在前面：                                                                 *
        *                  寒假回去学习了python，这是我的第一个插件。由于个人基础有限该插          *
        *           件借鉴了 @L大 从利用request在ha保存图片到本地 以及L大的scan_interval          *
        *           提示的前提下才完善此插件的。                                                 *
        *                 若果还想增添其他功能，请留言。我尽可能完善                              *
        *                                                                                     *
        **************************************************************************************/

    该插件使用简单方便,无需多余安装应用。
    该 baidu_face 二进制传感器插件是利用百度人脸识别api进行人脸识别。插件会一直获取homeassistant中摄像头图片，然后进行识别。若果识别成功或者失败，传感器会做出相应的图标改变和状态的改变。
    
    安装步骤：
          1. 如果你是树莓派用户，那么需要先进入虚拟环境， 然后输入 pip3 install baidu-aip(如果你是其他用户，那么请在homeassistant的安装环境里执行相应的命令来安装模块。)
          2. 请在configuration.yaml的同一目录下新建文件夹 custom_components/binary_sensor                              
          3. 在下该插件, 并将该插件放置于binary_sensor文件夹下

    配置示例 :
    binary_sensor:
      - platform : baidu_face
        # 从百度ai人脸识别平台的应用管理里获取
        app_id : xxxxxxxxxx
        api_key : xxxxxxxxxxxxxxxxxxx
        secret_key: xxxxxxxxxxxxxxxxxxxxxxxxxx
        group_id: xxxxxx
        # homeassistant 端口
        port: 8123
        # homeassistant 密码(可以为空)
        ha_passwd: xxxxxxxxxxx
        # 摄像头entity_id
        entity_id: camera.mjpeg_camera
        # 刷新频率(1~30s)
        scan_interval: 2
