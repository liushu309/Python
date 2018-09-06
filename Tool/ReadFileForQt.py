import os

class ListQtFiles:
    def __init__(self, file_dir = "./"):
        self.file_dir_ = file_dir
    def getFileList(self, file_sub_fix_list):
        """
            根据要查找的文件目录，返回一个已经分了类的列表
            file_sub_fix_list： 要分类的文件后缀名
        """
        all_file = os.listdir(self.file_dir_)
        # 构建输入列表 /home/liushu/Documents/Project/Qt/WeldTracking/WeldTracking
        out_put_list = []
        for sub_fix in file_sub_fix_list:
            out_put_list.append([sub_fix])
        for file in all_file:
            for i, sub_fix in enumerate(file_sub_fix_list):
                if file.endswith(sub_fix):
                    out_put_list[i].append(file)

        return out_put_list

    def printListInTxt(self, file_dir, input_lists):
        """
            将分类列表打印出来，方便复制粘贴
            file_dir： 打印文件目录
            input_lists: 输入分类列表
        """
        file = open(file_dir, "w")
        for sub_list in input_lists:
            if len(sub_list) > 0:
                file.write(sub_list[0] + ":\n")

                for i, file_name in enumerate(sub_list):
                    if i > 0:
                        file.write(file_name + " \\")
                        file.write("\n")
                file.write("\n\n")

        file.close()


if __name__ == "__main__":
    list_qt_files = ListQtFiles("/home/liushu/Documents/Project/Qt/WeldTracking/WeldTracking")
    out_put_list = list_qt_files.getFileList([ ".h", ".cpp", ".ui"])
    list_qt_files.printListInTxt("./example_file.txt", out_put_list)



 