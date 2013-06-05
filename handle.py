#!/usr/bin/python
import re,os,sys

post_dir = "./_posts"
category_dir = "./category"
category_list = []
link_list = '<ul><li><a href="/index.html">index</a></li>'
Default_Action = "update"
Clean_Action = "clean"
Error_Prompt = "Are you kidding?"

def read_arg():
	action = Default_Action
	if len(sys.argv) > 1:
		action = sys.argv[1]
	return action

def get_category_list():
	post_file_list = os.listdir(post_dir)
	reg_category = r'category: (.*)'
	pattern_category = re.compile(reg_category)
	for f in post_file_list:
		post_file_path = post_dir + '/' + f
		fp = open(post_file_path,'r')
		content = fp.read()
		fp.close()
		category_name = pattern_category.search(content).groups()
		category_list.append(category_name[0])

def clean_category_link():
	for key in set(category_list):
		print key
		category_file_path = category_dir + '/' + key + '.html'
		rm_command = 'rm ' + category_file_path
		git_rm_command = 'git rm ' + category_file_path 
		print os.popen(rm_command).read()
		print os.popen(git_rm_command).read()

def create_category_link():
	for key in set(category_list):
	#	print key
		example_file_path = category_dir + '/example.html'
		category_file_path = category_dir + '/' + key + '.html'
		cp_command = 'cp ' + example_file_path + ' ' + category_file_path
		print os.popen(cp_command).read()
		f = open(category_file_path,'r')
		content = f.read()
		f.close()
		f = open(category_file_path,'w')
		content = content.replace('example',key)
		f.write(content)
		f.close()
		href = '/' + key + '.html'
		link = '<li><a href="/category' + href + '">' + key + '</a></li>'
		global link_list
		link_list = link_list + link

def update_category_link():
	global link_list
	link_list = link_list + '</ul>'
	#print link_list
	cp_command = 'cp ./_layouts/default_fallback.html ./_layouts/default.html'
	print os.popen(cp_command).read()
	layout_file_path = './_layouts/default.html'
	layout = open(layout_file_path,'r')
	content_layout = layout.read()
	layout.close()
	layout = open(layout_file_path,'w')
	content_layout = content_layout.replace('CATEGORY_LIST',link_list)
	layout.write(content_layout)
	layout.close()

def start():
	action_user = read_arg()
	if action_user == Default_Action:
		get_category_list()
		create_category_link()
		update_category_link()
	elif action_user == Clean_Action:
		get_category_list()
		clean_category_link()
	else:
		print Error_Prompt
		quit()

start()
	

