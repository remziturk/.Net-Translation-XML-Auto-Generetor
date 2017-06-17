import sublime
import sublime_plugin
import re

class TranslateCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      if not region.empty():
        s = self.view.substr(region)
        key = re.sub('[^a-z0-9]+', '_', re.sub('(^[^a-z]|[^a-z0-9]$)', '', s[:30].lower()))
        self.view.replace(edit, region, "@localization.Get[\"r_{key}\"]".format(**locals()))


        file = open("C:/Users/remzi/Desktop/TFS/AkarcaCiftligi/Akarca/Akarca.Web/Language/tr.xml",'a')

        word = '<word Key="' + key + '" Value="' + s + '"/>'
        
        file.write(word)
        file.close()