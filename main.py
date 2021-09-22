#!/usr/bin/env python3

"""

"""
import json
from pprint import pprint
import subprocess
import sys


def main(args):
    exec_cmd("/ip dhcp-server lease print")


def load_input(input_file='input.json'):
    with open(input_file, 'r') as inf:
        loaded_dict = json.load(inf)
    return loaded_dict


def exec_cmd(cmd, shell_script='ssh_cmd.sh', input_file='ssh_cmd.sh'):
    """
    """
    hosts = load_input()
    pprint(hosts)

    # Запуск выполнения команды на каждом узле без ожидания её завершения.
    for ip in hosts['devices'].keys():
        hosts['devices'][ip]['process'] = subprocess.Popen(['./'+shell_script,
                                                            hosts['credentials']['login'],
                                                            hosts['credentials']['password'],
                                                            ip,
                                                            hosts['defaults']['port'],
                                                            cmd],
                                                           stdout=subprocess.PIPE,
                                                           stdin=subprocess.PIPE,
                                                           stderr=subprocess.PIPE,
                                                           encoding='UTF-8'
                                                           )

    for ip in hosts['devices'].keys():
        hosts['devices'][ip]['output'], hosts['devices'][ip]['error'] = hosts['devices'][ip]['process'].communicate()
        del(hosts['devices'][ip]['process'])
    pprint(hosts)

    with open('output.json', 'w') as ouf:
        ouf.write(json.dumps(hosts['devices']))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) or 0)
