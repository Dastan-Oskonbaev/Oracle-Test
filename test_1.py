def check_relation(net, name1, name2):
    connections = {}
    for name_a, name_b in net:
        if name_a not in connections:
            connections[name_a] = []
        if name_b not in connections:
            connections[name_b] = []
        connections[name_a].append(name_b)
        connections[name_b].append(name_a)

    visited = set()
    queue = [name1]
    while queue:
        current_name = queue.pop(0)
        if current_name == name2:
            return True
        if current_name not in visited:
            visited.add(current_name)
            queue.extend(connections[current_name])
    return False

net = (
    ("Нурбакыт", "Арслан"), ("Жанар", "Эмир"),
    ("Бегимай", "Улук"), ("Эрнис", "Мырза"),
    ("Талгат", "Айдар"), ("Таалай", "Айнуска"),
    ("Назима", "Айжан"), ("Ислам", "Махабат"),
    ("Нурсултан", "Айжаркын"), ("Элиза", "Алибек")
)

print(check_relation(net, "Нурбакыт", "Айжаркын"))
