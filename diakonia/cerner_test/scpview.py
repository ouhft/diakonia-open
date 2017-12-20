#!/usr/bin/python
"""
A series of utility functions to parse the output of SCPView and help render it into more analysable forms
"""
import io
import re


"""
Service Utils

Looking at the `service` output, and the `service id#` outputs. 

services = dictionary of { domain: { node: { service_number: { service, state, messages, servers } } } }
* domain: str - domain name, e.g. "D0481"
* node: str - the node name e.g. "ouhukapp3"
* service_number: int - the id of the service from scp view
* service: str - service name
* state: str - typically "registered"
* messages: int - count of messages for service at time of output
* servers: dictionary { id (int): name (str) } of server objects related to this service

"""


def get_services(filename):
    results = dict()
    with io.open(filename, 'r') as file:
        current_domain = ""
        current_node = ""
        current_service_number = None

        for raw_line in file:
            raw_line = raw_line.strip()
            # Skip blank lines
            if raw_line == "":
                continue
            # Skip command lines
            elif raw_line[:4].lower() == "scp>":
                continue
            # Look for header lines
            elif raw_line[:8].lower() == "service ":  # note space to avoid "service:"
                matches = re.compile(r'Service ([0-9]+) registered on node \[(\w+)\] in domain \[(\w+)\]').findall(raw_line)
                current_domain = str(matches[0][2])
                current_node = str(matches[0][1])
                current_service_number = int(matches[0][0])
                print("{0}, {1}, {2}".format(current_domain, current_node, current_service_number))
                if current_domain not in results:
                    print("DEBUG: New Domain: {0}".format(current_domain))
                    results[current_domain] = dict()
                if current_node not in results[current_domain]:
                    print("DEBUG: New Node: {0}".format(current_node))
                    results[current_domain][current_node] = dict()
                if current_service_number not in results[current_domain][current_node]:
                    print("DEBUG: New Service ID: {0}".format(current_service_number))
                    results[current_domain][current_node][current_service_number] = dict()

            else:
                split_line = raw_line.split(":")
                if split_line[0].lower() == "service":
                    results[current_domain][current_node][current_service_number]["service"] = split_line[1].strip()
                elif split_line[0].lower() == "state":
                    results[current_domain][current_node][current_service_number]["state"] = split_line[1].strip()
                elif split_line[0].lower() == "messages":
                    results[current_domain][current_node][current_service_number]["messages"] = int(split_line[1])
                elif split_line[0].lower() == "servers":
                    results[current_domain][current_node][current_service_number]["servers"] = dict()
                    if split_line[1] is "":  # If there are no servers, skip this section
                        continue
                    server_split = split_line[1].split("-")
                    server_id = int(server_split[0].strip())
                    server_name = server_split[1].strip()
                    results[current_domain][current_node][current_service_number]["servers"][server_id] = server_name
                else:
                    # elif raw_line is not "":
                    server_split = raw_line.split("-")
                    server_id = int(server_split[0].strip())
                    server_name = server_split[1].strip()
                    results[current_domain][current_node][current_service_number]["servers"][server_id] = server_name
                # else:
                #     continue

    return results

