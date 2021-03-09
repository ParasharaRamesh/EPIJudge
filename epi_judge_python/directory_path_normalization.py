from test_framework import generic_test

def isCurrDirectoryRedirection(subPath):
    return subPath == "."

def isPreviousDirectoryRedirection(subPath):
    return subPath == ".."

def isEmpty(l):
    return len(l) == 0

def shortest_equivalent_path(path: str) -> str:
    startsWithSlash = path[0] == "/"
    subPaths = list(filter(lambda x : x != '' , path.split("/")))
    newSubPaths = []

    if startsWithSlash:
        newSubPaths.append("/")

    for subPath in subPaths:
        if isEmpty(newSubPaths) and not isCurrDirectoryRedirection(subPath):
            newSubPaths.append(subPath)
        elif isCurrDirectoryRedirection(subPath):
            continue
        elif isPreviousDirectoryRedirection(subPath):
            if isEmpty(newSubPaths):
                newSubPaths.append(subPath)
            elif not isPreviousDirectoryRedirection(newSubPaths[-1]):
                newSubPaths.pop()
            else:
                newSubPaths.append(subPath)
        else:
            newSubPaths.append(subPath)

    if startsWithSlash:
        if len(newSubPaths) == 1:
            return "/"
        else:
            return f"{'/'.join(newSubPaths)}"[1:]
    elif len(newSubPaths) == 0:
        return "."
    else:
        return '/'.join(newSubPaths)


if __name__ == '__main__':
    # print(shortest_equivalent_path("/"))
    # print(shortest_equivalent_path("."))
    # print(shortest_equivalent_path("a/b/c"))
    # print(shortest_equivalent_path("a/b/../d"))
    # print(shortest_equivalent_path("a/././b/c/./../d"))
    # print(shortest_equivalent_path("../../local"))
    # print(shortest_equivalent_path("/foo/../foo/./../"))
    # print(shortest_equivalent_path("foo/../foo/./../"))
    # print(shortest_equivalent_path(".././zEvLHA/..///DPpISML/../../././//../../../gpiY/../bFpMXW/.///fsQ//"))
    exit(generic_test.generic_test_main('directory_path_normalization.py', 'directory_path_normalization.tsv', shortest_equivalent_path))
