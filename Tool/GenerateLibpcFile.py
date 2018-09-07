import os

class FindPcOsNames:
    def __init__(self, os_dir):
        self.os_dir_ = os_dir

    def getOsList(self):
        self.out_os_list = []
        os_list = os.listdir(self.os_dir_)
        for os_name in os_list:
            if os_name.endswith(".so"):
                self.out_os_list.append(os_name)
                # print(os_name)


        return self.out_os_list

    def printListsInFile(self, file_name):
        # 打开文件
        file = open(file_name, "w")

        for os_name in self.out_os_list:
            # 获取os中需要的字符
            need_os_name = os_name[3:-3]
            need_os_name = "-l" + need_os_name

            file.write(" " + need_os_name)
        # print(file_name)
        file.close()

if __name__ == "__main__":
    find_os_name = FindPcOsNames("/usr/local/Opencv-3.3.0/Release/lib")
    out_put_list = find_os_name.getOsList()
    find_os_name.printListsInFile("./VTK.pc")