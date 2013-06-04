---
layout: default
title: Use netfilters/iptables as router
category: Linux
---

##{{ page.title }}

###Clarify network environment

The inner network is 192.168.0.0/24,and the outer network is 222.200.160.0/128

###Ensure the kernel support netfilters

*cd /usr/src/linux

*make menuconfig

![Can not load the picture](/image/6-4-2.png "title")

###Enable the router function of kernel

*cat 1 >> /proc/sys/net/ipv4/ip_forward

###Write a script `iptables.rule`:

*#!/usr/bin/bash

*iptables -F

*iptables -t nat -F

*iptables -t nat -A POSTROUTING -s 192.168.0.0/24 -o eth0 -j MASQUERADE

*iptables-save

###Enable iptables serivce

*./iptables.rule

*service iptables start

*chkconfig iptables on(CentOS)

*rc-update add iptables default(Gentoo)
