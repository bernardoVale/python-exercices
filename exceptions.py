try:
    x = 5 + 'hey'
except TypeError:
    print("wont see")
finally:
    print("hello")

    #
    # try:
    #     child = subprocess.Popen(['java', '-version'], stderr=subprocess.PIPE)
    #     _, output = child.communicate()
    #     regex = re.search(r'(java version).*"(\d+\.\d).*', output.decode('utf-8'))
    #     if regex is not None:
    #         return regex.group(2)
    # # In case Java isn't found simply return None
    # except OSError:
    #     pass