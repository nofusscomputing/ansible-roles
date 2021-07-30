#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import gitlab
import os
import sys
import getopt
#import gitlab.v4.objects

#from commitizen import Check
#from commitizen import commands, config


get_first_commit = False
get_mr_title = False

try:
   opts, args = getopt.getopt(sys.argv[1:],"hic:t:ti:p",["commit","token=", "title", "project="])

except getopt.GetoptError:
   print('test.py [-c | --commit] [-t | --token {token}]')
   sys.exit(2)
   
for opt, arg in opts:
    if opt == '-h':
        print('[commit.py] -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-c", "--commit"):
       #inputfile = arg
        get_first_commit = True
    elif opt in ("-t", "--token"):
       ci_job_token = arg
    elif opt in ("-ti", "--title"):
       get_mr_title = True
    elif opt in ("-p", "--project"):
       project_id = arg



#try:
#    if os.environ['CI_JOB_TOKEN']:
#        ci_job_token = os.environ['CI_JOB_TOKEN']
#except:
#    pass
#else:

# private token or personal token authentication
gl = gitlab.Gitlab('https://gitlab.com', private_token=ci_job_token)

#project = gl.projects.get('28204898', lazy=True)
project = gl.projects.get(project_id, lazy=True)

for mr in project.mergerequests.list():
    if mr.source_branch =='development':
        mr_title = mr.title
        mr_first_commit = mr.sha

if get_first_commit:

    print('{0}'.format(mr_first_commit))
    #for mr in gl.mergerequests.list():
    #for mr in project.mergerequests.list():
        #print('\n\nMR=[-{0}-]'.format(mr))
        #print('\n\nsource_branch=[-{0}-]'.format(mr.source_branch))
        #print('\n\nsha=[-{0}-]'.format(mr.sha))
        #print('{0}'.format(mr.sha))

if get_mr_title:

    print('{0}'.format(mr_title))
