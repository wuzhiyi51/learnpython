from app import App
import  time
import  csv
class Manager():

    def __init__(self,count,App):
        self.count= count
        self.app =App
        self.file = open("starttime.txt","w")

    def run(self):
        while self.count>0:
            self.app.startApp()
            time.sleep(2)
            #获取时间
            self.file.write(self.app.getStartTime())
            self.app.stopApp()
            time.sleep(2)
            self.count=self.count-1

        #关闭资源
        self.file.close()

app= App("com.android.browser","/com.android.browser.BrowserActivity")
m = Manager(6,app)
m.run()