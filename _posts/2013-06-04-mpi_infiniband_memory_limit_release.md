---
layout: default
title: How to release mpi memory limit in infiniband network
category: MPI
---

##{{ page.title }}

###Modify linux memory limit script:

*cd /etc/security/limits

*\*hard memlock unlimited

*\*soft memlock unlimited

*\*hard data unlimited

*\*soft data unlimited

*\*hard core unlimited

*\*soft core unlimited

###Modify infiniband memory limit script:

*echo "options mlx4_core log_num_mtt=24" > /etc/modprobe.d/mofed.conf
