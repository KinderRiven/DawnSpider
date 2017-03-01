import wx


class App(wx.App):

    def __init__(self):
        wx.App.__init__(self)
        print "This is a new Frame!"


    def OnInit(self):
        print "This is a new frame."
        frame = wx.Frame(parent=None, title='Bare')
        frame.Show()
        return True


app = App()
app.MainLoop()