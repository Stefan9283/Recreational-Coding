

class Directory:
    def __init__(self, name, indent, parent=None) -> None:
        self.name = name
        self.indent = indent
        self.children = {}
        self.parent = parent

    def add_child(self, c):
        self.children[c.name] = c

    def accept(self, visitor): return visitor.visit_dir(self)
   

class File:
    def __init__(self, name, size, indent, parent) -> None:
        self.name = name
        self.size = size
        self.indent = indent
        self.parent = parent

    def accept(self, visitor): return visitor.visit_file(self)



tree = Directory('/', 0)

current_node = tree

cmds = list(map(str.split, map(str.rstrip, open('input').readlines())))

idx = 0

for cmd in cmds:
    tokens = cmd
    print(tokens)

    if tokens[1] == 'ls':
        continue
    elif tokens[1] == 'cd':
        if tokens[2] == '/':
            current_node = tree
        elif tokens[2] == '..':
            current_node = current_node.parent
        else:
            current_node = current_node.children[tokens[2]]
    elif tokens[0] == 'dir':
        current_node.add_child(
            Directory(tokens[1], current_node.indent + 1, current_node))
    else:
        current_node.add_child(
            File(tokens[1], int(tokens[0]), current_node.indent + 1, current_node))


class PrintVisitor:
    def visit(self, n):
        n.accept(self)

    def indent(self, i):
        for _ in range(i):
            print(' ', end='')

    def visit_dir(self, dir):
        self.indent(dir.indent)
        print('- {} (dir)'.format(dir.name))
        for child in dir.children:
            dir.children[child].accept(self)

    def visit_file(self, file):
        self.indent(file.indent)
        print('- {} (file, size={})'.format(file.name, file.size))

print()
PrintVisitor().visit(tree)


class AtMost100000Size:
    def __init__(self) -> None:
        self.sum = 0
        self.threshold = 100000

    def visit(self, n):
        return n.accept(self)

    def visit_dir(self, dir):
        s = 0
        for child in dir.children:
            s += dir.children[child].accept(self)
        if s < self.threshold:
            self.sum += s
            print(s, dir.name, self.sum)
        return s

    def visit_file(self, file):
        return file.size


print()
AtMost100000Size().visit(tree)




class GetUsedSpace:
    def visit(self, n):
        return n.accept(self)

    def visit_dir(self, dir):
        s = 0
        for child in dir.children:
            s += dir.children[child].accept(self)
        return s

    def visit_file(self, file):
        return file.size
    
    

available = 70000000 - GetUsedSpace().visit(tree)
needed = 30000000 


class SizesList:
    def visit(self, n):
        self.sizes = []
        return n.accept(self)

    def visit_dir(self, dir):
        s = 0
        for child in dir.children:
            s += dir.children[child].accept(self)
        self.sizes.append(s)
        return s

    def visit_file(self, file):
        return file.size
    
visitor = SizesList()
visitor.visit(tree)
sizes = sorted(visitor.sizes)

for size in sizes:
    if available + size >= needed:
        print(size)
        break