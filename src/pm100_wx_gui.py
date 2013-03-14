from pm100 import PM100D, find_instruments
import wx




class PM100D_Panel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, -1, size=(800,-1))
        self.inst_list = find_instruments()
        self.pm = PM100D(self.inst_list[0])
        
        text = wx.StaticText(self, -1, "      ---      ")
        font = wx.Font(36, wx.SWISS, wx.NORMAL, wx.NORMAL)
        text.SetFont(font)
        self.display = text
        
        self.timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self.on_meas, self.timer)
        self.timer.Start(300)
        
        self.ranges = [self.pm.range*1000]
        self.current_range = str(self.ranges[0])
        
        self.AutoRangeBtn = wx.ToggleButton(self, -1, "Auto")
        self.gauge = wx.Gauge(self, -1, 100, size=(-1, 21), style=wx.GA_HORIZONTAL|wx.GA_SMOOTH)
        self.range_val = wx.ComboBox(self, -1, str(self.ranges[0]),
                                     size=(100,-1),
                                     choices=[str(self.ranges[0]),],
                                     style=wx.CB_DROPDOWN|wx.TE_PROCESS_ENTER)
        self.range_val.Bind(wx.EVT_COMBOBOX, self.on_set_range)
        self.range_val.Bind(wx.EVT_TEXT_ENTER, self.on_set_range)
        
        self.AutoRangeBtn.SetValue(self.pm.autorange)
        self.AutoRangeBtn.Bind(wx.EVT_TOGGLEBUTTON, self.on_autorange)
        
        self.WLLabel = wx.StaticText(self, -1, "Wavelength (nm):")
        self.wavelengths = wavelengths = [780, 800]
        self.WLChoice = wx.ComboBox(self, -1, str(self.pm.wavelength),
                                    size = (100,-1), 
                                    choices=[str(v) for v in wavelengths],
                                    style=wx.CB_DROPDOWN|wx.TE_PROCESS_ENTER)
        self.WLChoice.Bind(wx.EVT_COMBOBOX, self.on_wavelength)
        self.WLChoice.Bind(wx.EVT_TEXT_ENTER, self.on_wavelength)
        
        top_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_sizer.Add(self.WLLabel,0,wx.ALL|wx.ALIGN_CENTER_VERTICAL,2)
        top_sizer.Add(self.WLChoice,0,wx.ALL,2)
        
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(self.AutoRangeBtn,0,wx.ALL,1)
        hsizer.Add(self.gauge, 1,wx.ALIGN_CENTER_VERTICAL|wx.ALL,1)
        hsizer.Add(self.range_val, 0,wx.ALIGN_CENTER_VERTICAL)
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(top_sizer,0,wx.EXPAND,0)
        sizer.Add(text, 1, wx.ALL, 5)
        sizer.Add(hsizer, 0, wx.EXPAND,0)
        self.SetSizer(sizer)
        self.Fit()
        
    def on_set_range(self, evt):
        val = float(self.range_val.GetValue()) *0.99/ 1000
        self.pm.range = val
        val = self.pm.range * 1000
        pmax_str = str(val)
        self.current_range = pmax_str
        self.range_val.SetLabel(pmax_str)
        if val not in self.ranges:
            self.ranges.append(val)
            self.range_val.Append(pmax_str)
        print "Setting range to", val
            
        
    def on_wavelength(self, evt):
        wl = int(self.WLChoice.GetValue())
        if wl not in self.wavelengths:
            self.wavelengths.append(wl)
            self.WLChoice.Append(str(wl))
        self.pm.wavelength = wl
        print "Wavelength set to", self.pm.wavelength
        
    def on_autorange(self, evt):
        val = bool(evt.IsChecked())
        self.pm.autorange = val
        
    def on_meas(self, evt):
        pmax = self.pm.range * 1000
        pmax_str = str(pmax)
        if pmax not in self.ranges:
            self.ranges.append(pmax)
            self.range_val.Append(pmax_str)
        pwr = self.pm.power * 1000
        self.display.SetLabel(str(pwr))
        if self.current_range != pmax_str:
            self.range_val.SetLabel(pmax_str)
            self.current_range = pmax_str
        self.gauge.SetValue(int(100*pwr/pmax))
        #self.Fit()
        #tl = wx.GetTopLevelParent(self)
        #tl.Fit()
        
        
if __name__=="__main__":
    app = wx.App(0)
    frame = wx.Frame(None,-1,"PM100 Power Meter")
    panel = PM100D_Panel(frame)
    frame.Fit()
    frame.SetSize((400,-1))
    frame.Show()
    app.MainLoop()