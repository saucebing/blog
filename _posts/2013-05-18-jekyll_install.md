---
layout: default
title: How to install jekyll
category: Linux_tools
---

##{{ page.title }}

###install ruby

*sudo emerge ruby*

###check the ruby version

*ruby -v*

if the verson is not 1.9.3,then you should use rvm to provide a virtual environment.

reference link[how to install ruby by rvm](http://octopress.org/docs/setup/rvm/)

###install jekyll

install rvm

*curl -L https://get.rvm.io | bash -s stable --ruby*

curl的使用方法参见[how to use curl](http://blog.sina.com.cn/s/blog_485acedb0100i261.html)

if curl does not work,you can go to your browser,and then copy the newurl to replace https://get.rvm.io

install ruby 1.9.3

*rvm install 1.9.3*

*rvm use 1.9.3*

*rvm rubygems latest*

check the version of ruby to be 1.9.3

*ruby -v*

sudo gem install jekyll

(gem is the ruby package manager)

If this process is too long to response,then it maybe rubygems.org is blocked by the firewall(What the fuck!)You can modify the source to taobao

*gem sources --remove https://rubygems.org/*

*gem sources -a http://ruby.taobao.org/*

*gem source -l*

It should be:

http://ruby.taobao.org

###using jekyll

change directory to your blog root directory

*cd ~/blog*

*jekyll server*

###open browers and type *localhost:4000* and then you can see the result




