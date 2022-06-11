import requests
import json

class War:

    def __init__(self):
        self.war_info = None
        self.error = None

    def get_war_info(self, tier):
        """
        Makes request to API for war info
        """
        try:
            self.war_info = requests.get(f"http://127.0.0.1:8000/war/{tier}").json()
            self.get_war_nodes()
        except:
            print("Error in request")

    def get_war_nodes(self):
        """
        Converts the node numbers to description of node
        """
        with open("files/nodes.json", 'r') as file:
            all_nodes = json.load(file)

        new_nodes = self.war_info['nodes']
        for key, value in new_nodes.items():
            temp_nodes = {}
            for node in value:
                if node == "Null":
                    temp_nodes["DNF"] = "Don't have node data"
                else:
                    temp_nodes[node] = all_nodes[node]

            new_nodes[key] = temp_nodes

        self.war_info['nodes'] = new_nodes
