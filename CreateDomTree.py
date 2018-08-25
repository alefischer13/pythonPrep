class node:
    def __init__(self, data):
        self.data = data
    children = []


def createTree():
    tags = "<html><head><body></body></head><footer></footer></html>"
    listOfTags = tags.split('><')
    newFirst = listOfTags[0].replace('<','')
    newLast = listOfTags[-1].replace('>','')
    listOfTags[0] = newFirst
    listOfTags[-1] = newLast
    current = node(listOfTags[0])
    stack = []
    stack.append(current)
    index = 1
    print(listOfTags[0])
    while len(stack) > 0:
        while index < listOfTags.len(listOfTags):
            if listOfTags[index][0] == '/':
                print('hi')
            else:
                newNode = node(listOfTags[index])
                current.children.append(newNode)
                stack.append(newNode)
                current = newNode
                print('     ' + current.data)


def main():
    createTree()


if __name__ == "__main__":
    main()

