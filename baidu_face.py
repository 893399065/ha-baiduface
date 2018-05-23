""" 利用百度人脸识别API进行人脸识别 """
import os
from homeassistant.components.binary_sensor import (
	BinarySensorDevice, PLATFORM_SCHEMA)
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.config import get_default_config_dir
from aip import AipFace
from requests import get
import time
import logging


_LOGGER = logging.getLogger(os.getcwd())

ATTR_SCORES = 'scores'
ATTR_GROUP_ID = 'group_id'
ATTR_UID = 'uid'
ATTR_USER_INFO = 'user_info'
ATTR_FACELIVENESS = "faceliveness"


CONF_APPID = 'app_id'
CONF_APIKEY = 'api_key'
CONF_SECRETKEY = 'secret_key'
CONF_GROUP_ID = 'group_id'
CONF_PORT = 'port'
CONF_HA_PASSWD = 'ha_passwd'
CONF_ENTITY_ID = 'entity_id'
CONF_PASS_SCORE = 'pass_score'


PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_APPID): cv.string,
    vol.Required(CONF_APIKEY): cv.string,
    vol.Required(CONF_SECRETKEY): cv.string,
    vol.Required(CONF_GROUP_ID): cv.string,
    vol.Required(CONF_PORT): cv.string,
    vol.Optional(CONF_HA_PASSWD,default=""): cv.string,
    vol.Required(CONF_ENTITY_ID): cv.string,
    vol.Optional(CONF_PASS_SCORE, default=80): cv.match_all,
})


def setup_platform(hass, config, add_devices,
	               discovery_info=None):
    """ 添加sensor类实例 """
    app_id = config.get(CONF_APPID)
    api_key = config.get(CONF_APIKEY)
    secret_key = config.get(CONF_SECRETKEY)
    group_id = config.get(CONF_GROUP_ID)
    port = config.get(CONF_PORT)
    passwd = config.get(CONF_HA_PASSWD)
    entity_id = config.get(CONF_ENTITY_ID)
    pass_score = config.get(CONF_PASS_SCORE)

    add_devices([FaceSensor(port, passwd, entity_id, app_id, api_key, secret_key, group_id, pass_score)])


class FaceSensor(BinarySensorDevice):
	def __init__(self, port, passwd, entity_id, app_id, api_key, secret_key, group_id, pass_score):
		self._state = None
		self._port = port
		self._passwd = passwd
		self._entity_id = entity_id
		self._app_id = app_id
		self._api_key = api_key
		self._secret_key = secret_key
		self._group_id = group_id
		self._pass_scores = pass_score
		self._path = get_default_config_dir()+".jpg"

	@property
	def name(self):
		return 'Faceidentity'

	@property
	def is_on(self):
		return self._state

	@property
	def icon(self):
		if self._state == True:
			return 'mdi:eye'
		else:
			return 'mdi:eye-off'

	@property
	def device_state_attributes(self):
		if "result" in self._result:
			return {
				ATTR_SCORES:self._result["result"][0]["scores"][0],
				ATTR_UID : self._result["result"][0]["uid"],
				ATTR_GROUP_ID : self._result["result"][0]["group_id"],
				ATTR_USER_INFO : self._result["result"][0]["user_info"],
				ATTR_FACELIVENESS: self._result["ext_info"]["faceliveness"],
			}
		return {}

	def get_file_content(self, filePath):
		with open(filePath, 'rb') as fp:
			return fp.read()

	def update(self):
		scores = self.face_identity()
		""" 活体、人脸阀值 """
		if scores > 0.393241:
			if self._result["result"][0]["scores"][0]>self._pass_scores:
				self._state = True
			else:
				self._state = False
		else:
			self._state = False

	def download_picture(self):
		""" 从ha里下载图片 """
		t = int(round(time.time()))
		url = 'http://127.0.0.1:%s/api/camera_proxy/%s?time=%d -o image.jpg'%(self._port, self._entity_id, t)
		headers = {'x-ha-access': '%s'%(self._passwd),
					'content-type': 'application/json'}
		response = get(url, headers=headers)
		with open(self._path, 'wb') as fp:
		    fp.write(response.content)

	def face_identity(self):
		""" 查找该人脸是否存在识别库里 """
		self.download_picture()
		image = self.get_file_content(filePath=self._path)
		client = AipFace(self._app_id, self._api_key, self._secret_key)
		options = {}
		options["ext_fields"] = "faceliveness"
		self._result = client.identifyUser(self._group_id, image, options)
		if "result" in self._result:
			scores = float(self._result["ext_info"]["faceliveness"])
		else:
			scores = 0
		return scores
