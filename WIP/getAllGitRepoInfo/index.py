# 本程序基本由 ChatGPT GPT-4 model 生成。

import os
import git
import json
import subprocess


def get_git_config_value(repo, key, is_local=True):
    try:
        if is_local:
            return repo.config_reader().get_value("user", key)
        else:
            return subprocess.check_output(["git", "config", "--global", f"user.{key}"]).decode("utf-8").strip()
    except (git.exc.GitCommandError, KeyError, subprocess.CalledProcessError):
        return None


def get_repo_info(repo_path):
    repo_info = {
        "repo_path": repo_path,
    }

    try:
        repo = git.Repo(repo_path)
        print(repo)
        can_get_info = True
        active_branch = repo.active_branch.name
        latest_commit = repo.head.commit
        remote_url = repo.remotes.origin.url
    except git.InvalidGitRepositoryError:
        print(f"{repo_path} 不是一个有效的 Git 仓库")
        return None
    except (git.exc.BadName, git.exc.BadObject, ValueError, TypeError):
        can_get_info = False

    local_user_name = get_git_config_value(repo, "name", is_local=True)
    local_user_email = get_git_config_value(repo, "email", is_local=True)

    global_user_name = get_git_config_value(repo, "name", is_local=False)
    global_user_email = get_git_config_value(repo, "email", is_local=False)

    repo_info.update({
        "local_user_name": local_user_name,
        "local_user_email": local_user_email,
        "global_user_name": global_user_name,
        "global_user_email": global_user_email,
    })

    if not can_get_info:
        repo_info["error"] = "无法获取部分信息。"
    else:
        try:
            commit = repo.head.commit
            if repo.head.is_detached:
                active_branch = "Detached HEAD"
            else:
                active_branch = repo.active_branch.name

            repo_info.update({
                "current_branch": active_branch,
                "latest_commit": commit.hexsha,
                "commit_message": commit.message.strip(),
                "author": str(commit.author),
                "commit_time": str(commit.committed_datetime),
                "parent_commits": [str(parent) for parent in commit.parents],
                "remote_url": repo.remote().url,
            })
        except (git.exc.BadName, git.exc.BadObject, ValueError):
            repo_info["error"] = "无法获取部分信息。"

    return repo_info


def traverse_folder(root_path):
    all_repos_info = []

    for foldername, subfolders, filenames in os.walk(root_path):
        print("当前文件夹：", foldername, subfolders, filenames)
        for subfolder in subfolders:
            print("子文件夹：", subfolder)
            if subfolder == ".git":
                repo_path = os.path.join(foldername, subfolder)
                repo_info = get_repo_info(repo_path)
                if repo_info is not None:
                    all_repos_info.append(repo_info)

    return all_repos_info


if __name__ == "__main__":
    # example path: ~/code
    root_path = os.path.join(os.path.expanduser('~'), 'code')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    result_file_path = os.path.join(current_dir, "result.json")
    all_repos_info = traverse_folder(root_path)

    with open(result_file_path, "w", encoding='utf-8') as f:
        json.dump(all_repos_info, f, ensure_ascii=False, indent=2)
