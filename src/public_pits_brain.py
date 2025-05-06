import json

class PublicPitsBrain:
    def __init__(self):
        self.root_memory = self.load_memory("memory/root_memory.json")
        self.flow_memory = self.load_memory("memory/flow_memory.json")
        self.forget_memory = self.load_memory("memory/forgettable_memory.json")

    def load_memory(self, file):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except:
            return {"entries": []}

    def query(self, user_input):
        prompt = f"""
You are a public Pits AI.
Root memory: {self.root_memory}
Recent interactions: {self.flow_memory}
User: {user_input}
"""
        return prompt

    def update_flow_memory(self, user_input):
        self.flow_memory["entries"].append({"user": user_input})
        self.save_memory("memory/flow_memory.json", self.flow_memory)

    def save_memory(self, file, data):
        with open(file, "w") as f:
            json.dump(data, f, indent=2)
