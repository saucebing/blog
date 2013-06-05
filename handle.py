#!/usr/bin/python
import re
import os
post_dir = "./_posts"
filelist = os.listdir(post_dir)
pattern_category = re.compile(r'category: (.*)')
category_list = []
link_list = '<ul><li><a href="/index.html">index</a></li>'
for f in filelist:
	fp = open(post_dir + '/' + f,'r')
	content = fp.read()
	fp.close()
	category_name = pattern_category.search(content).groups()
	category_list.append(category_name[0])
for key in set(category_list):
	print key
	command = 'cp example.html ' + key + '.html'
	print os.popen(command).read()
	f = open(key + '.html','r')
	content = f.read()
	f.close()
	f = open(key + '.html','w')
	content = content.replace('example',key)
	f.write(content)
	f.close()
	href = '/' + key + '.html'
	link = '<li><a href="' + href + '">' + key + '</a></li>'
	link_list = link_list + link
link_list = link_list + '</ul>'
print link_list
command = 'cp ./_layouts/default_fallback.html ./_layouts/default.html'
print os.popen(command).read()
layout = open('./_layouts/default.html','r')
content_layout = layout.read()
layout.close()
layout = open('./_layouts/default.html','w')
content_layout = content_layout.replace('loading',link_list)
layout.write(content_layout)
layout.close()
