# Git Cheat Sheet
## SETUP & INIT
| Command                                     | Description                                                                           |
|---------------------------------------------|---------------------------------------------------------------------------------------|
| `git config --global user.name "[firstname lastname]"` | Set a name that is identifiable for credit when reviewing version history.           |
| `git config --global user.email "[valid-email]"`       | Set an email address that will be associated with each history marker.               |
| `git init`                                  | Initialize an existing directory as a Git repository.                                |
| `git clone [url]`                           | Retrieve an entire repository from a hosted location via URL.                        |

---

## STAGE & SNAPSHOT
| Command                      | Description                                                                         |
|------------------------------|-------------------------------------------------------------------------------------|
| `git status`                 | Show modified files in the working directory, staged for your next commit.          |
| `git add [file]` / `git add .` | Add a file/all files as it looks now to your next commit (stage).                   |
| `git reset [file]` / `git reset .` | Unstage a file/all files while retaining the changes in the working directory.     |
| `git diff`                   | Show the diff of what has changed but not staged.                                   |
| `git diff --staged`          | Show the diff of what is staged but not yet committed.                              |
| `git commit -m "[descriptive message]"` | Commit your staged content as a new commit snapshot.                           |

---

## SHARE & UPDATE
| Command                                      | Description                                                                         |
|----------------------------------------------|-------------------------------------------------------------------------------------|
| `git remote add [alias] [url]`               | Add a Git URL as an alias.                                                         |
| `git fetch [alias]`                          | Fetch all the branches from that Git remote.                                       |
| `git merge [alias]/[branch]`                 | Merge a remote branch into your current branch to bring it up to date.             |
| `git push [alias] [branch]`                  | Transmit local branch commits to the remote repository branch.                     |
| `git pull`                                   | Fetch and merge any commits from the tracking remote branch.                       |

---

## BRANCH & MERGE
| Command                      | Description                                                                         |
|------------------------------|-------------------------------------------------------------------------------------|
| `git branch`                 | List your branches. A `*` appears next to the currently active branch.             |
| `git branch [branch-name]`   | Create a new branch at the current commit.                                          |
| `git checkout [branch-name]` | Switch to another branch and check it out into your working directory.              |
| `git merge [branch]`         | Merge the specified branch’s history into the current one.                         |

---

## INSPECT & COMPARE
| Command                                      | Description                                                                         |
|----------------------------------------------|-------------------------------------------------------------------------------------|
| `git log`                                    | Show the commit history for the currently active branch.                           |
| `git log branchB..branchA`                   | Show the commits on branchA that are not on branchB.                               |
| `git log --follow [file]`                    | Show the commits that changed the file, even across renames.                       |
| `git diff branchB...branchA`                 | Show the diff of what is in branchA that is not in branchB.                        |

---

## UNDO & FIX
| Command                      | Description                                                                         |
|------------------------------|-------------------------------------------------------------------------------------|
| `git restore [file]`         | Discard changes in the working directory.                                           |
| `git restore --staged [file]`| Unstage a file without discarding changes.                                          |
| `git reset --hard [commit]`  | Reset HEAD to a previous commit, discarding all changes in working directory.       |
| `git revert [commit]`        | Create a new commit that undoes the changes made in the specified commit.           |
