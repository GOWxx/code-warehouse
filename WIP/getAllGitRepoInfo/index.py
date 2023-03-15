import os
import git
# 遍历文件夹结构


def traverse_folder(root_path):
    print(root_path, 'test')
    for foldername, subfolders, filenames in os.walk(root_path):
        print("当前文件夹：", foldername, subfolders, filenames)
        for subfolder in subfolders:
            print("子文件夹：", subfolder)
            if subfolder == ".git":
                repo_path = os.path.join(foldername, subfolder, "..")
                # 获取仓库信息
                get_repo_info(repo_path)
        # for filename in filenames:
        #     print("文件名：", filename)
        #     if subfolders == ".git":
        #         repo_path = os.path.join(foldername, filename, "..")
        #         # 获取仓库信息
        #         get_repo_info(repo_path)
        #     # 判断是否为 .git 文件夹
        #     if foldername == ".git":
        #         repo_path = os.path.join(foldername, filename, "..")
        #         # 获取仓库信息
        #         get_repo_info(repo_path)

# 获取仓库信息


def get_repo_info(repo_path):
    try:
        repo = git.Repo(repo_path)
        print(repo)
    #     print("仓库路径：", repo_path)
    #     # 把所有信息写入文件
        f = open("result.txt", "a")
    #     f.write("仓库路径：" + repo_path + "  ")
    #     f.write("当前分支：" + repo.active_branch.name + "  ")
    #     f.write("最新提交：" + repo.head.commit.hexsha + "  ")
    #     f.write("提交信息：" + repo.head.commit.message + "  ")
    #     f.write("作者：" + repo.head.commit.author + "  ")
    #     f.write("提交时间：" + repo.head.commit.committed_datetime + "  ")
    #     f.write("父提交：" + repo.head.commit.parents + "  ")
    #     f.write("远程地址：" + repo.remote().url + "  ")
    except git.InvalidGitRepositoryError:
        f.write("非 Git 仓库：" + repo_path + "  ")
    #     f.close()


if __name__ == "__main__":
    root_path = os.path.join(os.path.expanduser('~'), 'code')
    traverse_folder(root_path)
    # test write file
    # f = open("result.txt", "a")
    # f.write("test write file")
    # f.close()
