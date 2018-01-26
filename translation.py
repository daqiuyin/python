#coding=utf-8
import wx
from aip import AipOcr

APP_ID = '10737306'
API_KEY = 'ycuTokmW4GepFOL6GYHDD14K'
SECRET_KEY = 'XHewKh1mRktOG3BGXEYGYKMTG5DbDylA'

client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

app = wx.App()
win = wx.Frame(None,title = '专属翻译软件（给你一个坚定的眼神）',size = (410,335))
bkg = wx.Panel(win)

def get_file_content(filePath):
    with open (filePath,'rb') as fp:
        result = client.general(fp.read())
        return result

def press_butt(event):
    result = get_file_content(filename.GetValue())

    output = []
    for i in result['words_result']:
        output.append(i['words']+'\n')
    soutput=''.join(output)
    contents.SetValue(soutput)

loadButton = wx.Button(bkg,label = 'TRANSLATE')
loadButton.Bind(wx.EVT_BUTTON,press_butt)

filename= wx.TextCtrl(bkg)
contents = wx.TextCtrl(bkg,style = wx.TE_MULTILINE|wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(filename,proportion=3,flag = wx.EXPAND)
hbox.Add(loadButton,proportion=1,flag=wx.LEFT,border=5)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()
