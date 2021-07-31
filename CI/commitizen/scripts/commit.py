#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import gitlab
import os
import sys
import getopt

get_first_commit = False
get_mr_title = False
get_target_branch = False

try:
   opts, args = getopt.getopt(sys.argv[1:],"hic:t:ti:p:b:o",["commit","token=", "title", "project=", "branch=", "target-branch"])

except getopt.GetoptError:
   print('test.py [-c | --commit] [-t | --token {token}]')
   sys.exit(2)
   
for opt, arg in opts:
    if opt == '-h':
        print('[commit.py] -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-c", "--commit"):
        get_first_commit = True
    elif opt in ("-t", "--token"):
       ci_job_token = arg
    elif opt in ("-ti", "--title"):
       get_mr_title = True
    elif opt in ("-p", "--project"):
       project_id = arg
    elif opt in ("-b", "--branch"):
       git_branch = arg
    elif opt in ("-o", "--target-branch"):
       get_target_branch = True

# private token or personal token authentication
gl = gitlab.Gitlab('https://gitlab.com', private_token=ci_job_token)

#project = gl.projects.get('28204898', lazy=True)
project = gl.projects.get(project_id, lazy=True)

project_mrs = project.mergerequests.list()
#mrs = gl.mergerequests.list()

for mr in project_mrs:
    if mr.source_branch == git_branch and str(mr.source_project_id) == str(project_id) and str(mr.state) == 'opened':
        mr_title = mr.title
        mr_first_commit = mr.sha
        target_branch = mr.target_branch

        #print('\n\nMR=[-{0}-]'.format(mr))


if get_target_branch:
    print('{0}'.format(target_branch))


if get_first_commit:

    print('{0}'.format(mr_first_commit))


if get_mr_title:

    print('{0}'.format(mr_title))
