from time import sleep
from kubernetes import client, config
import random
import re
from datetime import datetime
import argparse


def get_pod_name(item):
    pod_name = item.metadata.name
    if re.match(r"s[0-9]+", pod_name):
        return True, pod_name
    else:
        return False, item

def kill_pod(api, ret):
  while(len(ret.items)):
    item = random.choice(ret.items)
    chosen_item = get_pod_name(item)
    if chosen_item[0]:
        try:
          print(f"# Killing pod: '{chosen_item[1]}'\tat {datetime.now()}")
          api.delete_namespaced_pod(chosen_item[1], "default")
        except Exception as err:
          print(f"Error deleting pod: {err}")
        return
    else:
        ret.items.remove(chosen_item[1])
  print("Error: no pods found. Check your deployments and try again.")


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("--kill-time", help="Input the interval between deletion of pods (in seconds)")
  kill_time = int(parser.parse_args().kill_time)

  config.load_kube_config()
  v1 = client.CoreV1Api()

  print(f"\n#### pyMonkey will kill for you a pod of uBench each {kill_time} seconds ####\n")
  print ("Starting killing pods... ")
  sleep(3)

  while True:
    try:
      ret = v1.list_namespaced_pod("default")
      kill_pod(v1, ret)
      sleep(kill_time)
    except KeyboardInterrupt:
      print('\nExiting pyMonkey...')
      exit(1)
    except Exception as err:
      print(f"Error: {err}")
      exit(1)

if __name__ == "__main__":
  main()
