"""

OOP exercise

Source: https://www.youtube.com/watch?v=V8DGdPkBBxg

- build classes and script that lets you do this unit conversions
- using this example facts as reference
- the implementation would allow to resolve the example queries

example facts:
  m = 3.28 ft
  ft = 12 in
  hr = 60 min
  min = 60 sec

example queries:
  2 m = ? in --> answer = 78.72
  13 in = ? m --> answer = 0.330 (roughly)
  13 in = ? hr --> "not convertible!"

"""

class UnitConverter:
    def __init__(self):
        # adjacency list: {unit: [(neighbor, factor)]}
        self.graph = {}

    def add_conversion(self, u1, factor, u2):
        # ensure units exist in graph
        self.graph.setdefault(u1, [])
        self.graph.setdefault(u2, [])

        # add forward conversion (u1 -> u2)
        self.graph[u1].append((u2, factor))

        # add reverse conversion (u2 -> u1)
        # reverse factor = 1 / factor
        self.graph[u2].append((u1, 1 / factor))

    def convert(self, value, src, dst):
        # if units not known → not convertible
        if src not in self.graph or dst not in self.graph:
            return "not convertible!"

        # same unit → return original value
        if src == dst:
            return value

        visited = set()

        # DFS helper
        def dfs(current, acc):
            # if reached target → return accumulated value
            if current == dst:
                return acc

            visited.add(current)

            # explore neighbors
            for neighbor, factor in self.graph[current]:
                if neighbor not in visited:
                    # multiply accumulated value
                    result = dfs(neighbor, acc * factor)
                    if result is not None:
                        return result
            return None

        result = dfs(src, value)

        return result if result is not None else "not convertible!"


# ----- Script usage -----

converter = UnitConverter()

# given facts
converter.add_conversion("m", 3.28, "ft")
converter.add_conversion("ft", 12, "in")
converter.add_conversion("hr", 60, "min")
converter.add_conversion("min", 60, "sec")

print(converter.convert(2, "m", "in"))     # 78.72
print(round(converter.convert(13, "in", "m"), 3))  # 0.330
print(converter.convert(13, "in", "hr"))   # not convertible!