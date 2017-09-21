

def grep(pattern, content):

    # result = []
    #
    # list = content.split("\n")
    #
    # for line in list:
    #     if pattern in line:
    #         result.append(line)
    #
    #
    # return result

    return [x for x in content.split('\n') if pattern in x]