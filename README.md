# pyMonkey

This tiny python script will kill one pod of the [mSvcBench/MicroServiceSimulator](https://github.com/mSvcBench/MicroServiceSimulator) every chosen second.

First, install the dependencies:

```bash
pip install -r requirements.txt
```

Then, run (on the Kubernetes master node) the following command to kill one pod every 10 seconds:

```
$ python pymonkey.py --kill-time 20

#### pyMonkey will kill for you a pod of uBench each 20 seconds ####

Starting killing pods... 
# Killing pod: 's12-64fcb75cdd-7hfk4' at 2022-05-25 18:46:19.656305
# Killing pod: 's4-67798878b7-bgzlq' at 2022-05-25 18:46:39.702987
# Killing pod: 's10-5858cdf974-rx24m' at 2022-05-25 18:46:59.736331
# Killing pod: 's9-6c97dc4964-lt5fb' at 2022-05-25 18:47:19.779106
...
```

> **Node:** Be careful, the program will continue indefinitely if not stopped.