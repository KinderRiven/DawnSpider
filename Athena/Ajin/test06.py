import wx


class MyFrame(wx.Frame):
    pass

class MyApp(wx.App):

    def __init__(self):
        wx.App.__init__(self)
        frame = MyFrame(parent=None, title="Hello World")
        frame.Show(True)


app = MyApp()
app.MainLoop()