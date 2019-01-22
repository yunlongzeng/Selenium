import subprocess

#启动时间
class Open_Time():

    #命令初始化
    def __init__(self,device_name):
        self.check_device_command = "adb devices"  #check device 命令
        self.start_command = "adb shell am start -W -n {}/.ui.activity.LaunchActivity".format(device_name)
        self.stop_command = "adb shell am force-stop {}".format(device_name)
        self.home_command = "adb shell input keyevent 3"
        self.start_time_leng = 0
        self.start_time_re = 0

    #check设备是否处于连接状态
    def check_device(self):
        cmd = self.check_device_command.split()
        device = subprocess.run(cmd,stdout = subprocess.PIPE)
        device_info = device.stdout.decode(encoding = 'utf-8')
        device_info = device_info.split("attached")
        if device_info[1].strip() == "":
            # print("1")
            return False
        else:
            # print("2")
            return True

    #启动
    def start_program(self):
        cmd = self.start_command.split()
        start_command = subprocess.run(cmd,stdout = subprocess.PIPE)
        total_time = start_command.stdout.decode(encoding = 'utf-8')
        total_time = total_time.split("TotalTime:")
        total_time = total_time[1].split("WaitTime")
        return total_time[0].strip()

    #冷启动关闭
    def stop_program(self):
        cmd = self.stop_command.split()
        subprocess.run(cmd)

    #热启动关闭，home键返回
    def back_home(self):
        cmd = self.home_command.split()
        subprocess.run(cmd)

        
    #冷启动程序执行逻辑
    def run_leng(self,n):
        
        self.stop_program()
        for i in range(n):
            bool_check_device = self.check_device()
            if bool_check_device == True:
                time = int(self.start_program())
                print("第%s次冷启动的时间为：%s"%(i+1,time))
                self.start_time_leng += time
                self.stop_program()
            else:
                print("第%s次断开连接"%(i+1))
                av_time = self.start_time_leng/(i+1)
                print("%s次冷启动的平均时间为:%s"%(i+1,av_time))
                n = i+1
                break
        av_time = self.start_time_leng/10
        print("%s次冷启动的平均时间为:%s"%(n,av_time))

#热启动程序执行逻辑
    def run_re(self,n):
        bool_check_device = self.check_device()
        if bool_check_device == True:
            self.start_program()
            self.back_home()
        else:
            print("测试热启动前连接断开。")
        for i in range(n):
            bool_check_device = self.check_device()
            if bool_check_device == True:
                time = int(self.start_program())
                print("第%s次冷启动的时间为：%s"%(i+1,time))
                self.start_time_re += time
                self.back_home()
            else:
                print("第%s次断开连接"%(i+1))
                av_time = self.start_time_re/(i+1)
                print("%s次冷启动的平均时间为:%s"%(i+1,av_time))
                n = i+1
                break
        av_time = self.start_time_re/10
        print("%s次热启动的平均时间为:%s"%(n,av_time))

if __name__ == "__main__":
    open_time = Open_Time("org.cnodejs.android.md")
    open_time.run_leng(10)
    open_time.run_re(10)