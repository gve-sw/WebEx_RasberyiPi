#!/usr/bin/python
import unirest
import json

#TBD change to dynamically detected bot key
hard_key = 'Bearer MGVjZGIxYTItZmU2OS00OTcwLWE1NjItMjVmZjM0YmZmMTlmN2VmMTQ4OTctYTY4'

class sparkapi:

  def __init( self, x=0):
      self.key = hard_key

  def get_msg(self,id):
    response = unirest.get("https://api.ciscospark.com/v1/messages/"+id,
      headers={
        "Authorization": hard_key
      }
    )
    cmnd_text = response.body['text'].split(' ',1)
    print cmnd_text
    #cmnd_list = cmnd_text[1].split('|')
    #print string
    return cmnd_text

  def post_msg(self,grp,msg):
    response = unirest.post("https://api.ciscospark.com/v1/messages/",
      headers={
        "Authorization": hard_key,
        "Content-Type": "application/json"
      },
      params=json.dumps({"roomId":grp,"text":msg})
    )
    print response.body

  def post_file(self,grp,file_o):
    response = unirest.post("https://api.ciscospark.com/v1/messages/", 
      headers={
        "Authorization": hard_key,
        "Content-Type": "application/json"},
      params=json.dumps({"roomId":grp,"files":["https://secret-brushlands-95547.herokuapp.com/imgs/"+file_o]})
    )    

  def post_txt_file(self,grp,file_o):
    response = unirest.post("https://api.ciscospark.com/v1/messages/", 
      headers={
        "Authorization": hard_key,
        "Content-Type": "application/json"},
      params=json.dumps({"roomId":grp,"files":["https://secret-brushlands-95547.herokuapp.com/txt/"+file_o]})
    )  