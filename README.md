Lenovo@LAPTOP-ITG6URDD MINGW64 / (master)
$ git init
Reinitialized existing Git repository in D:/Git/.git/

Lenovo@LAPTOP-ITG6URDD MINGW64 / (master)
$ git add README.md
warning: in the working copy of 'README.md', LF will be replace
d by CRLF the next time Git touches it

Lenovo@LAPTOP-ITG6URDD MINGW64 / (master)
$ git commit -m "first commit"
[master 0943856] first commit
 1 file changed, 1 insertion(+)
 create mode 100644 README.md

Lenovo@LAPTOP-ITG6URDD MINGW64 / (master)
$ git branch -M main

Lenovo@LAPTOP-ITG6URDD MINGW64 / (main)
$ git remote add origin git@github.com:HcmStduy/hcmapi.git
error: remote origin already exists.

Lenovo@LAPTOP-ITG6URDD MINGW64 / (main)
$ git push -u origin main
Enumerating objects: 6, done.
Counting objects: 100% (6/6), done.
Delta compression using up to 16 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (6/6), 462 bytes | 462.00 KiB/s, done.
Total 6 (delta 0), reused 0 (delta 0), pack-reused 0
To github.com:HcmStduy/hcmapi.git
 * [new branch]      main -> main
  branch 'main' set up to track 'origin/main'.

Lenovo@LAPTOP-ITG6URDD MINGW64 / (main)
$